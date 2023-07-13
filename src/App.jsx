import React, { useState } from "react";
import "./App.css";
function App() {
  const [counter, setCounter] = useState(0);

  return (
    <React.Fragment>
      <div className="container">
        <div className="widget">
          <h1 id="header">Devops Counter</h1>
          <input
            className="counter"
            onChange={(event) => {
              if (Number.isNaN(Number(event.target.value))) return;

              setCounter(Number(event.target.value));
            }}
            onBlur={(event) => setCounter(Number(event.target.value))}
            value={counter}
          />
          <div className="inputs">
            <div>
              <button onClick={() => setCounter((prev) => prev - 1)}>-</button>

              <button onClick={() => setCounter((prev) => prev + 1)}>+</button>
            </div>
            <button className="btn-reset" onClick={() => setCounter(0)}>
              Reset
            </button>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

export default App;
