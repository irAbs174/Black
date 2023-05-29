import React from 'react';
import ReactDOM from 'react-dom';
import FocusTrapReact from 'focus-trap-react';

const App = () => {
  return (
    <FocusTrapReact>
      <div>
        <h1>My Focus-Trapped App</h1>
        <p>This is a paragraph inside a focus-trapped element.</p>
        <button>Click me!</button>
      </div>
    </FocusTrapReact>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));