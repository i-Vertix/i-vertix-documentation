import React, {useMemo, useState} from "react";

type Position = "left" | "center" | "right";
export type News = {
    title: string;
    image: string;
    text: JSX.Element;
    buttonLabel?: string;
    buttonLink?: string;
    style?: any;
    position?: Position;
};


const useNewsCarousel = () => {

    const [selectedIndex, setSelectedIndex] = useState<number>(0);

    const news = useMemo((): News[] => [
        {
            title: "22.10 on the way",
            image: "/img/landing/news/news_1.png",
            text: <p>
                We are finalizing our latest work to release a new major update of the i-Vertix monitoring.
                You can expect new features, new functionalities and improvements, always suited for your needs.
                During the next few months we will get in touch with you and roll-out the update on your systems.
                As always: if you have any questions or find something missing, something broken or something which
                could be improved, feel
                free to contact us via <a href={"mailto:support@i-vertix.com"}>Email</a>.
            </p>,
        },
        {
            title: "Monitoring - Integrated Documentation",
            image: "/img/landing/news/news_2.png",
            text: <p>
                With our new monitoring version we introduced the functionality to access the documentation' search
                directly from the monitoring web interface!<br/>
                On the left screen-corner you will find the i-Vertix icon which opens up a list of various helpful
                links, including the documentation search.
            </p>
        },
        {
            title: "Stay up to date",
            image: "/img/landing/news/news_3.png",
            text: <p>
                Don't want to miss any new features or news from i-Vertix?
                We got you covered! Simply subscribe to our newsletter which we publish every month to not miss a thing.
                If you'd like to further stay in touch with us you can follow us on <a
                href={"https://www.linkedin.com/company/i-vertix/"} target={"_blank"}
                rel={"noopener"}>LinkedIn</a>!
            </p>,
            buttonLabel: "Subscribe",
            buttonLink: "https://eepurl.com/gW63E1",
        },
    ], []);

    const additionalProps = useMemo(() => {
        const styles: any = [];
        const positions: (Position | undefined)[] = [];
        const leftIndex = selectedIndex - 1 < 0 ? news.length - 1 : selectedIndex - 1;
        const rightIndex = selectedIndex + 1 > news.length - 1 ? 0 : selectedIndex + 1;
        for (let i = 0; i < news.length; i++) {
            if (i === selectedIndex) {
                styles.push({
                    transform: "translateX(0px) scale(1)",
                    opacity: 1,
                    zIndex: 2,
                    cursor: "auto"
                });
                positions.push("center");
            } else if (i === leftIndex) {
                styles.push({
                    transform: `translateX(-220px) scale(0.85)`,
                    opacity: 1,
                    zIndex: 1,
                    cursor: "pointer"
                });
                positions.push("left");
            } else if (i === rightIndex) {
                styles.push({
                    transform: `translateX(220px) scale(0.85)`,
                    opacity: 1,
                    zIndex: 0,
                    cursor: "pointer"
                });
                positions.push("right");
            } else {
                styles.push({
                    transform: `translate(0px) scale(0)`,
                    opacity: 0,
                    zIndex: 0,
                    cursor: "none"
                });
                positions.push(undefined);
            }
        }
        return {styles, positions};
    }, [news.length, selectedIndex]);

    const _news = useMemo((): News[] =>
            news.map((n, i) => ({...n, style: additionalProps.styles[i], position: additionalProps.positions[i]})),
        [news, additionalProps, selectedIndex]);

    return {
        news: _news,
        setSelectedNews: setSelectedIndex
    };
}

export default useNewsCarousel;