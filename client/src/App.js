import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { Home, Result, TestPage } from "./page/index";
import { Header, Overview, About } from "./page/components/index";

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
          <Route path="/" exact component={Home} />
          <Route path="/result" component={Result} />
          <Route path="/test" component={TestPage} />
        <Overview />
        <About />
      </BrowserRouter>
    </div>
  );
};

export default App;
