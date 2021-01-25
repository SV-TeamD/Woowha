import React from "react";
import { Route } from "react-router-dom";
import mainpage from "./mainpage";
import resultpage from "./resultpage";
import ScrollToTop from "./ScrollToTop";
import testpage from "./testpage";

const App = () => {
  return (
    <div>
      <ScrollToTop>
        <Route path="/" component={mainpage} exact={true} />
        <Route path="/test" component={testpage} exact={true} />
        <Route path="/resultpage" component={resultpage} />
      </ScrollToTop>
    </div>
  );
};

export default App;
