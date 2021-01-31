import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import Home from "./page/Home";
import Result from "./page/Result";
const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Route path="/" component={Home} exact={true} />
        <Route path="/resultpage" component={Result} />
      </BrowserRouter>
    </div>
  );
};

export default App;
