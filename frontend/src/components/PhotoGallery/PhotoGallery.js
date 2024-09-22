import React, { useEffect, useMemo, useState } from 'react';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import Lightbox from 'react-image-lightbox';
import 'react-image-lightbox/style.css';
import 'swiper/css';
import 'swiper/css/navigation';
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';
import './style.css';

const PhotoGallery = ({ darkMode }) => {
    const images = useMemo(() => [
        'https://via.placeholder.com/800x400?text=Property+Image+1',
        'https://via.placeholder.com/800x400?text=Property+Image+2',
        'https://via.placeholder.com/800x400?text=Property+Image+3',
        'https://via.placeholder.com/800x400?text=Property+Image+4',
        'https://via.placeholder.com/800x400?text=Property+Image+5',
        'https://via.placeholder.com/800x400?text=Property+Image+6',
        'https://via.placeholder.com/800x400?text=Property+Image+7',
        'https://via.placeholder.com/800x400?text=Property+Image+8',
    ], []);

    const [mainImage, setMainImage] = useState(images[0]);
    const [lightboxOpen, setLightboxOpen] = useState(false);

    useEffect(() => {
        const interval = setInterval(() => {
            setMainImage(prev => {
                const nextIndex = (images.indexOf(prev) + 1) % images.length;
                return images[nextIndex];
            });
        }, 10000);

        return () => clearInterval(interval);
    }, [images]);

    return (
        <div className={darkMode ? 'PhotoGallery PhotoGallery-dark ' : 'PhotoGallery PhotoGallery-light'}>



            <div className="main-image-container" onClick={() => setLightboxOpen(true)}>
                <img src={mainImage} alt="Main Property" className="main-image" />
            </div>
            <Swiper
                spaceBetween={10}
                slidesPerView={4}
                navigation={{
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                }}
                modules={[Navigation]}
            >
                {images.map((image, index) => (
                    <SwiperSlide key={index} onClick={() => setMainImage(image)}>
                        <img src={image} alt={`Property ${index + 1}`} className="thumbnail-image" />
                    </SwiperSlide>
                ))}
                <div className={darkMode ? 'swiper-button-next PhotoGallery-dark ' : 'swiper-button-next PhotoGallery-light'}>
                    <FaChevronRight size={20} color={darkMode ? '#fff' : '#2196f3'} />
                </div>
                <div className={darkMode ? 'swiper-button-prev PhotoGallery-dark ' : 'swiper-button-prev PhotoGallery-light'}>
                    <FaChevronLeft size={20} color={darkMode ? '#fff' : '#2196f3'} />




                </div>
            </Swiper>

            {lightboxOpen && (
                <Lightbox
                    mainSrc={mainImage}
                    onCloseRequest={() => setLightboxOpen(false)}
                    nextSrc={images[(images.indexOf(mainImage) + 1) % images.length]}
                    prevSrc={images[(images.indexOf(mainImage) - 1 + images.length) % images.length]}
                    onMovePrevRequest={() =>
                        setMainImage(images[(images.indexOf(mainImage) - 1 + images.length) % images.length])
                    }
                    onMoveNextRequest={() =>
                        setMainImage(images[(images.indexOf(mainImage) + 1) % images.length])
                    }
                />
            )}
        </div>
    );
};

export default PhotoGallery;