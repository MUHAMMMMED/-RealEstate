import React from 'react';
import './style.css';

export default function Video({ darkMode }) {
    return (

        <div className={darkMode ? 'CardVideo Video-dark' : 'CardVideo Video-light '}>

            <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY?playlist=tgbNymZ7vqY&loop=1" class="iframe"></iframe>
        </div>
    )
}
