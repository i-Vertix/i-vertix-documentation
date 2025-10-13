
git clone https://github.com/glpi-project/doc.git glpi_orig

python asset-management_versioned_docs/md_conversion.py glpi_orig/source asset-management_versioned_docs/version-10

rm -rf asset-management_versioned_docs/version-10/
node scripts/build-sidebar.js  --versioning=10 --docs=asset-management \
&& npm run start

TODO:

- come verrà mantenuto il manuale?
  - aggiornamenti?
  - merge quando verrà modificata la doc originale?
- come gestire gli errori nella documentazione originale?
  - fork sorgenti + sottomodulo git
- cosa fare con i comandi cli? sono tipo glpi:

- modules/assets/index:
  - a link (documentation) points to the glpi agent repository (to be replaced)

- modules/configuration/plugins
  - is it something that should be published?

- cli:
  - needs to be published?