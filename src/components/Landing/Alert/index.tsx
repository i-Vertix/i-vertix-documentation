import React, {useEffect, useMemo, useRef, useState} from 'react';
import styles from './styles.module.css';
import clsx from "clsx";

export type Alert = {
    timestamp: number;
    title: string;
    size: "small" | "medium";
    description: string[];
    image?: string;
    link?: {
        label: string;
        to: string;
    };
}

const Alert = ({...alert}: Alert) => {
    const ref = useRef<HTMLDivElement | undefined>(undefined);
    const [closed, setClosed] = useState<boolean>(false);
    const show = useMemo(() => {
        const lastAlert: string | null = localStorage.getItem("ivertix-docs-alert");
        return !closed && (lastAlert === null || parseInt(lastAlert) < alert.timestamp);
    }, [closed, alert.timestamp]);
    const onClose = () => {
        setClosed(true);
        localStorage.setItem("ivertix-docs-alert", `${(new Date()).getTime()}`);
    }
    useEffect(() => {
        let onClickOutside: (event: any) => void | undefined = undefined;
        if (show && ref.current) {
            onClickOutside = (event) => {
                if (!ref.current.contains(event.target)) {
                    setClosed(true);
                    localStorage.setItem("ivertix-docs-alert", `${(new Date()).getTime()}`);
                }
            }
            document.addEventListener("mousedown", onClickOutside);
        }
        return () => {
            if (onClickOutside !== undefined) {
                document.removeEventListener("mousedown", onClickOutside);
            }
        }
    }, [ref, show]);

    return (
        show ? (
            <div className={styles.backdrop}>
                <div className={clsx("card", styles.card, alert.size === "small" ? styles.small : styles.medium)} ref={ref}>
                    {alert.image && <div className="card__image">
                        <img
                            src={alert.image}
                            alt=""/>
                    </div>}
                    <div className={styles.close} onClick={onClose}>
                        <svg
                            className={styles.closeIcon}
                            xmlns="http://www.w3.org/2000/svg" height="100%" viewBox="0 0 24 24" width="100%"
                            fill="currentColor">
                            <path d="M0 0h24v24H0z" fill="none"/>
                            <path
                                d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                        </svg>
                    </div>
                    <div className={clsx("card__body", styles.body)}>
                        <h4>{alert.title}</h4>
                        {alert.description.length > 0 && <small>
                            {alert.description.map((v, i) => <React.Fragment key={i}>
                                {v}
                                {i !== alert.description.length - 1 && <br />}
                            </React.Fragment>)}
                        </small>}
                    </div>
                    {alert.link && <div className="card__footer">
                        <a className="button button--primary button--block" href={alert.link.to}>
                            {alert.link.label}
                        </a>
                    </div>}
                </div>
            </div>
        ) : <></>
    );
};

export default React.memo(Alert);