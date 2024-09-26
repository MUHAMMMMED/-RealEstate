import React from 'react';
import './style.css';

export default function Map() {
    return (
        <div className="Map">
            <div className="map_canvas">

                <h4 className="Map_h4">العنوان على الخريطة</h4>

                <iframe
                    className="map_iframe"
                    width="100%"
                    height="400px"
                    frameBorder="0"
                    scrolling="no"
                    marginHeight="0"
                    marginWidth="0"

                    src="https://maps.google.com/maps?width=660&amp;height=385&amp;hl=en&amp;q={{cairo}}&amp;t=k&amp;z=18&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"
                ></iframe>
            </div>
        </div>
    );
}