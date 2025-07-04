import React from "react";

const Icon = ({ children, color, backgroundColor, height, width, spaceLeft, spaceRight }:
    { children: React.ReactNode, color: string, backgroundColor: string, height: number, width: number, spaceLeft: boolean, spaceRight: boolean }) => (
    <span style={{
        display: "inline-block",
        padding: 2,
        backgroundColor: backgroundColor,
        borderRadius: "50%",
        boxSizing: "content-box",
        color: color,
        verticalAlign: "middle",
        height: height,
        width: width,
        marginLeft: spaceLeft ? "4px" : "0",
        marginRight: spaceRight ? "4px" : "0"
    }}>
        {children}
    </span>
);

export default Icon;