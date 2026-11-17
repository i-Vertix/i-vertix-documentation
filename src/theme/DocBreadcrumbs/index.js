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

    // the latest release is the first entry of the release notes (its anchor is raw HTML in <summary>, which the
    // build's broken-anchor check does not see, so the link points to the page)
    const label = `${release.plugin_version} - ${release.config_version}`;
    return (
        <div className={styles.row}>
            <DocBreadcrumbs {...props} />
            <Link
                className={styles.release}
                to="/monitoringplugins/monitoring-plugins/release-notes"
                title="Latest published Plugin Store version - open the release notes">
                <span className={styles.releaseLabel}>Plugin Store</span>
                <span className={styles.releaseVersion}>{label}</span>
            </Link>
        </div>
    );
}
