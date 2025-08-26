
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

- modules/overview/kanban:
  - the lists are messed up, even in original sources
- modules/assets:
  - a link points to the glpi plugin repository
  - wrong link
- modules/assets/computers
  - bridges link is broken
- modules/assets/software
  - broken link
- modules/assistance/tickets/ticketopening/:
  - all links are broken
- modules/administration/groups
  - broken link
- modules/configuration/collectors
  - broken link
- modules/configuration/notifications/alarm_options
  - list is messed up, even in original sources
- modules/configuration/crontasks
  - fix crontab entry
- modules/configuration/external_links
  - list items are not italic or bold
- modules/configuration/plugins
  - is it something that should be published?
- glossary:
  - wrong format
- cli:
  - needs to be published?