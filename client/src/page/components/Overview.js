import React from "react";
import OverviewImage from "./OverviewImage"
import "./Overview.css";

const Overview = () => {
  return (
    <div className="overview-center">
      <h1>Overview</h1>
      {[...Array(16).keys()].map((index) => {
        return (
          <OverviewImage key={index} index={index+1}></OverviewImage>
        );
      })}
    </div>
  );
};

export default Overview;
