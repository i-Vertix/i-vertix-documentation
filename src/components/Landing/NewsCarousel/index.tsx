import React, {useState} from 'react';
import styles from './styles.module.css';
import NewsItem from "@site/src/components/Landing/NewsCarousel/NewsItem";
import useNewsCarousel from "@site/src/components/Landing/NewsCarousel/useNewsCarousel";
import clsx from "clsx";

const NewsCarousel = () => {

    const {news, setSelectedNews} = useNewsCarousel();

    return (
        <section className={styles.carouselContainer}>
            <div className={styles.slider}>
                {news.map((n, i) => <NewsItem {...n} key={`news-${i}`} onClick={() => setSelectedNews(i)}/>)}
            </div>
            <div className={styles.bullets}>
                {news.map((_, i) => <div
                    key={`bullet-${i}`}
                    onClick={() => setSelectedNews(i)}
                    className={clsx(styles.bullet, _.position === "center" && styles.bulletActive)}
                >
                </div>)}
            </div>
        </section>
    );
};

export default NewsCarousel;