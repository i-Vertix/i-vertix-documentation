# i-Vertix Docs

## Develop Deploy Status

[![Netlify Status](https://api.netlify.com/api/v1/badges/04f466d1-1cb3-47a6-a9f9-8aa60a01545d/deploy-status)](https://app.netlify.com/sites/i-vertix-docs-dev/deploys)

## Install Dependencies

```bash
npm install
```

## Local Build

```bash
npm run start
```

## Menu Sidebar

### Define Sidebar

The Sidebar is defined in yaml format (simplified version) and is built later into the required json format.

The folder structure of the documentation instance (for example monitoring) is represented in the yaml file with
`id` as the folder name and the `label` as the displayed name in the sidebar for the folder.
`items` are the respective markdown files present in the folder (use the file name without file extension as value).

#### Monitoring Definition

- [monitoring_versioned_sidebars/22.04-sidebar.yaml](./monitoring_versioned_sidebars/22.04-sidebar.yaml)

### Build Sidebar

To build the different sidebars use following commands:

#### Build Monitoring Sidebar

##### 22.04

```bash
node scripts/build-sidebar.js --docs=monitoring --versioning="22.04"
```

##### 22.10

```bash
node scripts/build-sidebar.js --docs=monitoring --versioning="22.10"
```

##### 23.10

```bash
node scripts/build-sidebar.js --docs=monitoring --versioning="23.10"
```

##### 24.10

```bash
node scripts/build-sidebar.js --docs=monitoring --versioning="23.10"
```

## API Docs

Use following command to bundle the API documentation:

```bash
redocly bundle ./openapi-specs-orig/24.10/centreon-api.yaml -o ./monitoring_versioned_docs/version-24.10/api/rest-api-v2.json
```

Unfortunately the centreon api spec contains some errors which need to be fixed before making the bundle.

Most common errors while bundling:

- wrong references schemas using `$ref`
- wrong `ResourceHostDetail.yaml` and `ResourceServiceDetail.yaml` object structure

Most commong issues while rendering:

- usage of *type* `float` -> use `number` instead
- usage of *type* `int` -> use `integer` instead
- typo `descriptions` instead of `description`

## Algolia Search

Algolia search is already enabled by the docusaurus.config.js

## Algolia Crawler

The algolia crawler runs inside a docker container with following configuration files:

- docsearch.config.json
- .env (template available, get api keys from algolia dashboard)

To start the crawler (docker container) you can use following command inside the directory where also the above 2 files
are located:

```bash
docker run -it --env-file=.env -e "CONFIG=$(cat config.json | jq -r tostring)" algolia/docsearch-scraper
```

> **DocSearch Documentation**
>
> [https://docsearch.algolia.com/docs/legacy/run-your-own](https://docsearch.algolia.com/docs/legacy/run-your-own)
