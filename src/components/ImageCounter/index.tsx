import React from "react";

export default ({children, num}: {children?: React.ReactNode, num?: number}) => (
    <span
        style={{
            backgroundColor: "#8B0000",
            borderRadius: "50%",
            color: "#fff",
            height: "1em",
            aspectRatio: "1 / 1",
            textAlign: "center",
            display: "inline-block",
            marginRight: "4px",
            lineHeight: 1
        }}
    >
        {children ?? num}
    </span>
);