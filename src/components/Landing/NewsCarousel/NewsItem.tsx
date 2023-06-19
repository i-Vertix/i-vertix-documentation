import React from 'react';
import styles from './styles.module.css';

interface Props {
    image: string;
    title: string;
    content: string;
    button?: {
        text: string;
        link: string;
    };
}

const NewsItem = ({button, content, image, title}: Props) => {


    return (
        <div className={`${styles.newsItem}`}>
            <img className={styles.newsImage} src={image} alt={title}/>
            <div className={styles.newsContent}>
                <h2 className={styles.newsTitle}>{title}</h2>
                <p className={styles.newsText}>
                    {content}
                </p>
                {button &&
                    <div className={styles.newsActions}>
                        <a href={button.link} className={styles.newsButton}>
                            {button.text}
                        </a>
                    </div>}
            </div>
        </div>
    );
};

export default NewsItem;