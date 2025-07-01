import React from 'react';
import Alert from "@site/src/components/Landing/Alert";
import alertConfig from "../../alert";
import {FocusProvider} from "@site/src/components/useFocus";

export default function Root({children}) {
    return <FocusProvider>
        {alertConfig.timestamp && <Alert {...alertConfig} />}
        {children}
    </FocusProvider>;
}