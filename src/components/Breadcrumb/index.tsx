import React from "react";

const Arrow = () => (
    <svg
        style={{ fill: "currentcolor", width: "1em", height: "1em", display: "inline-block", fontSize: "inherit", userSelect: "none" }}
        focusable="false"
        aria-hidden="true"
        viewBox="0 0 24 24"
    >
        <path d="M10 6 8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path>
    </svg>
);

export default ({ crumbs, disableMargin = false, size = "small" }: { children?: never, crumbs: string[], disableMargin?: boolean, size?: "small" | "medium" }) => (
    <div style={{
        display: "inline-flex",
        gap: "1px",
        padding: "2px 6px",
        marginRight: disableMargin ? "0px" : "4px",
        border: "1px solid",
        borderRadius: "10px",
        borderColor: "var(--ifm-font-color-base)",
        fontSize: size === "small" ? "0.875rem" : "1rem"
    }}>
        {crumbs.map((value, index, arr) => <>
            <span
                key={value}
                style={{
                    display: "inline-block",
                    lineHeight: 1
                }}
            >
                {value}
            </span>
            {index < arr.length -1 && <Arrow key={`a-${value}`} />}
        </>
        )}
    </div>
);