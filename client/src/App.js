import React from "react";
import { Route } from "react-router-dom";
import mainpage from "./mainpage";

const App = () => {
  return (
    <div>
      <Route path="/" component={mainpage} />
    </div>
  );
};

export default App;
