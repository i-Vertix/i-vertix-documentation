import {useLayoutEffect, useRef} from "react";
import ApiDocMdx from "@theme/ApiDocMdx";

const IVertixApiDoc = ({id, spec}:{id?: any, spec?: any}) => {

    const ref = useRef<HTMLDivElement | null>(null);

    useLayoutEffect(() => {
        if (ref.current) {
            const els = ref.current.getElementsByClassName("menu-content");
            if (els.length === 0) return;
            // const y = els[0].getBoundingClientRect().y;
            els[0].style.top = "var(--ifm-navbar-height)";
        }
    }, []);

    return <div ref={ref}>
        <ApiDocMdx id={id} spec={spec} />
    </div>
}

export default IVertixApiDoc;