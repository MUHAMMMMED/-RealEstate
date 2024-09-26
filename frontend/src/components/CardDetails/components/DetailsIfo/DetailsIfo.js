import React from 'react';
import { BiBracket, BiBuilding, BiBuildingHouse, BiCalendarWeek, BiCircleHalf, BiCross, BiRectangle } from "react-icons/bi";
import { IoBedOutline } from "react-icons/io5";
import { LuUtensils } from "react-icons/lu";
import { MdOutlinePayments } from "react-icons/md";
import { PiArmchairLight } from "react-icons/pi";
import { TbAirConditioningDisabled, TbBath } from "react-icons/tb";
import './style.css';

export default function DetailsInfo({ darkMode }) {
    return (
        <div className='DetailsInfo'>
            <h4 className='Ifo'>المعلومات التفصيلية</h4>
            <br />
            <table>
                <tbody>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiCalendarWeek /> تاريخ النشر </th>
                        <th>٢٩ شوال ١٤٣٨ هـ</th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiBuildingHouse /> نوع العقار </th>
                        <th> فيلا</th>
                    </tr>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiBracket /> المساحة   </th>

                        <th>119 م²</th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiCross /> اتجاه الشارع  </th>
                        <th> شرقية</th>
                    </tr>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiBuilding /> الدور </th>
                        <th>3</th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <PiArmchairLight /> أثاث المنزل</th>
                        <th> غير مفروشة</th>
                    </tr>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <IoBedOutline /> الغرف</th>
                        <th>3</th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiRectangle /> الصالات </th>
                        <th> 1</th>
                    </tr>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <LuUtensils /> مطبخ</th>
                        <th> 1 </th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <TbBath /> دورات المياه  </th>
                        <th>2</th>
                    </tr>

                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiCircleHalf />     بلكونة </th>
                        <th> 2</th>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <TbAirConditioningDisabled /> مكيف </th>
                        <th> نعم</th>
                    </tr>
                    <tr>
                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <BiBuilding />  عمر البناء </th>
                        <th> 20+ سنة</th>

                        <th className={darkMode ? 'Ifo-text-dark ' : 'Ifo-text-light'}>
                            <MdOutlinePayments />  طريقة الدفع   </th>
                        <th> كاش فق</th>
                    </tr>
                </tbody>
            </table>


        </div>
    );
}