import React from "react";
import "./Header.css";

const Header = () => {
  const scrollToTop = () => {
    window.scrollTo(0, 0);
  };
  const scrollToOverview = () => {
    window.scrollTo(0, 1600);
  };
  const scrollToAbout = () => {
    window.scrollTo(0, 1800);
  };

  return (
    <div className="top-header">
      <header>
        <ul>
          <li>
            <a href="/" style={{ fontWeight: "bold" }}>
              Woowha
            </a>
          </li>
          <li>
            <a href="#image" onClick={scrollToTop}>
              Image
            </a>
          </li>
          <li>
            <a href="#overview" onClick={scrollToOverview}>
              Overview
            </a>
          </li>
          <li>
            <a href="#about" onClick={scrollToAbout}>
              About
            </a>
          </li>
        </ul>
      </header>
    </div>
  );
};

export default Header;
