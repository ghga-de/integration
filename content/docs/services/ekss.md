---
title: "Encryption Key Store Service"
date: 2023-03-14 09:37:32.923863+00:00
draft: false
service_name: "encryption-key-store-service"
---


# Encryption Key Store Service

[ghga-de/encryption-key-store-service](https://github.com/ghga-de/encryption-key-store-service)

[ghga/encryption-key-store-service](https://hub.docker.com/r/ghga/encryption-key-store-service)

## Summary



## Provided

### REST API

This service provides a REST API with the following endpoints:

| Method | Path | Consumers |
| --- | --- | --- |
| `POST` | `/secrets` |  |
| `GET` | `/secrets/{secret_id}/envelopes/{client_pk}` |  |


### Events

This service publishes the following event types through a message broker:

| Topic | Type | Consumers |
| --- | --- | --- |


## Consumed

### REST API

This service relies on the following REST endpoints:

| Service | Method | Path |
| --- | --- | --- |


### Events

This service consumes the following events through the message broker:

| Topic | Type |
| --- | --- |



## Configuration

The service can be configured using the following configuration variables:

| Name | Description |
| --- | --- |
| `host` | The hostname or IP address to bind the HTTP server to |
| `port` | The port to bind the HTTP server to |
