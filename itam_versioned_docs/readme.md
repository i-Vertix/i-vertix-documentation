

git clone https://github.com/glpi-project/doc.git glpi_orig
python itam_versioned_docs/md_conversion.py glpi_orig/source itam_versioned_docs/version-10
rm -rf itam_versioned_docs/version-10/
node scripts/build-sidebar.js  --version=10 --docs=itam && npm run start