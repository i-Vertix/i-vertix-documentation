import React, { useRef } from 'react';
import { useSwipeable } from "react-swipeable";
import styles from './styles.module.css';
import NewsItem from "@site/src/components/Landing/NewsCarousel/NewsItem";
import useNewsCarousel from "@site/src/components/Landing/NewsCarousel/useNewsCarousel";
import clsx from "clsx";

const NewsCarousel = () => {
    const { news, setSelectedNews, currentNewsIndex } = useNewsCarousel();
    const isSwipingRef = useRef(false);
    const handlers = useSwipeable({
        onSwiping: () => {
            isSwipingRef.current = true;
        },
        onSwiped: () => {
            setTimeout(() => {
                isSwipingRef.current = false;
            }, 0);
        },
        onSwipedLeft: (data) => {
            data.event?.preventDefault();
            setSelectedNews((currentNewsIndex + 1) % news.length);
        },
        onSwipedRight: () => {
            setSelectedNews((currentNewsIndex - 1 + news.length) % news.length);
        },
        trackMouse: true,
    });

    return (
        <section className={styles.carouselContainer}>
            <div {...handlers} className={styles.slider}>
                {news.map((n, i) => (
                    <NewsItem
                        {...n}
                        key={`news-${i}`}
                        onClick={() => {
                            if (isSwipingRef.current) return;
                            setSelectedNews(i)
                        }}
                    />
                ))}
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