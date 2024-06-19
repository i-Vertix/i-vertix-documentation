import React from "react";

export default ({children}: {children: React.ReactNode}) => (
    <span
        style={{
            backgroundColor: "#8B0000",
            borderRadius: "50%",
            color: "#fff",
            minWidth: "18px",
            minHeight: "18px",
            textAlign: "center",
            display: "inline-block",
            marginRight: "4px",
            lineHeight: 1
        }}
    >
        {children}
    </span>
);