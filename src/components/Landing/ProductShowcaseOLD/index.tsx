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
    links: { label: string, to: string }[];
};

interface Props {
    products: ProductItem[];
}

const Product = ({label, Image, to, color, links}: ProductItem) => {

    const [expanded, setExpanded] = useState<boolean>(false);

    const onExpand = (event: React.MouseEvent) => {
        event.preventDefault();
        event.stopPropagation();
        setExpanded(prevState => !prevState);
    }

    return (
        <div className={styles.productContainer}>
            <Link className={styles.product} to={to}>
                {typeof Image === "string" ?
                    <img src={Image} alt={label} className={styles.productImg}/> :
                    <Image className={styles.productImg} role="img"/>}
                <div className={styles.productLabel}>
                    {label}
                </div>
                <div className={styles.productExpand} onClick={onExpand}>
                    <span className={styles.productExpandIcon}/>
                </div>
            </Link>
            {links.length > 0 && <div className={clsx(styles.collapse, expanded && styles.expanded)}>
                <ul className={styles.usefulLinks}>
                    {links.map(link => <li className={styles.usefulLink} key={link.label}>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
                             fill={"currentColor"}>
                            <path d="m375-240-43-43 198-198-198-198 43-43 241 241-241 241Z"/>
                        </svg>
                        <Link to={link.to}>{link.label}</Link>
                    </li>)}
                </ul>
            </div>}
        </div>
    );
}
const ProductShowcase = ({products}: Props) => {

    return (
        <section className={styles.container}>
            <div className={styles.innerContainer}>
                {products.map(value => <Product key={value.id} {...value} />)}
            </div>
        </section>
    );
};

export default ProductShowcase;