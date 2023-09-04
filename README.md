# i-Vertix Docs

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