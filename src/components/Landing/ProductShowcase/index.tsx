import React, {useState} from 'react';
import styles from './styles.module.css';
import clsx from "clsx";
import Link from "@docusaurus/Link";

export type ProductItem = {
    id: string;
    label: string;
    description: string;
    color: string;
    icon: string;
    Image: string | React.ComponentType<React.ComponentProps<'svg'>>;
    to: string;
    banner?: "news" | "updated";
};

interface Props {
    products: ProductItem[];
}

const Product = ({label, Image, to, color}: ProductItem) => {

    return (
        <div className={clsx('col col--12', styles.product)}>
            <div className="text--center">
                <Link to={to}>
                    {typeof Image === "string" ?
                        <img src={Image} alt={label} className={styles.productImg}/> :
                        <Image className={styles.productImg} role="img"/>}
                </Link>
            </div>
            <div className={clsx("text--center padding-horiz--md", styles.productLabel)}
                 style={{color: `var(--${color})`}}>
                <Link to={to} className={styles.link}>
                    {label}
                </Link>
            </div>
        </div>
    );
}
const ProductShowcase = ({products}: Props) => {

    return (
        <section className={styles.productShowcase}>
            <div className="container">
                <div className="row">
                    {products.map(value => <Product key={value.id} {...value} />)}
                </div>
            </div>
        </section>
    );
};

export default ProductShowcase;