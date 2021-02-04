import React from "react";
import "./About.css";

const About = () => {
  return (
    <div className="about">
      <h1>About</h1>
      <p>This website was created by
      <a href="https://github.com/Jivvon">Jivvon</a>,
      <a href="https://github.com/ByeongdoChoi">ByeongdoChoi</a>,
      <a href="https://github.com/genius-jo">genius-jo</a>,
      <a href="https://github.com/iSuddenly">iSuddenly</a></p>
      <p>It uses Deep Learning model CartoonGAN and CycleGAN to translate images.</p>
      <p>Thank you!</p>
    </div >
  );
};

export default About;
