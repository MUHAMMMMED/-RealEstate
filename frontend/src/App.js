import React, { useEffect, useState } from 'react';
import './App.css';
import './index.css';

import ThemeSwitcher from './components/ThemeSwitcher/ThemeSwitcher';

import 'swiper/css'; // ملف CSS الرئيسي لـ Swiper
import 'swiper/css/navigation'; // إذا كنت تحتاج إلى الملاحة
import 'swiper/css/pagination'; // إذا كنت تستخدم الترقيم

import Dashboard from './Screens/Dashboard/Dashboard';
import UploadMedia from './Screens/UploadImage/UploadImage';
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
      {/* <Header darkMode={darkMode} />

      <PhotoGallery darkMode={darkMode} />
      <Video darkMode={darkMode} />
      <CardDetails darkMode={darkMode} />
      <IfoCard darkMode={darkMode} />
      <FloatingBtn /> */}
      {/*
      <Filter darkMode={darkMode} />
      <Card darkMode={darkMode} />*/}
      <UploadMedia />
      <ThemeSwitcher toggleTheme={toggleDarkMode} darkMode={darkMode} />
      <Dashboard />

    </div>
  );
};

export default App;


