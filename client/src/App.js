import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from "./page/Home";
import Result from "./page/Result";
import TestPage from "./page/TestPage";
const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" component={Home} exact={true} />
          <Route path="/resultpage" component={Result} />
          <Route path="/test" component={TestPage} />
        </Switch>
      </BrowserRouter>
    </div>
  );
};

export default App;
