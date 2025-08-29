import React, { useState } from 'react';
import { BiTachometer } from "react-icons/bi";
import { LiaCogSolid } from "react-icons/lia";

import {
    FaAngleDoubleLeft,
    FaAngleDoubleRight,
    FaBars,
    FaRegUser
} from 'react-icons/fa';

import logoSmall from '../../assets/logo.jpg';
import logo from '../../assets/logo.png';

import BrowserStats from '../../components/BrowserStats/BrowserStats';
import CampaignChart from '../../components/CampaignChart/CampaignChart';
import DashboardCard from '../../components/DashboardCard/DashboardCard';
import ActiveUsersCard from '../../components/dashboard/components/ActiveUsersCard/ActiveUsersCard';
import Content from '../../components/dashboard/components/Content/Content';
import CustomerRatings from '../../components/dashboard/components/CustomerRatings/CustomerRatings';
import Notifications from '../../components/dashboard/components/Notifications/Notifications';
import Sidebar from '../../components/dashboard/components/Sidebar/Sidebar';
import './Dashboard.css';

const Dashboard = () => {
    const [isLeft, setIsLeft] = useState(true);
    const [language, setLanguage] = useState('ar');
    const [isSidebarVisible, setIsSidebarVisible] = useState(true);
    const [isSidebarExpanded, setIsSidebarExpanded] = useState(true); // حالة توسعة السايد بار
    const [isMobileSidebarVisible, setIsMobileSidebarVisible] = useState(false); // حالة عرض السايد بار في الموبايل

    const sidebarItems = [
        {
            label_ar: 'الملف الشخصي',
            label_en: 'Profile',
            icon: <FaRegUser />,
        },
        {
            label_ar: 'الملف الشخصي',
            label_en: 'Profile',
            icon: <FaRegUser />,
        },
        {
            label_ar: 'لوحة التحكم',
            label_en: 'Dashboard',
            icon: <BiTachometer />,
            subItems: [
                { label_ar: 'نظرة عامة', label_en: 'Overview', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },

            ],
        },
        {
            label_ar: 'الإعدادات',
            label_en: 'Settings',
            icon: <LiaCogSolid />,
        },
        {
            label_ar: 'الملف الشخصي',
            label_en: 'Profile',
            icon: <FaRegUser />,
        },
        {
            label_ar: 'الإعدادات',
            label_en: 'Settings',
            icon: <LiaCogSolid />,
        },
        {
            label_ar: 'الملف الشخصي',
            label_en: 'Profile',
            icon: <FaRegUser />,
        },

        {
            label_ar: 'لوحة التحكم',
            label_en: 'Dashboard',
            icon: <BiTachometer />,
            subItems: [
                { label_ar: 'نظرة عامة', label_en: 'Overview', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },
                { label_ar: 'إحصائيات', label_en: 'Statistics', icon: <BiTachometer /> },

            ],
        },
    ];

    const handleLanguageChange = () => {
        setIsLeft(!isLeft);
        setLanguage(language === 'ar' ? 'en' : 'ar');
    };

    const toggleSidebar = () => {
        setIsSidebarVisible(!isSidebarVisible);
    };

    const toggleSidebarExpansion = () => {
        setIsSidebarExpanded(!isSidebarExpanded);
    };

    const toggleMobileSidebar = () => {
        setIsMobileSidebarVisible(!isMobileSidebarVisible);
    };

    return (
        <div className={`dashboard ${isLeft ? 'ltr' : 'rtl'} ${isMobileSidebarVisible ? 'mobile' : ''}`}>
            {isSidebarVisible && (
                <Sidebar
                    logo={logo}
                    logoSmall={logoSmall}
                    items={sidebarItems}
                    isLeft={isLeft}
                    isExpanded={isSidebarExpanded}
                    toggleExpansion={toggleSidebarExpansion}
                />
            )}


            <div className="main-content">
                <div className="top-bar " style={{ textAlign: isLeft ? 'right' : 'left', direction: isLeft ? 'rtl' : 'ltr' }} >
                    <button className="menu-toggle" onClick={toggleMobileSidebar}>
                        <FaBars />
                    </button>
                    <button onClick={handleLanguageChange} className="language-toggle">
                        {language === 'ar' ? 'العربية' : 'English'}
                        {isLeft ? <FaAngleDoubleLeft /> : <FaAngleDoubleRight />}
                    </button>
                </div>
                <Notifications />
                <ActiveUsersCard />

                <DashboardCard />

                <BrowserStats />
                <CampaignChart />


                <CustomerRatings />
                <Content language={language} />
            </div>
        </div>
    );
};

export default Dashboard;

