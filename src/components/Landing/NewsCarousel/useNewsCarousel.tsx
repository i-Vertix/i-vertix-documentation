import React, { useMemo, useState } from "react";

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
            title: "NEW Cloud Discovoery",
            image: "/img/landing/news/cloud-discovery.png",
            text: <p>
                We're excited to introduce the latest update of our i-Vertix Discovery module, now including the new discovery type: Cloud discovery.
                <br />
                This new functionality enables the discovery for a lot of cloud technologies, such as AWS, Azure, VMware VeloCloud, ExtremeCloud IQ, Cisco Webex and more.
            </p>,
            buttonLabel: "Read more",
            buttonLink: "./monitoring/monitoring-resources/discovery/common-discovery",
        },
        {
            title: "NEW i-Vertix Monitoring 4.3",
            image: "/img/landing/news/new-release.jpg",
            text: <p>
                Check out the new features and functionalities of our new i-Vertix Monitoring version 4.3.
                <br />
                Brand new Dashboards, Widgets and improvements are waiting for you to discover!
            </p>,
            buttonLabel: "Blog",
            buttonLink: "https://i-vertix.com/en/i-vertix-it-monitoring-4-3/",
        },
        {
            title: "NEW i-Vertix Monitoring Troubleshooter",
            image: "/img/landing/news/troubleshooter.jpg",
            text: <p>
                Mid-October we introduced a great new addition to i-Vertix Monitoring — the Monitoring Troubleshooter.
                It helps you test connectivity, run SNMP walks, and analyze routing or DNS issues directly within your monitoring interface.
            </p>,
            buttonLabel: "Read more",
            buttonLink: "https://i-vertix.com/en/i-vertix-it-monitoring-4-3/",
        },
        {
            title: "Stay up to date",
            image: "/img/landing/news/newsletter.jpg",
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
        return { styles, positions };
    }, [news.length, selectedIndex]);

    const _news = useMemo((): News[] =>
        news.map((n, i) => ({ ...n, style: additionalProps.styles[i], position: additionalProps.positions[i] })),
        [news, additionalProps, selectedIndex]);

    return {
        news: _news,
        setSelectedNews: (index: number) => {
            setSelectedIndex(index)
        },
        currentNewsIndex: selectedIndex 
    };
}

export default useNewsCarousel;