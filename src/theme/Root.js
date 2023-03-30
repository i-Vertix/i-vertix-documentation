import React from 'react';
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Alert from "@site/src/components/Landing/Alert";
import alertConfig from "../../alert";

export default function Root({children}) {
    const {siteConfig} = useDocusaurusContext();
    return <>
        {alertConfig.timestamp && <Alert {...alertConfig} />}
        {children}
    </>;
}