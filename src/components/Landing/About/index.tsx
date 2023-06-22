import React from 'react';
import styles from './styles.module.css';
import useAboutText from "@site/src/components/Landing/About/useAboutText";
import clsx from "clsx";

const About = () => {

    const {text, onSelectedTextChange, selectedText} = useAboutText();

    return (
        <section className={styles.aboutContainer}>
            <div className={styles.innerContainer}>
                <div className={styles.contentContainer}>
                    <h2>{text.title}</h2>
                    {text.text}
                </div>
                <div className={styles.summitContainer}>
                    <img src={"/img/landing/summit.png"} className={styles.summitImage}/>
                    <svg width={"100%"} height={"100%"} className={styles.summitOverlay} viewBox={"0 0 900 840"}>
                        <g>
                            {/* oben-xy links-xy rechts-xy */}
                            <polygon points="165,130 235,130 200,190"
                                     className={clsx(styles.triangle, selectedText === 0 && styles.triangleActive)}
                                     onClick={() => onSelectedTextChange(0)}/>
                            <polygon points="330,40 400,40 365,100"
                                     className={clsx(styles.triangle, selectedText === 1 && styles.triangleActive)}
                                     onClick={() => onSelectedTextChange(1)}/>
                            <polygon points="565,80 635,80 600,140"
                                     className={clsx(styles.triangle, selectedText === 2 && styles.triangleActive)}
                                     onClick={() => onSelectedTextChange(2)}/>
                        </g>
                    </svg>
                </div>
            </div>
        </section>
    );
};

export default About;