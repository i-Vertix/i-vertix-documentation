import React, {useMemo, useState} from 'react';

const text0Title = "Who we are";
const text0 = <p>
    At i-Vertix, we are a team of dedicated professionals, IT enthusiasts, and problem-solvers who are passionate about
    ensuring the heartbeat of your digital infrastructure never falters. With years of expertise in the field, we have
    made it our purpose to help organizations thrive in the digital era.
</p>;
const text1Title = "What we do";
const text1 = <p>
    We specialize in crafting cutting-edge IT Network Management solutions that provide real-time insights, improve
    efficiency, and enhance the overall IT experience. Whether you're a small business looking to optimize your
    operations or a global enterprise striving for digital excellence, i-Vertix is your trusted partner for IT
    environments.
</p>;
const text2Title = "Why choose us";
const text2 = <>
    <p>
        <strong>Innovation:</strong> We are at the forefront of IT Network Management technology, constantly innovating
        to meet the evolving
        needs of your business.
    </p>
    <p>
        <strong>Expertise:</strong> Our team of seasoned professionals brings unparalleled expertise to deliver tailored
        solutions that
        match your unique requirements.
    </p>
    <p>
        <strong>Scalability:</strong> Our solutions are designed to grow with your business, ensuring you're always
        prepared for what's next.
    </p>
    <p>
        <strong>Reliability:</strong> Count on i-Vertix to provide reliable, real-time monitoring that keeps your
        systems running smoothly.
    </p>
    <p>
        <strong>Customer Focus:</strong> Your success is our priority. We're committed to providing exceptional
        support and building lasting partnerships.
    </p>
</>;

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