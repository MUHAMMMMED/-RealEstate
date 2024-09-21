// import './App.css';
import React, { useEffect, useState } from 'react';
import './App.css';
import ThemeSwitcher from './components/ThemeSwitcher/ThemeSwitcher';
import './styles/global.css';
import './styles/variables.css';

const App = () => {
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem('darkMode') === 'true';
  });

  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  const toggleDarkMode = () => {
    setDarkMode(prevMode => !prevMode);
  };

  return (
    <div className={darkMode ? 'App dark' : 'App light'}>
      <header>
        <h1>Welcome to My Project</h1>
        <ThemeSwitcher toggleTheme={toggleDarkMode} darkMode={darkMode} />
      </header>
      <main>
        <h2>This is a sample content area.</h2>
      </main>
    </div>
  );
};

export default App;