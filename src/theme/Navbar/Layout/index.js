import React from 'react';
import clsx from 'clsx';
import {ThemeClassNames, useThemeConfig} from '@docusaurus/theme-common';
import {
    useHideableNavbar,
    useNavbarMobileSidebar,
} from '@docusaurus/theme-common/internal';
import {translate} from '@docusaurus/Translate';
import NavbarMobileSidebar from '@theme/Navbar/MobileSidebar';
import styles from './styles.module.css';
import useFocus from "@site/src/components/useFocus";

function NavbarBackdrop(props) {
    return (
        <div
            role="presentation"
            {...props}
            className={clsx('navbar-sidebar__backdrop', props.className)}
        />
    );
}

const NavbarLayout = ({children}) => {
    const {
        navbar: {hideOnScroll, style},
    } = useThemeConfig();
    const mobileSidebar = useNavbarMobileSidebar();
    const {navbarRef, isNavbarVisible} = useHideableNavbar(hideOnScroll);
    return (
        <nav
            ref={navbarRef}
            aria-label={translate({
                id: 'theme.NavBar.navAriaLabel',
                message: 'Main',
                description: 'The ARIA label for the main navigation',
            })}
            className={clsx(
                ThemeClassNames.layout.navbar.container,
                'navbar',
                'navbar--fixed-top',
                hideOnScroll && [
                    styles.navbarHideable,
                    !isNavbarVisible && styles.navbarHidden,
                ],
                {
                    'navbar--dark': style === 'dark',
                    'navbar--primary': style === 'primary',
                    'navbar-sidebar--show': mobileSidebar.shown,
                },
            )}>
            {children}
            <NavbarBackdrop onClick={mobileSidebar.toggle}/>
            <NavbarMobileSidebar/>
        </nav>
    )
}

export default function NavbarLayoutWrapper({children}) {
    const focus = useFocus();
    return <>
        {!focus ? <NavbarLayout>{children}</NavbarLayout> : <nav className={"navbar"} style={{display: "none"}}></nav>}
    </>
}
