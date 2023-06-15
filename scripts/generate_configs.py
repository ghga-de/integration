#!/usr/bin/env python3
# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Script generates config according to service manifest and service config schema. """

import os
from pathlib import Path
from typing import Any, Optional
from pydantic import BaseModel, root_validator
import yaml
import requests

BASE_PATH = Path(__file__).parent.resolve().parent
SERVICE_PATH = BASE_PATH / "service_manifests"
FILE_MAPPING_PATH = BASE_PATH / "event_type_mapping.yaml"
OUTPUT_DIR = BASE_PATH / "generated_configs"


class ExtraConfiq(BaseModel):
    value: Optional[Any] = None
    value_instructions: Optional[Any] = None


class VaultDetails(BaseModel):
    path: str
    mode: str


class MongoDBDetails(BaseModel):
    db_name: str
    mode: str


class S3Details(BaseModel):
    bucket: str
    config_parameter: str
    mode: str


class Storage(BaseModel):
    s3: Optional[list[S3Details]] = None
    mongodb: Optional[MongoDBDetails] = None
    vault: Optional[list[VaultDetails]] = None


class RestConsumptionDetails(BaseModel):
    config_parameter: str


class RestProduces(BaseModel):
    public: bool
    gateway_prefix: Optional[str] = None

    @root_validator
    def check_gateway_prefix(cls, values: dict):
        if values["public"] and values["gateway_prefix"] is None:
            raise ValueError("You may only specify only if public is true")
        return values


class RestApi(BaseModel):
    produces: Optional[RestProduces] = None
    consumes: Optional[dict[str, RestConsumptionDetails]] = None


class EventDetails(BaseModel):
    config_parameter: str
    topic_config_parameter: str


class EventApi(BaseModel):
    produces: Optional[dict[str, EventDetails]] = None
    consumes: Optional[dict[str, EventDetails]] = None


class Api(BaseModel):
    rest: Optional[RestApi] = None
    events: Optional[EventApi] = None


class IntegrationManifest(BaseModel):
    shortname: str
    name: str
    version: str
    api: Api
    storage: Optional[Storage]
    extra_config: Optional[dict[str, ExtraConfiq]] = None


def get_event_type_mapping() -> dict[str, str]:
    with open(FILE_MAPPING_PATH, "r") as fm:
        return yaml.safe_load(fm)


def get_config_schema(service_name: str, version_number: str) -> dict[str, dict]:
    url = f"https://raw.githubusercontent.com/ghga-de/{service_name}/{version_number}/config_schema.json"
    response = requests.get(url=url)
    if requests.status_codes == 200:
        raise Exception
    config_schema = response.json()

    return config_schema


def get_default_configs(service_name: str, version_number: str) -> dict[str, Any]:
    config_schema = get_config_schema(
        service_name=service_name, version_number=version_number
    )
    config = {}

    for property, content in config_schema["properties"].items():
        value = content.get("default", "<Please fill>")
        config[property] = value

    return config


def get_integration_manifest(service_short_name: str) -> IntegrationManifest:
    file_path = SERVICE_PATH / f"{service_short_name}.yaml"

    with open(file_path, "r") as fh:
        manifest_dict = yaml.safe_load(fh)

    manifest = IntegrationManifest(**manifest_dict)

    return manifest


def get_config_from_manifest(
    manifest: IntegrationManifest, event_mapping: dict[str, str]
) -> dict[str, Any]:
    config = {}
    if manifest.api.rest:
        rest_manifest = manifest.api.rest
        if rest_manifest.consumes:
            for service_name, details in rest_manifest.consumes.items():
                config[
                    details.config_parameter
                ] = f"<Please fill with api url for service {service_name}>"

    if manifest.api.events:
        events = {}
        if manifest.api.events.produces:
            events.update(manifest.api.events.produces)
        if manifest.api.events.consumes:
            events.update(manifest.api.events.consumes)

        for event_type, details in events.items():
            if event_type not in event_mapping:
                raise Exception
            config[details.config_parameter] = event_type
            config[details.topic_config_parameter] = event_mapping[event_type]

    if manifest.storage:
        if manifest.storage.s3:
            for s3details in manifest.storage.s3:
                config[s3details.config_parameter] = s3details.bucket
        if manifest.storage.mongodb:
            config["db_name"] = manifest.storage.mongodb.db_name

    if manifest.extra_config:
        for config_name, details in manifest.extra_config.items():
            config[config_name] = (
                details.value or f"<Please fill - {details.value_instructions}>"
            )

    return config


def write_config(service_short_name: str, config: dict[str, Any]):
    file_name = f"{service_short_name}.yaml"
    file_path = OUTPUT_DIR / file_name
    with open(file_path, "w") as fp:
        yaml.safe_dump(config, fp)


def get_shortnames():
    return [filename.replace(".yaml", "") for filename in os.listdir(SERVICE_PATH)]


def generate_config_for_service(service_short_name: str):
    manifest = get_integration_manifest(service_short_name=service_short_name)
    config = get_default_configs(
        service_name=manifest.name, version_number=manifest.version
    )
    event_mapping = get_event_type_mapping()
    manifest_config = get_config_from_manifest(
        manifest=manifest, event_mapping=event_mapping
    )
    config.update(manifest_config)
    write_config(service_short_name=service_short_name, config=config)


def generate_config_for_services():
    shortnames = get_shortnames()
    for shortname in shortnames:
        print("service:", shortname)
        generate_config_for_service(service_short_name=shortname)


if __name__ == "__main__":
    generate_config_for_services()
