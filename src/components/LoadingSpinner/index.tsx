import React from 'react';
import styles from './styles.module.css';

export default function LoadingSpinner({children}: {children?: React.ReactNode}) {
    return (
        <div className={styles.container}>
            <div className={styles.spinner}></div>
            {children && <p>{children}</p>}
        </div>
    );
}