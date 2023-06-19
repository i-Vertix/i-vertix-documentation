import React from 'react';
import styles from './styles.module.css';
import {News} from "@site/src/components/Landing/NewsCarousel/useNewsCarousel";
import clsx from "clsx";

const NewsItem = (props: News & { onClick: () => void }) => {

    return (
        <div className={styles.newsItemContainer} style={props.style} onClick={props.onClick}>
            <div className={clsx(styles.newsItem, props.active && styles.newsItemActive)}>
                <img className={styles.newsImage} src={props.image} alt={props.title}/>
                <div className={styles.newsContentContainer}>
                    <h2 className={styles.newsTitle}>{props.title}</h2>
                    <div className={styles.newsContent}>
                        {props.text}
                    </div>
                    {props.buttonLink !== undefined && (
                        <div className={styles.newsActions}>
                            <a href={props.buttonLink} className={styles.newsButton}>
                                {props.buttonLabel ?? "Read more"}
                            </a>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default NewsItem;