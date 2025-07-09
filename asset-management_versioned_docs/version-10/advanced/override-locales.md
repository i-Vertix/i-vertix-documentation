---
id: override-locales
title: Override Locales
---

# Override i-Vertix ITAM locales

i-Vertix ITAM uses the [gettext](https://www.gnu.org/software/gettext/) tool to
manage its translations. You can override the default. This is the
preferred method rather than editing the original po files and risk
losing your changes when updating i-Vertix ITAM.

To do so, you need to create a file named `filename.po` in the
`files/_locales/core/` directory. You can also create overrides for
plugins with the same method in `files/_locales/pluginkey/` directory
where `pluginkey` matches the plugin folder name.

:::info

Depending on your i-Vertix ITAM configuration, the `_locales` directory can be
located elsewhere (if you provided a `local_define.php` file with a
`i-Vertix ITAM_LOCAL_I18N_DIR` constant). It's possible to have multiple
files, to manage several languages for example.

:::

The file must be a valid [gettext] file. You can use
[Poedit](https://poedit.net/) to create it.

``` po
# Override PO file
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2019-04-13 10:43+0200\n"
"PO-Revision-Date: 2019-04-13 10:43+0200\n"
"Last-Translator: Automatically generated\n"
"Language-Team: none\n"
"Language: en_GB\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"

msgid "Login"
msgstr "Login from local gettext"
```

`msgid` is the source string, `msgstr` is the translation. You can find
the correct source sentences to use in the `locales/glpi.pot` file.

Next you need to compile your .po file into a .mo file readable by i-Vertix ITAM.
To do so, you can use the following command:

    $ cd files/_locales/core/
    $ msgfmt -o filename.mo filename.po

Finally, i-Vertix ITAM uses a cache system to avoid loading MO files at each
request. You need to clear the cache to see your changes. To do so, in
Debug mode, go to "Setup \> General", "Performance" tab and click on
"Reset" button on the "Translation cache" section. If you have
command-line access, you may also clear this cache using the
[glpi:cache:clear] CLI command. If you clear the cache with
the CLI command, make sure you run the command as the web server user.
