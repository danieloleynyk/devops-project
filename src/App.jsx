import React, { useState } from "react";
import "./App.css";
function App() {
  const [counter, setCounter] = useState(0);
  const [errorMessage, setErrorMessage] = useState("");
  const lowerLimit = -10; // Set your lower limit here
  const upperLimit = 10; // Set your upper limit here
  const numberRegex = /^-?\d+$/;

  const isValidNumber = (input) => {
    return numberRegex.test(input);
  };

  const handleInput = (event) => {
    const value = event.target.value.trim();

    if (value.length === 0 || value === "-") {
      setCounter(value);
      setErrorMessage("");
      return;
    }

    if (!isValidNumber(value)) {
      setErrorMessage("The value is invalid");
    } else if (value > upperLimit) {
      setCounter(upperLimit);
      setErrorMessage("Counter reached the upper limit");
    } else if (value < lowerLimit) {
      setCounter(lowerLimit);
      setErrorMessage("Counter reached the lower limit");
    } else {
      setCounter(value);
      setErrorMessage("");
    }
  };

  const handleIncrement = () => {
    if (counter >= upperLimit) {
      setErrorMessage("Counter reached the upper limit");
    } else {
      setCounter((prevCounter) => prevCounter + 1);
      setErrorMessage("");
    }
  };

  const handleDecrement = () => {
    if (counter <= lowerLimit) {
      setErrorMessage("Counter reached the lower limit");
    } else {
      setCounter((prevCounter) => prevCounter - 1);
      setErrorMessage("");
    }
  };

  const handleReset = () => {
    setCounter(0);
    setErrorMessage("");
  };

  return (
    <React.Fragment>
      <div className="container">
        <div className="widget">
          <h1 id="header">Devops Counter</h1>
          <input className="counter" onChange={handleInput} value={counter} />
          {errorMessage && <p className="error-message">{errorMessage}</p>}

          <div className="inputs">
            <div>
              <button
                disabled={counter <= lowerLimit}
                onClick={handleDecrement}
              >
                -
              </button>

              <button
                disabled={counter >= upperLimit}
                onClick={handleIncrement}
              >
                +
              </button>
            </div>
            <button className="btn-reset" onClick={handleReset}>
              Reset
            </button>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

export default App;
