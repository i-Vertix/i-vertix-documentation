import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import ProductShowcase, {ProductItem} from '@site/src/components/Landing/ProductShowcase';
import NewsCarousel from "@site/src/components/Landing/NewsCarousel";
import About from "@site/src/components/Landing/About";
import Header from "@site/src/components/Landing/Header";
import Search from "@site/src/components/Landing/Search";
import styles from './styles.module.css';


export default function Home(): JSX.Element {
    const {siteConfig} = useDocusaurusContext();
    return (
        <Layout
            title={`i-Vertix - IT Infrastructure Management`}
            description={"Powerful and scalable solutions to manage your IT Infrastructure"}>
            <Header/>
            <main className={styles.docsContainer}>
                <Search />
                <ProductShowcase products={siteConfig.customFields.products as ProductItem[]}/>
            </main>
            <NewsCarousel/>
            <About/>
        </Layout>
    );
}
