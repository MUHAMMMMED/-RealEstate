import React from 'react';
import { FaMapMarkerAlt } from 'react-icons/fa';
import Map from '../Map/Map';
import DetailsInfo from './components/DetailsIfo/DetailsIfo';
import './style.css';

export default function CardDetails({ darkMode }) {
    return (<>
        <div className='CardDetails'>

            <div className={darkMode ? 'Details_center CardDetails-dark ' : 'Details_center CardDetails-light'}>
                <h1 className="Details_h2"> شقة للإيجار في شارع المنصوريه</h1>
                <p className="Details-location  ">
                    <samp className='Details-location-samp'> <FaMapMarkerAlt className="Details-marker-icon" /></samp>
                    <samp className='Details-location-samp'> شقة للإيجار في شارع المنصوريه</samp>
                </p>

                <strong className="Details_price"> <samp>150,000 </samp><span className='currency'>ريال</span></strong>

                <p className={darkMode ? 'Details_p Ifo-text-dark ' : 'Details_p Ifo-text-light'}>

                    للايجار شقه في حي ظهره لبن
                    شقة دور ثالث بدون سطح
                    مجدده كامل بويات وسباكة وكهرباء

                    في فيلا خاصه

                    مدخلين واحد للرجال مجلس ودورة مياه
                    والثاني للعائلة

                    تحتوي الشقة على مجلس رجال وصالة ومطبخ وغرفتين ودورتين مياه

                    الماء والكهرباء على المالك مجاني

                    الاجار 28 الف دفعتين عائلة صغيرة


                    رقم رخصة فال للوساطة والتسويق: 1100171520
                </p>
                <DetailsInfo darkMode={darkMode} />



                <Map darkMode={darkMode} /></div>
        </div>
    </>
    )
} 