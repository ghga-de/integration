---
title: "Internal File Registry Service"
date: 2023-03-14 09:37:32.931867+00:00
draft: false
service_name: "internal-file-registry-service"
---


# Internal File Registry Service

[ghga-de/internal-file-registry-service](https://github.com/ghga-de/internal-file-registry-service)

[ghga/internal-file-registry-service](https://hub.docker.com/r/ghga/internal-file-registry-service)

## Summary

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque
pellentesque posuere ante, ac porttitor nulla eleifend quis. Mauris eget
aliquam diam. Duis laoreet blandit luctus. Donec at lacus porta, bibendum
lectus dignissim, eleifend est. Etiam sit amet blandit dui. Cras id ante et
neque hendrerit vulputate non aliquam eros.


## Provided

### REST API

This service provides a REST API with the following endpoints:

| Method | Path | Consumers |
| --- | --- | --- |


### Events

This service publishes the following event types through a message broker:

| Topic | Type | Consumers |
| --- | --- | --- |
| `internal_file_registry` | `file_registered` |  [Download Controller Service](../dcs)<br> [Upload Controller Service](../ucs)<br> |
| `internal_file_registry` | `file_staged_for_download` |  |


## Consumed

### REST API

This service relies on the following REST endpoints:

| Service | Method | Path |
| --- | --- | --- |


### Events

This service consumes the following events through the message broker:

| Topic | Type |
| --- | --- |
| `file_interrogation` | `file_validation_success` |
| `file_downloads` | `file_stage_requested` |



## Configuration

The service can be configured using the following configuration variables:

| Name | Description |
| --- | --- |
| `kafka_servers` | A list of Apache Kafka servers to connect to |
| `files_to_register_topic` | An Apache Kafka event topic |
| `files_to_register_type` | An Apache Kafka event schema |
| `file_staged_event_topic` | An Apache Kafka event topic |
| `file_staged_event_type` | An Apache Kafka event schema |
| `file_registered_event_topic` | An Apache Kafka event topic |
| `file_registered_event_type` | An Apache Kafka event schema |
| `files_to_stage_topic` | An Apache Kafka event topic |
| `files_to_stage_type` | An Apache Kafka event schema |
| `db_connection_str` | The MongoDB connection URI |
| `db_name` | The MongoDB database name |
| `s3_endpoint_url` | The S3 endpoint URL |
| `s3_access_key_id` | The S3 access key ID |
| `s3_secret_access_key` | The S3 secret access key |
