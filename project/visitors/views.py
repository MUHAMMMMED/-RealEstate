from rest_framework import viewsets  # استيراد viewsets من Django Rest Framework
from .models import (
    Device,
    OperatingSystem,
    Location,
    DeviceType,
    OS,
    PeakTime,
    Region,
    City,
    Country,
    UserVisit,
)
from .serializers import (
    DeviceSerializer,
    OperatingSystemSerializer,
    LocationSerializer,
    DeviceTypeSerializer,
    OSSerializer,
    PeakTimeSerializer,
    RegionSerializer,
    CitySerializer,
    CountrySerializer,
    UserVisitSerializer,
)

from django.utils import timezone
from datetime import timedelta, datetime


 
# عرض البيانات لجهاز
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()  # استعلام للحصول على جميع الأجهزة
    serializer_class = DeviceSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات لنظام التشغيل
class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all()  # استعلام للحصول على جميع أنظمة التشغيل
    serializer_class = OperatingSystemSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات للموقع
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()  # استعلام للحصول على جميع المواقع
    serializer_class = LocationSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات لنوع الجهاز
class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()  # استعلام للحصول على جميع أنواع الأجهزة
    serializer_class = DeviceTypeSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات لنظام تشغيل الجهاز
class OSViewSet(viewsets.ModelViewSet):
    queryset = OS.objects.all()  # استعلام للحصول على جميع أنظمة تشغيل الأجهزة
    serializer_class = OSSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات لأوقات الذروة
class PeakTimeViewSet(viewsets.ModelViewSet):
    queryset = PeakTime.objects.all()  # استعلام للحصول على جميع أوقات الذروة
    serializer_class = PeakTimeSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات للمنطقة
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()  # استعلام للحصول على جميع المناطق
    serializer_class = RegionSerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات للمدينة
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()  # استعلام للحصول على جميع المدن
    serializer_class = CitySerializer  # تحديد السيريالايزر المستخدم

# عرض البيانات للبلد
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()  # استعلام للحصول على جميع البلدان
    serializer_class = CountrySerializer  # تحديد السيريالايزر المستخدم

# # عرض البيانات لزيارة المستخدم
class UserVisitViewSet(viewsets.ModelViewSet):
    queryset = UserVisit.objects.all()  # استعلام للحصول على جميع زيارات المستخدمين
    serializer_class = UserVisitSerializer  # تحديد السيريالايزر المستخدم




# views.py

# views.py


# class UserVisitViewSet(viewsets.ModelViewSet):
#     serializer_class = UserVisitSerializer  # تحديد السيريالايزر المستخدم

#     def get_queryset(self):
#         # الحصول على جميع زيارات المستخدمين كبداية
#         queryset = UserVisit.objects.all()

#         # الحصول على المعلمات من طلب GET
#         country_id = self.request.query_params.get('country', None)  # معلمة الدولة
#         filter_option = self.request.query_params.get('filter', None)  # معلمة الفلتر
#         start_date = self.request.query_params.get('start_date', None)  # تاريخ البدء
#         end_date = self.request.query_params.get('end_date', None)  # تاريخ الانتهاء

#         # تصفية البيانات بناءً على الدولة إذا كانت موجودة
#         if country_id:
#             queryset = queryset.filter(country__id=country_id)

#         # تطبيق الفلتر بناءً على الخيار المحدد
#         if filter_option:
#             queryset = self.apply_filter(queryset, filter_option)

#         # تصفية بواسطة تاريخين محددين إذا كانت موجودة
#         if start_date and end_date:
#             try:
#                 start = datetime.strptime(start_date, '%Y-%m-%d').date()
#                 end = datetime.strptime(end_date, '%Y-%m-%d').date()
#                 queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=end)
#             except ValueError:
#                 # إذا كان هناك خطأ في تنسيق التواريخ، يمكن تجاهل التصفية أو التعامل مع الخطأ
#                 pass

#         return queryset  # إعادة مجموعة النتائج المصفاة

#     def apply_filter(self, queryset, filter_option):
#         today = timezone.now().date()

#         if filter_option == 'last_year':
#             # السنة السابقة
#             start = today.replace(year=today.year - 1, month=1, day=1)
#             end = today.replace(month=12, day=31)
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=end)

#         elif filter_option == 'current_year':
#             # السنة الحالية
#             start = today.replace(month=1, day=1)
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=today)

#         elif filter_option == 'last_six_months':
#             # آخر ستة أشهر
#             start = today - timedelta(days=182)  # تقريبًا ستة أشهر
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=today)

#         elif filter_option == 'last_three_months':
#             # آخر ثلاثة أشهر
#             start = today - timedelta(days=90)  # تقريبًا ثلاثة أشهر
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=today)

#         elif filter_option == 'last_month':
#             # آخر شهر
#             start = today.replace(day=1) - timedelta(days=1)  # آخر يوم في الشهر الماضي
#             start = start.replace(day=1)  # أول يوم في الشهر الماضي
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=today)

#         elif filter_option == 'current_month':
#             # الشهر الحالي
#             start = today.replace(day=1)
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=today)

#         elif filter_option == 'current_week':
#             # الأسبوع الحالي (من الأحد إلى السبت)
#             start = today - timedelta(days=today.weekday())  # assuming week starts on Monday
#             end = start + timedelta(days=6)
#             queryset = queryset.filter(created_at__date__gte=start, created_at__date__lte=end)

#         elif filter_option == 'today':
#             # اليوم الحالي
#             queryset = queryset.filter(created_at__date=today)

#         return queryset  # إعادة مجموعة النتائج المصفاة بعد تطبيق الفلتر









from django.http import JsonResponse
from django.views import View
from user_agents import parse
from geoip2.database import Reader
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # X-Forwarded-For can contain multiple IPs, the first is the client's IP
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip

class RecordVisitorView(View):
    def get(self, request):
        # تحليل معلومات وكيل المستخدم
        user_agent_string = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_string)
        device_type = 'Desktop' if user_agent.is_pc else 'Mobile' if user_agent.is_mobile else 'Tablet'
        os_family = user_agent.os.family
        browser = user_agent.browser.family

        # الحصول على عنوان IP
        # ip_address = get_client_ip(request)
        # ip_address = '41.235.53.21'
        ip_address = '66.242.64.1'

        # Get browser fingerprint
        browser_fingerprint = get_browser_fingerprint(request)


     # Use cookies for tracking
        user_cookie = request.COOKIES.get('user_cookie')
        if not user_cookie:
            # Create new cookie if not exists
            user_cookie = get_random_string(32)
   

        # استخدام GeoIP لتحديد الموقع
        geo_info = {}
        try:
            with Reader(settings.GEOIP_PATH) as reader:
                response = reader.city(ip_address)
                geo_info = {
                'country': response.country.name,
                'country_iso_code': response.country.iso_code,
                'state': response.subdivisions.most_specific.name,
                'state_iso_code': response.subdivisions.most_specific.iso_code,
                'region': response.continent.name,  
                'city': response.city.name,
                'postal_code': response.postal.code,
                'latitude': response.location.latitude,
                'longitude': response.location.longitude,
                'timezone': response.location.time_zone,
                'continent': response.continent.name,
                'continent_iso_code': response.continent.code,
                }
        except Exception as e:
            logger.error(f"GeoIP lookup failed for IP {ip_address}: {e}")
            geo_info = {'error': str(e)}  # Return the exception message

        # استخراج معلمات UTM من رابط الطلب
        utm_source = request.GET.get('utm_source')
        utm_medium = request.GET.get('utm_medium')
        utm_campaign = request.GET.get('utm_campaign')
    
        # referrer = request.META.get('HTTP_REFERER')
    
        # if referrer:
        #  if 'facebook.com' in referrer:
        #     source = 'Facebook'
        #  elif 'twitter.com' in referrer:
        #     source = 'Twitter'
        # # أضف المزيد من الشروط حسب الحاجة
        #  else:
            # source = 'Other'
        
        # احفظ مصدر الزيارات كما تراه مناسبًا
        # request.session['referrer'] = source



        if utm_source:
         # حفظ هذه المعلومات في الجلسة
         request.session['utm_source'] = utm_source
         request.session['utm_medium'] = utm_medium
         request.session['utm_campaign'] = utm_campaign

 


        # بناء الاستجابة
        response_data = {
            'geo_info': geo_info,
            'device_type': device_type,
            'os': os_family,
            'browser': browser,
            'browser_fingerprint': browser_fingerprint,
            'cookie': user_cookie,
            'info': '.',
            'Comingـfrom': utm_source,
            'Advertising_Platform': utm_medium,
            'Campaign_Name': utm_campaign,
            'referrer info': '.',
            # 'referrer': source,


        }
        return JsonResponse(response_data)




# https://yourdomain.com/?utm_source=facebook&utm_medium=social&utm_campaign=spring_sale
# https://yourdomain.com/?utm_source=twitter&utm_medium=social&utm_campaign=spring_sale
# https://yourdomain.com/?utm_source=linkedin&utm_medium=social&utm_campaign=spring_sale

	# •	utm_source: مصدر الحملة (مثل facebook, twitter, google).
	# •	utm_medium: وسيلة الحملة (مثل cpc, social, email).
	# •	utm_campaign: اسم الحملة التسويقية (مثل spring_sale, launch).

 

from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    # استخراج معلمات UTM من رابط الطلب
    utm_source = request.GET.get('utm_source')
    utm_medium = request.GET.get('utm_medium')
    utm_campaign = request.GET.get('utm_campaign')
    
    if utm_source:
        # حفظ هذه المعلومات في الجلسة
        request.session['utm_source'] = utm_source
        request.session['utm_medium'] = utm_medium
        request.session['utm_campaign'] = utm_campaign

        # بناء الاستجابة
        response_data = {
            'utm_source': utm_source,
            'utm_medium': utm_medium,
            'utm_campaign': utm_campaign,
        }
        return JsonResponse(response_data)
    
    # إذا لم تكن معلمات UTM موجودة، إرجاع 'none' كقيمة في قاموس
    return JsonResponse({'result': 'none'})






 
 


import hashlib
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from django.shortcuts import render

# Helper to anonymize IP
def anonymize_ip(ip_address):
    parts = ip_address.split('.')
    parts[-1] = '0'  # Replace last part with 0 for anonymity
    return '.'.join(parts)

# Helper to get browser fingerprint (simply an example)
def get_browser_fingerprint(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    accept_lang = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    hash_input = f'{user_agent}{accept_lang}{get_random_string(5)}'
    return hashlib.sha256(hash_input.encode()).hexdigest()

# Middleware to handle tracking
def tracking_middleware(get_response):
    def middleware(request):
        # Anonymize IP
        ip_address = anonymize_ip(request.META.get('REMOTE_ADDR', '0.0.0.0'))
        
        # Use cookies for tracking
        user_cookie = request.COOKIES.get('user_cookie')
        if not user_cookie:
            # Create new cookie if not exists
            user_cookie = get_random_string(32)
        
        # Get browser fingerprint
        browser_fingerprint = get_browser_fingerprint(request)
        
        # Add to session or log data anonymously for analytics
        request.session['user_data'] = {
            'ip': ip_address,
            'cookie': user_cookie,
            'browser_fingerprint': browser_fingerprint,
        }
        response = get_response(request)
        response.set_cookie('user_cookie', user_cookie, max_age=365*24*60*60)  # Set cookie for 1 year
        return response



    return middleware

# View to handle user consent for cookies
def consent_view(request):
    if request.method == 'POST':
        response = JsonResponse({'status': 'Consent received'})
        response.set_cookie('consent', 'yes', max_age=365*24*60*60)
        return response
    return render(request, 'consent.html')


 




# # views.py أو أي ملف مناسب في مشروعك
# from .models import HashedIP
# from .utils import generate_salt, hash_ip

# def process_user_ip(ip):
#     # البحث عن الحاش الموجود مسبقاً
#     existing = HashedIP.objects.all()
#     for record in existing:
#         if hash_ip(ip, record.salt) == record.hashed_ip:
#             return True  # المستخدم موجود مسبقاً

#     # إذا لم يكن موجوداً، قم بإنشاء سجل جديد
#     salt = generate_salt()
#     hashed = hash_ip(ip, salt)
#     HashedIP.objects.create(hashed_ip=hashed, salt=salt)
#     return False  # المستخدم جديد













# # middleware.py
# from django.utils.deprecation import MiddlewareMixin
# from .views import process_user_ip

# class IPHashMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         ip = get_client_ip(request)
#         if ip:
#             user_exists = process_user_ip(ip)
#             if user_exists:
#                 # قم باتخاذ الإجراء المناسب، مثل تسجيل الدخول التلقائي أو تخصيص المحتوى
#                 pass
#             else:
#                 # المستخدم جديد، يمكنك تخصيص تجربة مختلفة له
#                 pass

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


# # settings.py
# MIDDLEWARE = [
#     # ... الميدلويرات الأخرى
#     'your_app.middleware.IPHashMiddleware',
# ]


# views.py

# from django.shortcuts import render
# from .models import TrafficSource

# def record_visit(request):
#     # الحصول على UTM parameters من الطلب باستخدام GET
#     utm_source = request.GET.get('utm_source')
#     utm_medium = request.GET.get('utm_medium')
#     utm_campaign = request.GET.get('utm_campaign')
#     # الحصول على عنوان URL الحالي للصفحة التي زارها المستخدم
#     visit_url = request.build_absolute_uri()

#     # إذا كان هناك أي من UTM parameters، نقوم بتخزين البيانات في قاعدة البيانات
#     if utm_source or utm_medium or utm_campaign:
#         TrafficSource.objects.create(
#             utm_source=utm_source,
#             utm_medium=utm_medium,
#             utm_campaign=utm_campaign,
#             visit_url=visit_url
#         )

#     # العودة إلى الصفحة المطلوبة أو تقديم الرد المناسب
#     return render(request, 'home.html')  # يجب تعديل هذا حسب الصفحة التي تريد عرضها


# views.py

# from django.shortcuts import render
# from .models import TrafficSource
# from django.db.models import Count

# def report(request):
#     # الحصول على ملخص البيانات، عد الزيارات لكل مصدر، وسيلة، وحملة
#     report_data = TrafficSource.objects.values('utm_source', 'utm_medium', 'utm_campaign').annotate(total_visits=Count('id'))

#     # عرض البيانات في صفحة التقرير
#     return render(request, 'report.html', {'report_data': report_data})