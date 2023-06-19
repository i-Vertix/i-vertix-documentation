import React, {useMemo, useState} from "react";

export type News = {
    title: string;
    image: string;
    text: JSX.Element;
    buttonLabel?: string;
    buttonLink?: string;
    style?: any;
    active?: boolean;
};


const useNewsCarousel = () => {

    const [selectedIndex, setSelectedIndex] = useState<number>(0);

    const news = useMemo((): News[] => [
        {
            title: "OS Discovery Released",
            image: "/img/alerts/os-discovery.png",
            text: <p>
                In June we released our brand new OS-Discovery functionality for our monitoring solution.
                Discovery you will be able to monitor your virtualized servers in seconds!
            </p>,
            buttonLabel: "Take me to the docs",
            buttonLink: "/monitoring/monitoring-resources/discovery/vmware-discovery",
        },
        {
            title: "New Monitoring version is on the way",
            image: "/img/alerts/os-discovery.png",
            text: <p>
                At the moment we are finalizing and testing our recent work.<br/>
                By the end of june we will release a brand new monitoring version!<br/>
                Don't miss any upcoming features and improvements
                by subscribing to our Newsletter!

                <strong>Stay tuned boys!</strong>
            </p>,
            buttonLabel: "Subscribe",
            buttonLink: "https://i-vertix.com",
        },
        {
            title: "New docs are in the making",
            image: "/img/alerts/os-discovery.png",
            text: <p>
                As you maybe have already noticed, Log & Data Management and Asset Management docs aren't yet available
                on our documentation.<br/>
                We are hardly working to provide some fresh, useful docs for you as soon as possible.<br/>
                In the meantime, <strong>live long and prosper</strong>.
            </p>,
            buttonLabel: "Subscribe",
            buttonLink: "https://i-vertix.com",
        },
    ], []);

    const newsStyles = useMemo(() => {
        const styles: any = [];
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
            } else if (i === leftIndex) {
                styles.push({
                    transform: `translateX(-220px) scale(0.85)`,
                    opacity: 1,
                    zIndex: 1,
                    cursor: "pointer"
                });
            } else if (i === rightIndex) {
                styles.push({
                    transform: `translateX(220px) scale(0.85)`,
                    opacity: 1,
                    zIndex: 0,
                    cursor: "pointer"
                });
            } else {
                styles.push({
                    transform: `translate(0px) scale(0)`,
                    opacity: 0,
                    zIndex: 0,
                    cursor: "none"
                });
            }
        }
        return styles;
    }, [news.length, selectedIndex]);

    const _news = useMemo((): News[] =>
            news.map((n, i) => ({...n, style: newsStyles[i], active: selectedIndex === i})),
        [news, newsStyles, selectedIndex]);

    return {
        news: _news,
        setSelectedNews: setSelectedIndex
    };
}

export default useNewsCarousel;