import React, { useEffect, useState } from 'react';
import './App.css';
import Header from './components/Header/Header';
import PhotoGallery from './components/PhotoGallery/PhotoGallery';
import ThemeSwitcher from './components/ThemeSwitcher/ThemeSwitcher';

import 'swiper/css'; // ملف CSS الرئيسي لـ Swiper
import 'swiper/css/navigation'; // إذا كنت تحتاج إلى الملاحة
import 'swiper/css/pagination'; // إذا كنت تستخدم الترقيم

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
      <PhotoGallery darkMode={darkMode} />
      {/*
      <Filter darkMode={darkMode} />
      <Card darkMode={darkMode} />*/}
      <ThemeSwitcher toggleTheme={toggleDarkMode} darkMode={darkMode} />

    </div>
  );
};

export default App;


