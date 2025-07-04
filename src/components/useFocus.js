import React, {useEffect, useMemo} from 'react';

const getFocus = () => {
    return useMemo(() => {
        const queryString = typeof window !== "undefined" ? window.location.search : "";
        const params = new URLSearchParams(queryString);
        return params.get("focus") === "true";
    }, []);
};

export const FocusProvider = ({children}) => {
    const focus = getFocus();
    useEffect(() => {
        if (focus && window) {
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.delete("focus");
            window.history.replaceState({}, '', currentUrl.href);
        }
    }, []);
    return <FocusContext.Provider value={focus}>{children}</FocusContext.Provider>;
};

export const FocusContext = React.createContext(false);

const useFocus = () => {
    return React.useContext(FocusContext);
}

export default useFocus;