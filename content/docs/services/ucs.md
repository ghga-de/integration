---
title: "Upload Controller Service"
date: 2023-03-14 09:37:32.947693+00:00
draft: false
service_name: "upload-controller-service"
---


# Upload Controller Service

[ghga-de/upload-controller-service](https://github.com/ghga-de/upload-controller-service)

[ghga/upload-controller-service](https://hub.docker.com/r/ghga/upload-controller-service)

## Summary



## Provided

### REST API

This service provides a REST API with the following endpoints:

| Method | Path | Consumers |
| --- | --- | --- |
| `GET` | `/files/{file_id}` |  |
| `POST` | `/uploads` |  |
| `GET` | `/uploads/{upload_id}` |  |
| `PATCH` | `/uploads/{upload_id}` |  |
| `POST` | `/uploads/{upload_id}/parts/{part_no}/signed_urls` |  |


### Events

This service publishes the following event types through a message broker:

| Topic | Type | Consumers |
| --- | --- | --- |
| `file_uploads` | `file_upload_received` |  [Interrogation Room Service](../irs)<br> |


## Consumed

### REST API

This service relies on the following REST endpoints:

| Service | Method | Path |
| --- | --- | --- |


### Events

This service consumes the following events through the message broker:

| Topic | Type |
| --- | --- |
| `metadata` | `file_metadata_upserts` |
| `internal_file_registry` | `file_registered` |
| `file_interrogation` | `file_validation_failure` |



## Configuration

The service can be configured using the following configuration variables:

| Name | Description |
| --- | --- |
| `host` | The hostname or IP address to bind the HTTP server to |
| `port` | The port to bind the HTTP server to |
| `kafka_servers` | A list of Apache Kafka servers to connect to |
| `upload_rejected_event_topic` | An Apache Kafka event topic |
| `upload_rejected_event_type` | An Apache Kafka event schema |
| `upload_accepted_event_topic` | An Apache Kafka event topic |
| `upload_accepted_event_type` | An Apache Kafka event schema |
| `upload_received_event_topic` | An Apache Kafka event topic |
| `upload_received_event_type` | An Apache Kafka event schema |
| `file_metadata_event_topic` | An Apache Kafka event topic |
| `file_metadata_event_type` | An Apache Kafka event schema |
| `db_connection_str` | The MongoDB connection URI |
| `db_name` | The MongoDB database name |
| `s3_endpoint_url` | The S3 endpoint URL |
| `s3_access_key_id` | The S3 access key ID |
| `s3_secret_access_key` | The S3 secret access key |
