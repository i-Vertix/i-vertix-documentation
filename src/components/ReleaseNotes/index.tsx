import React from 'react';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import useReleaseNotes from './useReleaseNotes';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Details from "@theme/Details";

interface Props {
    docId: string; // z. B. "monitoring"
    version: string; // z. B. "24.10"
}

function formatDate(timestamp: number) {
    const date = new Date(timestamp);
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    };
    return date.toLocaleDateString('en-US', options);
}

export default function ReleaseNotesContent({ docId, version }: Props) {
    const data = useReleaseNotes(docId, version);

    if (!data) return <p>No release Notes available</p>;

    const { tabs } = data;

    return (
        <div className="ivertix-release-notes">
            <Tabs>
                {tabs.map(tab => (
                    <TabItem key={tab.label} value={tab.label} label={tab.label} className="markdown">
                        <Heading as="h2" id={tab.label}>{tab.label} Release Notes</Heading>
                        {tab.notes.map(note => (
                            <React.Fragment key={`${note.component}-${note.version}`}>
                                <code className={styles.date}>{formatDate(note.date)}</code>
                                <Heading className={styles.heading} as="h3" id={`${note.component}-${note.version}`}>
                                    {tab.label === "All" ? `${note.component} - ${note.version}` : note.version}
                                </Heading>
                                {note.sections.map(s => (
                                    <Details key={s.name} className={styles.section} summary={s.name}>
                                        {s.description && <p>{s.description}</p>}
                                        <ul>
                                            {s.listItems.map(item => <li key={item}>{item}</li>)}
                                        </ul>
                                    </Details>
                                ))}
                            </React.Fragment>
                        ))}
                    </TabItem>
                ))}
            </Tabs>
        </div>
    );
}
