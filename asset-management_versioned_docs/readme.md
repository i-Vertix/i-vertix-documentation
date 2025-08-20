
git clone https://github.com/glpi-project/doc.git glpi_orig

python asset-management_versioned_docs/md_conversion.py glpi_orig/source asset-management_versioned_docs/version-10

rm -rf asset-management_versioned_docs/version-10/
node scripts/build-sidebar.js  --versioning=10 --docs=asset-management \
&& npm run start

TODO:
- modules/overview/kanban:
  - the lists are messed up, even in original sources
- modules/assets:
  - a link points to the glpi plugin repository
  - wrong link
  - available types list is messed up
- modules/assets/computers
  - bridges link is broken
- modules/assets/software 
  - broken link
- modules/assets/tabs:
  - the whole section provides rst files that are included in modules/assets, maybe could be skipped or still interesting?
- modules/assistance/tickets
  - in the index all links are called ticket 