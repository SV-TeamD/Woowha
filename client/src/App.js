import React from "react";
import { Route } from "react-router-dom";
import mainpage from "./mainpage";
import resultpage from "./resultpage";
import testpage from "./testpage";

const App = () => {
  return (
    <div>
      <Route path="/" component={mainpage} exact={true} />
      <Route path="/resultpage" component={resultpage} />
      <Route path="/test" component={testpage} />
    </div>
  );
};

export default App;
