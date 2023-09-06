# i-Vertix Docs

## Develop Deploy Status

[![Netlify Status](https://api.netlify.com/api/v1/badges/04f466d1-1cb3-47a6-a9f9-8aa60a01545d/deploy-status)](https://app.netlify.com/sites/i-vertix-docs-dev/deploys)

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

**Monitoring**:

- [monitoring_versioned_sidebars/22.04-sidebar.yaml](./monitoring_versioned_sidebars/22.04-sidebar.yaml)

### Build Sidebar

To build the different sidebars use following commands:

#### Monitoring:

**22.04**

```bash
npm run build-sidebar-monitoring -- --version=22.04
```

**22.10**

```bash
npm run build-sidebar-monitoring -- --version=22.10
```

## Algolia Search

Algolia search is already enabled by the docusaurus.config.js

## Algolia Crawler

Docker container with following configuration files:

- docsearch.config.json
- .env

To start the crawler (docker container) you can use following command inside the directory where also the above 2 files
are located:

```bash
docker run -it --env-file=.env -e "CONFIG=$(cat config.json | jq -r tostring)" algolia/docsearch-scraper
```