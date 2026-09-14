import React from "react";

export default ({children, num, color = "#8B0000", disableMargin = false}: {children?: React.ReactNode, num?: number, disableMargin?: boolean, color?: string}) => (
    <span
        style={{
            backgroundColor: color,
            borderRadius: "50%",
            color: "#fff",
            height: "1em",
            aspectRatio: "1 / 1",
            textAlign: "center",
            display: "inline-block",
            marginRight: disableMargin ? "0px" : "4px",
            lineHeight: 1
        }}
    >
        {children ?? num}
    </span>
);