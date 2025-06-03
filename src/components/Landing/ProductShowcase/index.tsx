import React from 'react';
import styles from "@site/src/components/Landing/ProductShowcase/styles.module.css";
import Link from "@docusaurus/Link";


export type ProductItem = {
    id: string;
    label: string;
    description: string;
    color: string;
    icon: string;
    Image: string | React.ComponentType<React.ComponentProps<'svg'>>;
    to: string;
    links: { label: string, to: string }[];
};

interface Props {
    products: ProductItem[];
}

const Product = ({label, Image, to, description}: ProductItem) => {

    return (
        <Link className={styles.card} to={to}>
            <div className={styles.card__section}>
                <div className={styles.card__icon}>
                    {typeof Image === "string" ?
                        <img src={Image} alt={label}/> :
                        <Image role="img"/>}
                </div>
                <h3 className={styles.card__header}>{label}</h3>
                <p className={styles.card__description}>
                    {description}
                </p>
            </div>
        </Link>
    );
}

const ProductShowcase = ({products}: Props) => {

    return (
        <section className={styles.section}>
            <div className={styles.container}>
                <div className={styles.cards}>
                    {products.map(value => <Product key={value.id} {...value} />)}
                </div>
            </div>
        </section>
    );
};

export default ProductShowcase;