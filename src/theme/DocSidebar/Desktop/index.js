import React from 'react';
import clsx from 'clsx';
import {useThemeConfig} from '@docusaurus/theme-common';
import Logo from '@theme/Logo';
import CollapseButton from '@theme/DocSidebar/Desktop/CollapseButton';
import Content from '@theme/DocSidebar/Desktop/Content';
import styles from './styles.module.css';
import SidebarHeader from "@site/src/components/SidebarHeader";

export const getDocId = (path) => {
    const pathMatches = path.match(/^\/([a-z-]+)\//);
    if (!pathMatches || !pathMatches[1]) {
        return undefined;
    }
    return pathMatches[1];
}

function DocSidebarDesktop({path, sidebar, onCollapse, isHidden}) {
    const {
        navbar: {hideOnScroll},
        docs: {
            sidebar: {hideable},
        },
    } = useThemeConfig();
    const docId = getDocId(path);
    return (
        <div
            className={clsx(
                styles.sidebar,
                hideOnScroll && styles.sidebarWithHideableNavbar,
                isHidden && styles.sidebarHidden,
            )}>
            {hideOnScroll && <Logo tabIndex={-1} className={styles.sidebarLogo}/>}
            <SidebarHeader docId={docId} mobile={false}/>
            <Content path={path} sidebar={sidebar}/>
            {hideable && <CollapseButton onClick={onCollapse}/>}
        </div>
    );
}

export default React.memo(DocSidebarDesktop);
