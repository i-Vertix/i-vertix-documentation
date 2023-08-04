# i-Vertix Docs

## Algolia Search

Algolia search is already enabled by the docusaurus.config.js

## Algolia Crawler

Docker container with following configuration files:
- docsearch.config.json
- .env

To start the crawler (docker container) you can use following command inside the directory where also the above 2 files are located:

`docker run -it --env-file=.env -e "CONFIG=$(cat config.json | jq -r tostring)" algolia/docsearch-scraper`