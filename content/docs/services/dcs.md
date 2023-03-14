---
title: "Download Controller Service"
date: 2023-03-14 09:37:32.915850+00:00
draft: false
service_name: "download-controller-service"
---


# Download Controller Service

[ghga-de/download-controller-service](https://github.com/ghga-de/download-controller-service)

[ghga/download-controller-service](https://hub.docker.com/r/ghga/download-controller-service)

## Summary



## Provided

### REST API

This service provides a REST API with the following endpoints:

| Method | Path | Consumers |
| --- | --- | --- |
| `GET` | `/objects/{object_id}` |  |


### Events

This service publishes the following event types through a message broker:

| Topic | Type | Consumers |
| --- | --- | --- |
| `file_downloads` | `download_served` |  |
| `file_downloads` | `file_registered` |  |
| `file_downloads` | `unstaged_download_requested` |  |


## Consumed

### REST API

This service relies on the following REST endpoints:

| Service | Method | Path |
| --- | --- | --- |


### Events

This service consumes the following events through the message broker:

| Topic | Type |
| --- | --- |
| `internal_file_registry` | `file_registered` |



## Configuration

The service can be configured using the following configuration variables:

| Name | Description |
| --- | --- |
| `host` | The hostname or IP address to bind the HTTP server to |
| `port` | The port to bind the HTTP server to |
| `kafka_servers` | A list of Apache Kafka servers to connect to |
| `download_served_event_topic` | An Apache Kafka event topic |
| `download_served_event_type` | An Apache Kafka event schema |
| `file_registered_event_topic` | An Apache Kafka event topic |
| `file_registered_event_type` | An Apache Kafka event schema |
| `files_to_register_topic` | An Apache Kafka event topic |
| `files_to_register_type` | An Apache Kafka event schema |
| `unstaged_download_event_topic` | An Apache Kafka event topic |
| `unstaged_download_event_type` | An Apache Kafka event schema |
| `db_connection_str` | The MongoDB connection URI |
| `db_name` | The MongoDB database name |
| `s3_endpoint_url` | The S3 endpoint URL |
| `s3_access_key_id` | The S3 access key ID |
| `s3_secret_access_key` | The S3 secret access key |
