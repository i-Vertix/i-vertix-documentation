import React, {useLayoutEffect, useRef} from "react";
import BrowserOnly from "@docusaurus/BrowserOnly";
import LoadingSpinner from "@site/src/components/LoadingSpinner";

const IVertixApiDoc = ({ id, spec }: { id?: any; spec?: any }) => {
    return (
        <BrowserOnly fallback={<LoadingSpinner>Preparing API Documentation</LoadingSpinner>}>
            {() => {
                const ApiDocInner = () => {
                    const ref = useRef<HTMLDivElement | null>(null);

                    useLayoutEffect(() => {
                        if (ref.current) {
                            const els = ref.current.getElementsByClassName("menu-content");
                            if (els.length === 0) return;
                            (els[0] as HTMLElement).style.top = "var(--ifm-navbar-height)";
                        }
                    }, []);

                    const ApiDocMdx = require("@theme/ApiDocMdx").default;

                    return (
                        <div ref={ref}>
                            <ApiDocMdx id={id} spec={spec} />
                        </div>
                    );
                };

                return <ApiDocInner />;
            }}
        </BrowserOnly>
    );
};

export default IVertixApiDoc;