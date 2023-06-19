import React, {useState} from 'react';
import styles from './styles.module.css';
import Slider from "react-slick";
import NewsItem from "@site/src/components/Landing/NewsCarousel/NewsItem";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

const NewsCarousel = () => {

    return (
        <section className={styles.carouselContainer}>
            <div>
                <Slider
                    // autoplay
                    // autoplaySpeed={4000}
                    centerMode
                    dots
                    infinite
                    variableWidth
                    centerPadding={"0px"}
                    responsive={[
                        {
                            breakpoint: 720,
                            settings: {
                                infinite: true
                            }
                        }
                    ]}
                >
                    <NewsItem image={"/img/alerts/os-discovery.png"} title={"OS Discovery"}
                              content={"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent scelerisque nisl eu orci mattis molestie. Nam hendrerit sagittis laoreet. Mauris faucibus nunc id dui consequat, vel pellentesque leo porta. Nulla eu elementum leo, quis imperdiet ligula. Praesent sed lectus interdum, iaculis turpis ac, faucibus lacus. Proin vel placerat leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras quis tristique velit, eget varius ex. Morbi fermentum sapien dignissim, pharetra tortor at, laoreet arcu."}
                              button={{link: "https://google.de", text: "Read more"}}/>
                    <NewsItem image={"/img/alerts/os-discovery.png"} title={"OS Discovery"} content={"second content"}
                              button={{link: "https://google.de", text: "Read more"}}/>
                    <NewsItem image={"/img/alerts/os-discovery.png"} title={"OS Discovery"} content={"third content"}
                              button={{link: "https://google.de", text: "Read more"}}/>

                </Slider>
            </div>
        </section>
    );
};

export default NewsCarousel;