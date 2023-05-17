// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: 'i-Vertix Documentation',
    tagline: 'Managing an IT infrastructure has never been easier',
    favicon: 'img/logo-ivertix-100.png',

    // Set the production url of your site here
    url: 'https://docs.i-vertix.cloud',
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: '/',

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: 'i-Vertix', // Usually your GitHub org/user name.
    projectName: 'i-vertix-documentation', // Usually your repo name.

    onBrokenLinks: 'throw',
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
                id: 'log-management',
                label: 'Log & Data Management',
                description: 'Hi, this is a description text. I am very long',
                icon: '/img/logo-log-management-1000.png',
                Image: '/img/logo-log-management-1000.png',
                to: '/log-management/intro',
                color: 'ivertix-log-management',
                banner: "news"
            },
            {
                id: 'monitoring',
                label: 'IT Monitoring',
                description: 'Hi, this is a description text. I am very long',
                icon: '/img/logo-monitoring-1000.png',
                Image: '/img/logo-monitoring-1000.png',
                to: '/monitoring/intro',
                color: 'ivertix-monitoring',
                banner: "news"
            },
            {
                id: 'asset-management',
                label: 'IT Asset Management',
                description: 'Hi, this is a description text. I am very long',
                icon: '/img/logo-asset-management-1000.png',
                Image: '/img/logo-asset-management-1000.png',
                to: '/asset-management/intro',
                color: 'ivertix-asset-management',
            }
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
                sidebarPath: require.resolve('./sidebarsAssetManagement.js'),
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
                sidebarPath: require.resolve('./sidebarsLogManagement.js'),
                includeCurrentVersion: false
                // ... other options
            },
        ],
    ],

    themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
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
                        label: 'Product Documentation',
                        position: 'left',
                        items: [
                            {
                                label: "IT Monitoring",
                                description: "Keep a 360° view of your IT infrastructure",
                                icon: "/img/logo-monitoring-100.png",
                                id: "ivertix-monitoring",
                                docsPluginId: "monitoring"
                            },
                            {
                                label: "Log & Data Management",
                                description: "Analyze logfiles and network traffic in real time",
                                icon: "/img/logo-log-management-100.png",
                                id: "ivertix-log-management",
                                docsPluginId: "log-management"
                            },
                            {
                                label: "IT Asset Management",
                                description: "Automatically manage, track, inventory and update your IT assets",
                                icon: "/img/logo-asset-management-100.png",
                                id: "ivertix-asset-management",
                                docsPluginId: "asset-management"
                            }
                        ]
                    },
                    {
                        href: "https://i-vertix.com/en/blog/",
                        label: "Blog",
                        target: '_blank'
                    },
                    {
                        href: "https://www.i-vertix.com/",
                        position: "right",
                        className: "header-icon-link header-homepage-link",
                    },
                    {
                        href: "https://www.linkedin.com/company/i-vertix/",
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
                        title: 'Products',
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
                    // {
                    //     title: 'Community',
                    //     items: [
                    //         {
                    //             label: 'Stack Overflow',
                    //             href: 'https://stackoverflow.com/questions/tagged/docusaurus',
                    //         },
                    //         {
                    //             label: 'Discord',
                    //             href: 'https://discordapp.com/invite/docusaurus',
                    //         },
                    //         {
                    //             label: 'Twitter',
                    //             href: 'https://twitter.com/docusaurus',
                    //         },
                    //     ],
                    // },
                    {
                        title: 'Follow us on',
                        items: [
                            {
                                html: `
<a href="https://www.linkedin.com/company/i-vertix/" target="_blank" rel="noreferrer noopener" aria-label="i-Vertix on LinkedIn">
    <img src="/img/socials/linkedin.svg" alt="LinkedIn" width="32" height="32" />
</a>
<a href="https://www.linkedin.com/company/i-vertix/" target="_blank" rel="noreferrer noopener" aria-label="i-Vertix on Youtube">
    <img src="/img/socials/youtube.svg" alt="LinkedIn" width="32" height="32" />
</a>`,
                            }
                        ],
                    },
                ],
                logo: {
                    alt: 'i-Vertix',
                    src: 'img/logo-ivertix-100.png',
                    href: 'https://i-vertix.com',
                    width: 100,
                    height: 100,
                },
                copyright: `Copyright © ${new Date().getFullYear()} i-Vertix`,
            },
            prism: {
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme,
            },
        }),
};

module.exports = config;
