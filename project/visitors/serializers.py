# from rest_framework import serializers
# from .models import (
#     Device,
#     OperatingSystem,
#     Location,
#     DeviceType,
#     OS,
#     PeakTime,
#     Region,
#     City,
#     Country,
#     UserVisit,
# )

# class DeviceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Device
#         fields = ['id', 'name']

# class OperatingSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OperatingSystem
#         fields = ['id', 'name']

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['id', 'name']

# class DeviceTypeSerializer(serializers.ModelSerializer):
#     device = DeviceSerializer()  # Nested serializer

#     class Meta:
#         model = DeviceType
#         fields = ['id', 'device', 'date', 'total_visits']

# class OSSerializer(serializers.ModelSerializer):
#     operating_system = OperatingSystemSerializer()  # Nested serializer

#     class Meta:
#         model = OS
#         fields = ['id', 'operating_system', 'date', 'total_visits']

# class PeakTimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PeakTime
#         fields = ['id', 'hour', 'total_visits', 'date']

# class RegionSerializer(serializers.ModelSerializer):
#     location = LocationSerializer()  # Nested serializer

#     class Meta:
#         model = Region
#         fields = ['id', 'location', 'date', 'total_visits']

# class CitySerializer(serializers.ModelSerializer):
#     location = LocationSerializer()  # Nested serializer
#     region = RegionSerializer()  # Nested serializer

#     class Meta:
#         model = City
#         fields = ['id', 'location', 'region', 'date', 'total_visits']

# class CountrySerializer(serializers.ModelSerializer):
#     location = LocationSerializer()  # Nested serializer
#     region = RegionSerializer()  # Nested serializer
#     device_type = DeviceTypeSerializer()  # Nested serializer
#     operating_system = OSSerializer()  # Nested serializer
#     peak_time = PeakTimeSerializer()  # Nested serializer

#     class Meta:
#         model = Country
#         fields = ['id', 'location', 'date', 'total_visits', 'region', 'device_type', 'operating_system', 'peak_time']

# class UserVisitSerializer(serializers.ModelSerializer):
#     country = CountrySerializer()  # Nested serializer

#     class Meta:
#         model = UserVisit
#         fields = ['id', 'hashed_ip', 'salt', 'user_cookie', 'browser_fingerprint', 'created_at', 'total_visits', 'country']


from rest_framework import serializers
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

# سيريالايزر لجهاز
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device  # النموذج المستخدم
        fields = ['id', 'name']  # الحقول التي سيتم تضمينها

# سيريالايزر لنظام التشغيل
class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem  # النموذج المستخدم
        fields = ['id', 'name']  # الحقول التي سيتم تضمينها

# سيريالايزر للموقع
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # النموذج المستخدم
        fields = ['id', 'name']  # الحقول التي سيتم تضمينها

# سيريالايزر لنوع الجهاز
class DeviceTypeSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()  # سيريالايزر متداخل

    class Meta:
        model = DeviceType  # النموذج المستخدم
        fields = ['id', 'device', 'date', 'total_visits']  # الحقول التي سيتم تضمينها

# سيريالايزر لنظام تشغيل الجهاز
class OSSerializer(serializers.ModelSerializer):
    operating_system = OperatingSystemSerializer()  # سيريالايزر متداخل

    class Meta:
        model = OS  # النموذج المستخدم
        fields = ['id', 'operating_system', 'date', 'total_visits']  # الحقول التي سيتم تضمينها

# سيريالايزر لأوقات الذروة
class PeakTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakTime  # النموذج المستخدم
        fields = ['id', 'hour', 'total_visits', 'date']  # الحقول التي سيتم تضمينها

# سيريالايزر للمنطقة
class RegionSerializer(serializers.ModelSerializer):
    location = LocationSerializer()  # سيريالايزر متداخل

    class Meta:
        model = Region  # النموذج المستخدم
        fields = ['id', 'location', 'date', 'total_visits']  # الحقول التي سيتم تضمينها

# سيريالايزر للمدينة
class CitySerializer(serializers.ModelSerializer):
    location = LocationSerializer()  # سيريالايزر متداخل
    region = RegionSerializer()  # سيريالايزر متداخل

    class Meta:
        model = City  # النموذج المستخدم
        fields = ['id', 'location', 'region', 'date', 'total_visits']  # الحقول التي سيتم تضمينها

# سيريالايزر للبلد
class CountrySerializer(serializers.ModelSerializer):
    location = LocationSerializer()  # سيريالايزر متداخل
    region = RegionSerializer()  # سيريالايزر متداخل
    device_type = DeviceTypeSerializer()  # سيريالايزر متداخل
    operating_system = OSSerializer()  # سيريالايزر متداخل
    peak_time = PeakTimeSerializer()  # سيريالايزر متداخل

    class Meta:
        model = Country  # النموذج المستخدم
        fields = ['id', 'location', 'date', 'total_visits', 'region', 'device_type', 'operating_system', 'peak_time']  # الحقول التي سيتم تضمينها

# سيريالايزر لزيارة المستخدم
class UserVisitSerializer(serializers.ModelSerializer):
    country = CountrySerializer()  # سيريالايزر متداخل

    class Meta:
        model = UserVisit  # النموذج المستخدم
        fields = ['id', 'hashed_ip', 'salt', 'user_cookie', 'browser_fingerprint', 'created_at', 'total_visits', 'country']  # الحقول التي سيتم تضمينها