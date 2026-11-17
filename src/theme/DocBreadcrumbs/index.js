import React from 'react';
import DocBreadcrumbs from '@theme-original/DocBreadcrumbs';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {useActivePlugin} from '@docusaurus/plugin-content-docs/client';
import styles from './styles.module.css';

// Monitoring Plugin Packs pages show the latest published Plugin Store release next to the breadcrumbs
export default function DocBreadcrumbsWrapper(props) {
    const {siteConfig} = useDocusaurusContext();
    const activePlugin = useActivePlugin();
    const release = siteConfig.customFields.pluginStoreRelease;

    if (activePlugin?.pluginId !== 'monitoringplugins' || !release) {
        return <DocBreadcrumbs {...props} />;
    }

    const label = `${release.plugin_version} - ${release.config_version}`;
    const anchor = label.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    return (
        <div className={styles.row}>
            <DocBreadcrumbs {...props} />
            <Link
                className={styles.release}
                to={`/monitoringplugins/monitoring-plugins/release-notes#${anchor}`}
                title="Latest published Plugin Store version - open the release notes">
                <span className={styles.releaseLabel}>Plugin Store</span>
                <span className={styles.releaseVersion}>{label}</span>
            </Link>
        </div>
    );
}
