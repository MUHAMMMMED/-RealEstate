import React from 'react';
import { FaMoon, FaSun } from 'react-icons/fa';
import './ThemeSwitcher.css';

const ThemeSwitcher = ({ toggleTheme, darkMode }) => {
    return (
        <button className="theme-switcher" onClick={toggleTheme}>
            {darkMode ? (
                <>
                    <FaSun className="icon" />
                </>
            ) : (
                <>
                    <FaMoon className="icon" />
                </>
            )}
        </button>
    );
};

export default ThemeSwitcher;