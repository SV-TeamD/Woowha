import React from "react";
import Header from "./components/Header";
import ImageResult from "./ImageResult";
import Overview from "./components/Overview";
import About from "./components/About";
import "./components/Button.css";
import "./Result.css";

const Result = () => {
  return (
    <div>
      <Header />
      <ImageResult />
      <Overview />
      <About />
    </div>
  );
};

export default Result;
