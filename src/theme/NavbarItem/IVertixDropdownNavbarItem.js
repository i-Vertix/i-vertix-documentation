import React, {useState, useRef, useEffect} from 'react';
import clsx from 'clsx';
import {
    useCollapsible,
    Collapsible,
} from '@docusaurus/theme-common';
import {useDocsVersionCandidates, useLocalPathname} from '@docusaurus/theme-common/internal';
import NavbarNavLink from '@theme/NavbarItem/NavbarNavLink';
import NavbarItem from '@theme/NavbarItem';
import Link from "@docusaurus/Link";

const isDocumentationActive = (currentPath, docsMainPath) => {
    const pathMatches = docsMainPath.match(/\/[a-z-]+\//);
    if (!pathMatches[0]) {
        return false;
    }
    const regexpString = `^${pathMatches[0].slice(0, -1)}\/`;
    return !!currentPath.match(new RegExp(regexpString));
}

const getRegexForDocumentationActive = (currentPath, docsMainPath) => {
    const pathMatches = docsMainPath.match(/\/[a-z-]+\//);
    if (!pathMatches[0]) {
        return false;
    }
    return`^${pathMatches[0].slice(0, -1)}\/`;
}

const getVersionMainDoc = (version) =>
    version.docs.find((doc) => doc.id === version.mainDocId);

function DropdownNavbarItemDesktop({
                                       items,
                                       position,
                                       className,
                                       onClick,
                                       ...props
                                   }) {
    const localPathname = useLocalPathname();
    const dropdownRef = useRef(null);
    const [showDropdown, setShowDropdown] = useState(false);

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (!dropdownRef.current || dropdownRef.current.contains(event.target)) {
                return;
            }
            setShowDropdown(false);
        };
        document.addEventListener('mousedown', handleClickOutside);
        document.addEventListener('touchstart', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
            document.removeEventListener('touchstart', handleClickOutside);
        };
    }, [dropdownRef]);
    return (
        <div
            ref={dropdownRef}
            className={clsx('navbar__item', 'dropdown', 'ivertix__dropdown', 'dropdown--hoverable', {
                'dropdown--right': position === 'right',
                'dropdown--show': showDropdown,
            })}>
            <span
                className={clsx('ivertix__navbar-link', className)}
                onKeyDown={(e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        setShowDropdown(!showDropdown);
                    }
                }}>
                {props.label}
            </span>
            <ul className="dropdown__menu">
                {items.map((itemProps, i) => {
                    const dropdownVersion = useDocsVersionCandidates(itemProps.docsPluginId)[0];
                    const dropdownTo = getVersionMainDoc(dropdownVersion).path;
                    const isActive = isDocumentationActive(localPathname, dropdownTo);

                    return (
                        <Link
                            key={`nav-link-${i}`}
                            to={dropdownTo}
                            className={clsx("ivertix__navbar-link-item", isActive && "ivertix__navbar-link-item-active")}
                        >
                            <div className="ivertix__navbar-link-item-icon">
                                <img alt={itemProps.label} src={itemProps.icon}/>
                            </div>
                            <div className="ivertix__navbar-link-item-content">
                                <span className="ivertix__navbar-link-item-label">
                                    {itemProps.label}
                                </span>
                                <span className="ivertix__navbar-link-item-desc">
                                    {itemProps.description}
                                </span>
                            </div>
                        </Link>
                    )
                })}
            </ul>
        </div>
    );
}

function DropdownNavbarItemMobile({
                                      items,
                                      className,
                                      position, // Need to destructure position from props so that it doesn't get passed on.
                                      onClick,
                                      ...props
                                  }) {
    const localPathname = useLocalPathname();
    const {collapsed, toggleCollapsed} = useCollapsible({
        initialState: false
    });

    console.log(props.label);

    return (
        <li
            className={clsx('menu__list-item', {
                'menu__list-item--collapsed': collapsed,
            })}>
            <NavbarNavLink
                label={props.label}
                role="button"
                className={clsx(
                    'menu__link menu__link--sublist menu__link--sublist-caret',
                    className,
                )}
                onClick={(e) => {
                    e.preventDefault();
                    toggleCollapsed();
                }}>
                {props.children ?? props.label}
            </NavbarNavLink>
            <Collapsible lazy as="ul" className="menu__list" collapsed={collapsed}>
                {items.map((itemProps, i) => {
                    const dropdownVersion = useDocsVersionCandidates(itemProps.docsPluginId)[0];
                    const dropdownTo = getVersionMainDoc(dropdownVersion).path;
                    const regex = getRegexForDocumentationActive(localPathname, dropdownTo);
                    return (
                        <NavbarItem
                            type={"default"}
                            label={itemProps.label}
                            activeBaseRegex={regex}
                            to={dropdownTo}
                            mobile
                            isDropdownItem
                            onClick={onClick}
                            activeClassName="menu__link--active"
                            key={i}
                        />
                    )
                })}
            </Collapsible>
        </li>
    );
}

export default function IVertixDropdownNavbarItem({mobile = false, ...props}) {
    const Comp = mobile ? DropdownNavbarItemMobile : DropdownNavbarItemDesktop;
    return <Comp {...props} />;
}
