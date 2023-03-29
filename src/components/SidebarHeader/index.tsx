import React from 'react';
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import VersionDropdown from '@theme/NavbarItem/DocsVersionDropdownNavbarItem';
import styles from './styles.module.css';
import {ProductItem} from "@site/src/components/Landing/ProductShowcase";
import clsx from "clsx";

const DesktopHeader = ({docConfig}: { docConfig: ProductItem }) => {

    return (
        <div className={styles.sidebarHeader}>
            <div className={styles.title}>
                <img src={docConfig.icon} alt={""}/>
                <span>{docConfig.label}</span>
            </div>
            <div className={styles.version}>
                <VersionDropdown docsPluginId={docConfig.id}
                                 dropdownItemsBefore={[]}
                                 dropdownItemsAfter={[]}
                                 items={[]}/>
            </div>
        </div>
    );
}

const MobileHeader = ({docConfig}: { docConfig: ProductItem }) => {
    return (
        <>
            <div className={clsx(styles.title, styles.mobileTitle)}>
                <img src={docConfig.icon} alt={""}/>
                <span>{docConfig.label}</span>
            </div>
            <ul className={"theme-doc-sidebar-menu menu__list"}>
                <VersionDropdown docsPluginId={docConfig.id}
                                 mobile={true}
                                 dropdownItemsBefore={[]}
                                 dropdownItemsAfter={[]}
                                 items={[]}/>
            </ul>
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