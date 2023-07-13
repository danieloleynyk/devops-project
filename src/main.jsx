import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

const htmlRoot = document.getElementById("root");
const root = ReactDOM.createRoot(htmlRoot);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
