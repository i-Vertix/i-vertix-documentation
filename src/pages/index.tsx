import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import ProductShowcase, {ProductItem} from '@site/src/components/Landing/ProductShowcase';
import NewsCarousel from "@site/src/components/Landing/NewsCarousel";
import About from "@site/src/components/Landing/About";
import Header from "@site/src/components/Landing/Header";

export default function Home(): JSX.Element {
    const {siteConfig} = useDocusaurusContext();
    return (
        <Layout
            title={`Get started with i-Vertix`}
            description="Description will go into a meta tag in <head />">
            <Header/>
            <main>
                <ProductShowcase products={siteConfig.customFields.products as ProductItem[]}/>
            </main>
            <NewsCarousel/>
            <About/>
        </Layout>
    );
}
