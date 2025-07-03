import React from 'react';
import Sidebar from '@theme-original/DocRoot/Layout/Sidebar';
import useFocus from "@site/src/components/useFocus";

export default function SidebarWrapper(props) {
    const focus = useFocus();
    return (
        <>
            {!focus && <Sidebar {...props} />}
        </>
    );
}
