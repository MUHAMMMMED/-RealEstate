// src/components/UploadMedia.js

import axios from 'axios';
import React, { useState } from 'react';
import './UploadMedia.css'; // ملف CSS الخاص بالمكون

function UploadMedia() {
    const [selectedImage, setSelectedImage] = useState(null);
    const [recordedAudio, setRecordedAudio] = useState(null);
    const [animatedVideo, setAnimatedVideo] = useState(null);
    const [isRecording, setIsRecording] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioURL, setAudioURL] = useState(null);

    const handleImageChange = (e) => {
        setSelectedImage(e.target.files[0]);
    };

    const startRecording = () => {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                const recorder = new MediaRecorder(stream);
                setMediaRecorder(recorder);
                recorder.start();
                setIsRecording(true);
                const chunks = [];

                recorder.ondataavailable = (e) => {
                    chunks.push(e.data);
                };

                recorder.onstop = () => {
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    setRecordedAudio(blob);
                    setAudioURL(URL.createObjectURL(blob));
                };
            })
            .catch(err => {
                console.error("فشل في الوصول إلى الميكروفون:", err);
            });
    };

    const stopRecording = () => {
        mediaRecorder.stop();
        setIsRecording(false);
    };

    const handleUpload = () => {
        const formData = new FormData();
        formData.append('image', selectedImage);
        formData.append('audio', recordedAudio);

        axios.post('http://localhost:8000/api/animator/upload/', formData)
            .then(response => {
                setAnimatedVideo(`http://localhost:8000/media/${response.data.animated_video_url}`);
            })
            .catch(error => {
                console.error("خطأ في رفع الوسائط:", error);
            });
    };

    return (
        <div className="upload-container">
            <h2>تحميل صورة وتسجيل صوت لتحريك الوجه</h2>
            <div className="input-group">
                <label htmlFor="imageUpload" className="custom-file-upload">
                    اختر صورة
                </label>
                <input
                    id="imageUpload"
                    type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                />
            </div>

            <div className="record-group">
                <button
                    className={`record-button ${isRecording ? 'recording' : ''}`}
                    onClick={isRecording ? stopRecording : startRecording}
                >
                    {isRecording ? 'إيقاف التسجيل' : 'بدء التسجيل'}
                </button>
                {audioURL && (
                    <audio controls src={audioURL}></audio>
                )}
            </div>

            <button
                className="upload-button"
                onClick={handleUpload}
                disabled={!selectedImage || !recordedAudio}
            >
                تحميل ومعالجة
            </button>

            {animatedVideo && (
                <div className="video-container">
                    <h3>الفيديو المتحرك:</h3>
                    <video controls src={animatedVideo}></video>
                </div>
            )}
        </div>
    );
}

export default UploadMedia;