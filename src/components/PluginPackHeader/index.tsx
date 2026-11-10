import React from "react";
import styles from "./styles.module.css";

type Props = {
    name: string;
    image: string;
    category?: string;
    metadata?: string[];
};

/**
 * Header of a plugin pack page: plugin pack image and name, followed by category and metadata badges.
 * Use it with `hide_title: true` in the front matter, since it renders the page <h1>.
 */
export default function PluginPackHeader({name, image, category, metadata = []}: Props) {
    return (
        <header className={styles.header}>
            <img className={styles.image} src={image} alt={name} width={80} height={80}/>
            <div>
                <h1 className={styles.title}>{name}</h1>
                <div className={styles.badges}>
                    {category && <span className="badge badge--primary">{category}</span>}
                    {metadata.map((m) => (
                        <span key={m} className="badge badge--secondary">{m}</span>
                    ))}
                </div>
            </div>
        </header>
    );
}
