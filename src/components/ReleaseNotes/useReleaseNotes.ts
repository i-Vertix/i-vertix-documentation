import { useMemo } from 'react';

export type Section = {
  name: string;
  description?: string;
  listItems: string[];
}

export type ReleaseNote = {
  component: string;
  version: string;
  date: number;
  sections: Section[];
}

export type ReleaseNotesTab = {
  label: string;
  notes: ReleaseNote[];
}

export type ReleaseNotesData = {
  tabs: ReleaseNotesTab[];
  allNotes: ReleaseNote[];
}

const useReleaseNotes = (docId: string, version: string): ReleaseNotesData | null => {
  return useMemo(() => {
    const notes: ReleaseNote[] = require(`@site/${docId}_versioned_docs/version-${version}/release-notes.json`);

    if (!notes || notes.length === 0) return null;

    const sortedNotes = [...notes].sort((a, b) => b.date - a.date);
    const components = Array.from(new Set(sortedNotes.map(n => n.component))).sort();

    const tabs: ReleaseNotesTab[] = [
      { label: 'All', notes: sortedNotes },
      ...components.map(c => ({
        label: c,
        notes: sortedNotes.filter(n => n.component === c),
      })),
    ];

    // const toc: ReleaseNotesData['toc'] = sortedNotes.map(n => ({
    //   id: n.version,
    //   value: `${n.component} ${n.version}`,
    //   level: 2,
    //   children: n.sections.map(s => ({
    //     id: `${n.version}-${s.name}`,
    //     value: s.name,
    //     level: 3,
    //   })),
    // }));

    return { tabs, allNotes: sortedNotes };
  }, [docId, version]);
}

export default useReleaseNotes;