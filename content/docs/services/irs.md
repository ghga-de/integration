---
title: "Interrogation Room Service"
date: 2023-03-14 09:37:32.939792+00:00
draft: false
service_name: "interrogation-room-service"
---


# Interrogation Room Service

[ghga-de/interrogation-room-service](https://github.com/ghga-de/interrogation-room-service)

[ghga/interrogation-room-service](https://hub.docker.com/r/ghga/interrogation-room-service)

## Summary



## Provided

### REST API

This service provides a REST API with the following endpoints:

| Method | Path | Consumers |
| --- | --- | --- |


### Events

This service publishes the following event types through a message broker:

| Topic | Type | Consumers |
| --- | --- | --- |
| `file_interrogation` | `file_validation_success` |  [Internal File Registry Service](../ifrs)<br> |
| `file_interrogation` | `file_validation_failure` |  [Upload Controller Service](../ucs)<br> |


## Consumed

### REST API

This service relies on the following REST endpoints:

| Service | Method | Path |
| --- | --- | --- |
| `eks` | `/secrets` | `POST` |


### Events

This service consumes the following events through the message broker:

| Topic | Type |
| --- | --- |
| `file_uploads` | `file_upload_received` |



## Configuration

The service can be configured using the following configuration variables:

| Name | Description |
| --- | --- |
| `kafka_servers` | A list of Apache Kafka servers to connect to |
| `upload_received_event_topic` | An Apache Kafka event topic |
| `upload_received_event_type` | An Apache Kafka event schema |
| `interrogation_failure_topic` | An Apache Kafka event topic |
| `interrogation_failure_type` | An Apache Kafka event schema |
| `interrogation_success_topic` | An Apache Kafka event topic |
| `interrogation_success_type` | An Apache Kafka event schema |
| `s3_endpoint_url` | The S3 endpoint URL |
| `s3_access_key_id` | The S3 access key ID |
| `s3_secret_access_key` | The S3 secret access key |
