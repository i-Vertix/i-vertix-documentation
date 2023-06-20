import clsx from "clsx";
import styles from "@site/src/components/Landing/Header/styles.module.css";
import React from "react";

const Header = () => {
    return (
        <header className={clsx('hero hero--primary', styles.heroBanner)}>
            <div className={styles.heroTitleContainer}>
                <img src={"/img/landing/logo-ivertix-text.png"} alt={"i-Vertix"} className={styles.heroLogo}/>
                <div className={styles.heroTitle}>Documentation</div>
            </div>
        </header>
    );
}

export default Header;