import React from 'react';
import styles from './styles.module.css';
import SearchIcon from "./search.svg";

const Search = () => {

    const onInputFocus = (e: any) => {
        (document.querySelector('.DocSearch') as HTMLElement).click();
    }

    return (
        <section className={styles.container}>
            <div className={styles.searchContainer}>
                <SearchIcon />
                <input className={styles.searchInput} placeholder={"Search"} onFocus={onInputFocus}/>
            </div>
        </section>
    );
};

export default Search;