import React from 'react';
import clsx from 'clsx';
import {
    NavbarSecondaryMenuFiller,
    ThemeClassNames,
} from '@docusaurus/theme-common';
import {useNavbarMobileSidebar} from '@docusaurus/theme-common/internal';
import DocSidebarItems from '@theme/DocSidebarItems';
import SidebarHeader from "@site/src/components/SidebarHeader";
import {getDocId} from "@site/src/theme/DocSidebar/Desktop";
// eslint-disable-next-line react/function-component-definition
const DocSidebarMobileSecondaryMenu = ({sidebar, path}) => {
    const mobileSidebar = useNavbarMobileSidebar();
    const docId = getDocId(path);
    return (
        <>
            <SidebarHeader docId={docId} mobile={true} />
            <ul className={clsx(ThemeClassNames.docs.docSidebarMenu, 'menu__list')}>
                <DocSidebarItems
                    items={sidebar}
                    activePath={path}
                    onItemClick={(item) => {
                        // Mobile sidebar should only be closed if the category has a link
                        if (item.type === 'category' && item.href) {
                            mobileSidebar.toggle();
                        }
                        if (item.type === 'link') {
                            mobileSidebar.toggle();
                        }
                    }}
                    level={1}
                />
            </ul>
        </>
    );
};

function DocSidebarMobile(props) {
    return (
        <NavbarSecondaryMenuFiller
            component={DocSidebarMobileSecondaryMenu}
            props={props}
        />
    );
}

export default React.memo(DocSidebarMobile);
