import React from 'react';
import { FaMoon, FaSun } from 'react-icons/fa'; // استيراد الأيقونات من react-icons
import './ThemeSwitcher.css'; // استيراد ملف CSS للتصميم

const ThemeSwitcher = ({ toggleTheme, darkMode }) => {
    return (
        <button className="theme-switcher" onClick={toggleTheme}>
            {darkMode ? (
                <>
                    <FaSun className="icon" /> Light Mode
                </>
            ) : (
                <>
                    <FaMoon className="icon" /> Dark Mode
                </>
            )}
        </button>
    );
};

export default ThemeSwitcher;