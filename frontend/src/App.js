import React, { useEffect, useState } from 'react';
import './App.css';
import Header from './components/Header/Header';
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
      <Header darkMode={darkMode} />

      <h1>Welcome to My Project</h1>

      <ThemeSwitcher toggleTheme={toggleDarkMode} darkMode={darkMode} />

    </div>
  );
};

export default App;