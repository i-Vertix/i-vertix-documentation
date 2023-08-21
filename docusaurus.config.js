// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: 'i-Vertix Documentation',
    tagline: 'Managing an IT infrastructure has never been easier',
    favicon: 'img/logo-ivertix-blue-100.png',

    // Set the production url of your site here
    // url: 'https://i-vertix.guide',
    url: 'https://i-vertix-docs-dev.netlify.app',
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: '/',

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: 'i-Vertix', // Usually your GitHub org/user name.
    projectName: 'i-vertix-documentation', // Usually your repo name.

    onBrokenLinks: 'warn',
    onBrokenMarkdownLinks: 'warn',

    // Even if you don't use internalization, you can use this field to set useful
    // metadata like html lang. For example, if your site is Chinese, you may want
    // to replace "en" with "zh-Hans".
    i18n: {
        defaultLocale: 'en',
        locales: ['en'],
    },

    customFields: {
        products: [
            {
                id: 'monitoring',
                label: 'IT Monitoring',
                description: 'i-Vertix IT Monitoring enables an extensive oversight of the IT environment, offering an integrated monitoring with immediate error correction',
                icon: '/img/logo-monitoring-1000.png',
                Image: '/img/logo-monitoring-1000.png',
                to: '/monitoring/intro',
            },
            // {
            //     id: 'log-management',
            //     label: 'Log & Data Management',
            //     description: 'Hi, this is a description text. I am very long',
            //     icon: '/img/logo-log-management-1000.png',
            //     Image: '/img/logo-log-management-1000.png',
            //     to: '/log-management/intro'
            // },
            // {
            //     id: 'asset-management',
            //     label: 'IT Asset Management',
            //     description: 'Hi, this is a description text. I am very long',
            //     icon: '/img/logo-asset-management-1000.png',
            //     Image: '/img/logo-asset-management-1000.png',
            //     to: '/asset-management/intro'
            // },
        ]
    },

    presets: [
        [
            '@docusaurus/preset-classic',
            {
                docs: false,
                theme: {
                    customCss: [require.resolve('./src/css/custom.css')],
                }
            }
        ]
    ],

    plugins: [
        [
            '@docusaurus/plugin-content-docs',
            {
                id: 'monitoring',
                path: 'monitoring',
                routeBasePath: 'monitoring',
                includeCurrentVersion: false
                // ... other options
            },
        ],
        [
            '@docusaurus/plugin-content-docs',
            {
                id: 'asset-management',
                path: 'asset-management',
                routeBasePath: 'asset-management',
                includeCurrentVersion: false
                // ... other options
            },
        ],
        [
            '@docusaurus/plugin-content-docs',
            {
                id: 'log-management',
                path: 'log-management',
                routeBasePath: 'log-management',
                includeCurrentVersion: false
                // ... other options
            },
        ],
    ],

    themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
            docs: {
                sidebar: {
                    hideable: true,
                    autoCollapseCategories: true
                }
            },
            algolia: {
                // The application ID provided by Algolia
                appId: '26QPCG4J0S',
                // Public API key: it is safe to commit it
                apiKey: 'd0e8f15baedb811b3e2468e17c1f603e',
                indexName: 'i-vertix-docs',
                // Optional: see doc section below
                contextualSearch: true,
                // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
                // externalUrlRegex: 'external\\.com|domain\\.com',
                // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
                // replaceSearchResultPathname: {
                //     from: '/docs/', // or as RegExp: /\/docs\//
                //     to: '/',
                // },
                // Optional: Algolia search parameters
                searchParameters: {},
                // Optional: path for search page that enabled by default (`false` to disable it)
                searchPagePath: 'search',
                //... other Algolia params
            },
            // Replace with your project's social card
            image: 'img/docusaurus-social-card.jpg',
            navbar: {
                title: '',
                logo: {
                    alt: 'i-Vertix',
                    src: 'img/logo-ivertix-100.png',
                },
                items: [
                    {
                        type: 'custom-ivertixDropdown',
                        label: 'Docs',
                        position: 'left',
                        items: [
                            {
                                label: "IT Monitoring",
                                description: "Keep a 360° view of your IT infrastructure",
                                icon: "/img/logo-monitoring-100.png",
                                id: "ivertix-monitoring",
                                docsPluginId: "monitoring"
                            },
                            // {
                            //     label: "Log & Data Management",
                            //     description: "Analyze logfiles and network traffic in real time",
                            //     icon: "/img/logo-log-management-100.png",
                            //     id: "ivertix-log-management",
                            //     docsPluginId: "log-management"
                            // },
                            // {
                            //     label: "IT Asset Management",
                            //     description: "Automatically manage, track, inventory and update your IT assets",
                            //     icon: "/img/logo-asset-management-100.png",
                            //     id: "ivertix-asset-management",
                            //     docsPluginId: "asset-management"
                            // }
                        ]
                    },
                    {
                        to: "https://i-vertix.com/en/blog/",
                        label: "Blog",
                        target: '_blank'
                    },
                    {
                        to: "https://helpdesk.i-vertix.cloud/",
                        position: "right",
                        label: "Helpdesk Portal"
                    },
                    {
                        to: "https://www.i-vertix.com/",
                        position: "right",
                        className: "header-icon-link header-homepage-link",
                    },
                    {
                        to: "https://www.linkedin.com/company/i-vertix/",
                        position: "right",
                        className: "header-icon-link header-linkedin-link",
                    },
                    // {
                    //     type: 'docsVersionDropdown',
                    //     docsPluginId: 'monitoring',
                    //     position: "right"
                    // },
                    // {
                    //     type: 'docsVersionDropdown',
                    //     docsPluginId: 'asset-management',
                    //     position: "right"
                    // },
                    // {
                    //     type: 'docsVersionDropdown',
                    //     docsPluginId: 'log-management',
                    //     position: "right"
                    // }
                ],
            },
            footer: {
                style: 'dark',
                links: [
                    {
                        title: 'Docs',
                        items: [
                            {
                                label: 'Monitoring',
                                to: '/monitoring/intro',
                            },
                            {
                                label: 'Asset Management',
                                to: '/asset-management/intro',
                            },
                            {
                                label: 'Log Management',
                                to: '/log-management/intro',
                            },
                        ],
                    },
                    {
                        title: 'Contact us',
                        items: [
                            {
                                label: 'sales@i-vertix.com',
                                to: 'mailto:sales@i-vertix.com',
                            },
                            {
                                label: '+39 0471 1430170',
                                to: 'tel:003904711430170',
                            }
                        ],
                    },
                    {
                        title: 'Links',
                        items: [
                            {
                                label: 'Helpdesk Portal',
                                to: "https://helpdesk.i-vertix.cloud/",
                            },
                            {
                                label: 'Credits',
                                to: 'https://i-vertix.com',
                            },
                            {
                                label: 'Legal information',
                                to: 'https://i-vertix.com',
                            }
                        ],
                    },
                    {
                        title: 'Follow us on',
                        items: [
                            {
                                html: `
<div class="footer__socials">
<a href="https://www.linkedin.com/company/i-vertix/" target="_blank" rel="noreferrer noopener" aria-label="i-Vertix on LinkedIn">
    <img src="/img/socials/linkedin.svg" alt="LinkedIn" width="32" height="32" />
</a>
<a href="https://www.youtube.com/channel/UCa38ZZWVFpCX5XhY8v0UFnQ" target="_blank" rel="noreferrer noopener" aria-label="i-Vertix on Youtube">
    <img src="/img/socials/youtube.svg" alt="Youtube" width="32" height="32" />
</a>
</div>
<div class="footer__capterra">
<a href="https://www.capterra.com/reviews/229594/i-Vertix-IT-Network-Monitoring--Management?utm_source=vendor&utm_medium=badge&utm_campaign=capterra_reviews_badge" target="_blank" rel="noreferrer noopener" aria-label="i-Vertix Reviews - Capterra">
    <img src="https://assets.capterra.com/badge/b04a3bce76c7bb9ae072469a6424cd7b.svg?v=2178388&p=229594" alt="Capterra" />
</a>
</div>`,
                            }
                        ],
                    },
                ],
                // logo: {
                //     alt: 'i-Vertix',
                //     src: 'img/logo-ivertix-100.png',
                //     href: 'https://i-vertix.com',
                //     width: 100,
                //     height: 100,
                // },
                copyright: `Copyright © ${new Date().getFullYear()} i-Vertix`,
            },
            prism: {
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme,
            },
        }),
};

module.exports = config;
