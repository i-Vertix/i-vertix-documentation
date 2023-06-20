import React from 'react';
import clsx from 'clsx';

export default function FooterLayout({style, links, logo, copyright}) {
    return (
        <footer
            className={clsx('footer', {
                'footer--dark': style === 'dark',
            })}>
            <div className="container container-fluid">
                <div className="footer__container">
                    <div className={"footer__logo-custom"}>
                        <a href={"/"} title={"i-Vertix Documentation"}>
                            <img src={"/img/logo-ivertix-100.png"} width={100} height={100} alt={"i-Vertix"}/>
                        </a>
                    </div>
                    {links}
                </div>
                {(logo || copyright) && (
                    <div className="footer__bottom text--center">
                        {/*{logo && <div className="margin-bottom--sm">{logo}</div>}*/}
                        {copyright}
                    </div>
                )}
            </div>
        </footer>
    );
}
