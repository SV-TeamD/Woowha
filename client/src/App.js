import React from "react";
import { Route, Link } from "react-router-dom";
import mainpage from "./mainpage";
import resultpage from "./resultpage";

const App = () => {
  return (
    <div>
      <Route path="/" component={mainpage} />
    </div>
  );
};

export default App;
