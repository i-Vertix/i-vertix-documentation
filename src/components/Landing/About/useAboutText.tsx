import React, {useMemo, useState} from 'react';

const text0Title = "Who we are";
const text0 = <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent scelerisque nisl eu orci mattis molestie. Nam
    hendrerit sagittis laoreet. Mauris faucibus nunc id dui consequat, vel pellentesque leo porta. Nulla eu elementum
    leo, quis imperdiet ligula. Praesent sed lectus interdum, iaculis turpis ac, faucibus lacus. Proin vel placerat leo.
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras quis tristique
    velit, eget varius ex. Morbi fermentum sapien dignissim, pharetra tortor at, laoreet arcu.
</p>;
const text1Title = "What we do";
const text1 = <p>
    Nunc eu rutrum purus, eu accumsan mauris. Mauris at felis laoreet, porta est ut, interdum sapien. Vestibulum vitae
    dui et nulla bibendum feugiat. Etiam justo tellus, lacinia a mattis ac, euismod sit amet leo. Donec vitae neque
    volutpat, consectetur magna accumsan, pellentesque mi. Maecenas in nibh nibh. Nulla commodo enim egestas efficitur
    iaculis. Vestibulum maximus, orci varius volutpat facilisis, est nisl accumsan nisl, at condimentum nunc lectus nec
    libero. Vivamus ante est, fringilla non odio ut, interdum ultricies sapien. Donec sit amet gravida tellus, a
    venenatis ligula.
</p>;
const text2Title = "Why choose us";
const text2 = <p>
    Cras fringilla nibh eget diam congue, ac ultricies ex tempus. Proin ullamcorper, enim ac pellentesque commodo,
    tortor enim auctor purus, vitae hendrerit purus metus et leo. In pellentesque ex eu felis varius, sit amet
    ullamcorper est viverra. Suspendisse placerat eros vitae massa porttitor venenatis. Vivamus vitae consequat ipsum.
    Proin non pretium eros. In vehicula molestie hendrerit. Duis ac arcu pharetra, efficitur eros sed, elementum arcu.
    Nam vestibulum ornare diam vitae aliquam. Phasellus neque purus, viverra non euismod sed, laoreet eget sem. Cras et
    nunc facilisis, consectetur purus sit amet, mollis magna.
</p>;

const useAboutText = () => {

    const [selectedText, setSelectedText] = useState<number>(0);
    const onSelectedTextChange = (index: number) => {
        setSelectedText(index);
    }

    const text = useMemo(() => {
        switch (selectedText) {
            case 0:
                return {title: text0Title, text: text0};
            case 1:
                return {title: text1Title, text: text1};
            case 2:
                return {title: text2Title, text: text2};
            default:
                return null;
        }
    }, [selectedText]);

    return {text, onSelectedTextChange, selectedText};

};

export default useAboutText;