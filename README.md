# YAML K8S Split
[![Docker Pulls](https://img.shields.io/docker/pulls/illallangi/yamlk8ssplit.svg)](https://hub.docker.com/r/illallangi/yamlk8ssplit)
[![Image Size](https://images.microbadger.com/badges/image/illallangi/yamlk8ssplit.svg)](https://microbadger.com/images/illallangi/yamlk8ssplit)
![Build](https://github.com/illallangi/YAMLK8SSplit/workflows/Build/badge.svg)

Splits Kubernetes YAML resources into seperate files based on .kind, .metadata.namespace and .metadata.name.

## Installation

    sudo python -m pip install git+https://github.com/illallangi/YAMLK8SSplit.git

## Usage

    yamlk8ssplit *.yaml
