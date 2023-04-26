# Integration
Repository for GHGA microservice manifests.

The Integration repository contains service manifests in YAML format for each microservice within the [GHGA](https://github.com/ghga-de). 

Service manifests follow [schema.json](https://github.com/ghga-de/integration/blob/9c8d1c80bab3af0062ac0a59f1117252bfe7285e/schema.json) and serve multiple purposes, including service logic validation, documentation and visualization of the service landscape. As well as supporting the (semi) automatic generation of helm charts, docker-compose files, etc.

You can access auto-generated service documentation at https://ghga-de.github.io/integration.

## Repository Structure

```
├── schema.json
├── services
│   ├── microservice1.yaml
│   ├── microservice2.yaml
│   ├── ...
├── html
│   ├── config.toml
```
**schema.json**: JSON schema used to validate the service schema.

**services**: Service manifests in YAML format

**html**: Configuration for auto-generated web interface

## Usage
The service manifests in this repository have several use cases, including:

- Facilitating service logic validation.
- Enabling human-readable documentation and visualization of the service landscape.
- Supporting the (semi) automatic generation of helm charts, docker-compose files, and other such resources.

### [ghga-devutil](https://github.com/ghga-de/ghga-devutil)
The **ghga-devutil** is a command-line tool designed to provide a proof-of-concept parser for manifests. It annotates services and generate markdown files. It can also build a web interface from manifests that serves as human-readable documentation for the GHGA service landscape. 

For more information, please visit [ghga-de/ghga-devutil](https://github.com/ghga-de/ghga-devutil)

## License
This repository is free to use and modify according to the [Apache 2.0 License](https://github.com/ghga-de/microservice-repository-template/blob/main/LICENSE).
