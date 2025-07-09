

git clone https://github.com/glpi-project/doc.git glpi_orig

python asset-management_versioned_docs/md_conversion.py glpi_orig/source asset-management_versioned_docs/version-10

rm -rf asset-management_versioned_docs/version-10/
node scripts/build-sidebar.js  --version=10 --docs=assets-management && npm run start



TODO:
- sistemare boxes indentate
- parsing indici non in index.md
- path immagini
- opt: link assoluti