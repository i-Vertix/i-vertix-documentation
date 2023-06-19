import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import ProductShowcase, {ProductItem} from '@site/src/components/Landing/ProductShowcase';
import styles from './index.module.css';
import NewsCarousel from "@site/src/components/Landing/NewsCarousel";
import About from "@site/src/components/Landing/About";

function HomepageHeader() {
    const {siteConfig} = useDocusaurusContext();
    return (
        <header className={clsx('hero hero--primary', styles.heroBanner)}>
        </header>
    );
}

export default function Home(): JSX.Element {
    const {siteConfig} = useDocusaurusContext();
    return (
        <Layout
            title={`Get started with i-Vertix`}
            description="Description will go into a meta tag in <head />">
            <HomepageHeader/>
            <main>
                <ProductShowcase products={siteConfig.customFields.products as ProductItem[]}/>
            </main>
            <NewsCarousel />
            <About />
        </Layout>
    );
}
