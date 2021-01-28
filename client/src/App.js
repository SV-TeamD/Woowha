import React from "react";
import { Route } from "react-router-dom";
import mainpage from "./mainpage";
import resultpage from "./resultpage";
import testpage from "./test";

const App = () => {
  return (
    <div>
      <Route path="/" component={mainpage} exact={true} />
      <Route path="/test" component={testpage} exact={true} />
      <Route path="/resultpage" component={resultpage} />
    </div>
  );
};

export default App;
