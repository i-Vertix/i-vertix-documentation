import React from 'react';
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import VersionDropdown from '@theme/NavbarItem/DocsVersionDropdownNavbarItem';
import styles from './styles.module.css';
import {ProductItem} from "@site/src/components/Landing/ProductShowcase";
import clsx from "clsx";
import {useVersions} from "@docusaurus/plugin-content-docs/client";

// unversioned docs (e.g. monitoringplugins) only have the "current" version -> no version selector
const useIsVersioned = (docsPluginId: string) => {
    const versions = useVersions(docsPluginId);
    return !(versions.length === 1 && versions[0].name === "current");
};

const DesktopHeader = ({docConfig}: { docConfig: ProductItem }) => {
    const isVersioned = useIsVersioned(docConfig.id);
    return (
        <div className={styles.sidebarHeader}>
            <div className={styles.title}>
                <img src={docConfig.icon} alt={""}/>
                <span>{docConfig.label}</span>
            </div>
            {isVersioned && <div className={styles.version}>
                <VersionDropdown docsPluginId={docConfig.id}
                                 dropdownItemsBefore={[]}
                                 dropdownItemsAfter={[]}
                                 items={[]}/>
            </div>}
        </div>
    );
}

const MobileHeader = ({docConfig}: { docConfig: ProductItem }) => {
    const isVersioned = useIsVersioned(docConfig.id);
    return (
        <>
            <div className={clsx(styles.title, styles.mobileTitle)}>
                <img src={docConfig.icon} alt={""}/>
                <span>{docConfig.label}</span>
            </div>
            {isVersioned && <ul className={"theme-doc-sidebar-menu menu__list"}>
                <VersionDropdown docsPluginId={docConfig.id}
                                 mobile={true}
                                 dropdownItemsBefore={[]}
                                 dropdownItemsAfter={[]}
                                 items={[]}/>
            </ul>}
            <div className={styles.mobileDivider}>

            </div>
        </>
    );
}

const SidebarHeader = ({docId, mobile}: { docId: string | undefined, mobile: boolean }) => {
    const {siteConfig} = useDocusaurusContext();
    const docConfig: ProductItem | undefined = (siteConfig.customFields.products as ProductItem[]).find(value => value.id === docId);
    return (
        docConfig ? (
            mobile ? <MobileHeader docConfig={docConfig}/> : <DesktopHeader docConfig={docConfig}/>
        ) : <></>
    );
};

export default SidebarHeader;