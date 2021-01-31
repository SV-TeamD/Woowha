import React from "react";
import Header from "./components/Header";
import ImageUpload from "./ImageUpload";
import Overview from "./components/Overview";
import About from "./components/About";
import "./components/Button.css";
import "./Home.css";

const Home = () => {
  return (
    <div>
      <Header />
      <ImageUpload />
      <Overview />
      <About />
    </div>
  );
};

export default Home;
