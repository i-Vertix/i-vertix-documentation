import React from 'react';
import styles from './styles.module.css';
import clsx from "clsx";
import Link from "@docusaurus/Link";

export type ProductItem = {
    id: string;
    label: string;
    description: string;
    icon: string;
    Image: string | React.ComponentType<React.ComponentProps<'svg'>>;
    to: string;
    banner?: "news" | "updated";
};

interface Props {
    products: ProductItem[];
}

const Product = ({label, description, Image, to, banner}: ProductItem) => {

    return (
        <Link className={clsx('col col--4', styles.product)} to={to}>
            {banner && <span className={styles.banner}>{banner}</span>}
            <div className="text--center">
                {typeof Image === "string" ?
                    <img src={Image} alt={label} className={styles.productImg}/> :
                    <Image className={styles.productImg} role="img"/>}
            </div>
            <div className={clsx("text--center padding-horiz--md", styles.productLabel)}>
                <div className="button button--secondary button--lg">
                    {label}
                </div>
            </div>
        </Link>
    );
}
const ProductShowcase = ({products}: Props) => {

    return (
        <section className={styles.productShowcase}>
            <div className="container">
                <div className="row">
                    {products.map(value => <Product {...value} />)}
                </div>
            </div>
        </section>
    );
};

export default ProductShowcase;