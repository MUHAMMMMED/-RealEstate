from django.db import models
from django.utils import timezone

class Device(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class OperatingSystem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name  

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name  

class DictionarySource(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class DictionaryMedium(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class DictionaryCampaign(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class DictionaryPageTitle(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
 

class DeviceType(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='device_types')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return str(self.device)

class OS(models.Model):
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE, related_name='operating_systems')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return str(self.operating_system)

class PeakTime(models.Model):
    hour = models.IntegerField(unique=True, db_index=True)
    total_visits = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Hour {self.hour}: {self.total_visits} Visits"

class Region(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='regions')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.location.name}"

class City(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='cities')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.location.name}, {self.region.name}"
 

class Source(models.Model):
    dictionary_source = models.ForeignKey(DictionarySource, on_delete=models.CASCADE, related_name='sources')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"Source: {self.dictionary_source}, Total Visits: {self.total_visits}"

class Medium(models.Model):
    dictionary_medium = models.ForeignKey(DictionaryMedium, on_delete=models.CASCADE, related_name='media')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"Medium: {self.dictionary_medium}, Total Visits: {self.total_visits}"

class Campaign(models.Model):
    dictionary_campaign = models.ForeignKey(DictionaryCampaign, on_delete=models.CASCADE, related_name='campaigns')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"Campaign: {self.dictionary_campaign}, Total Visits: {self.total_visits}"

class Page(models.Model):
    dictionary_page_title = models.ForeignKey(DictionaryPageTitle, on_delete=models.CASCADE, related_name='pages')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)

    def __str__(self):
        return f"Page Title: {self.dictionary_page_title}, Total Visits: {self.total_visits}"

class TrafficSource(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='traffic_sources')
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE, related_name='traffic_media')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='traffic_campaigns')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='traffic_pages')

    def __str__(self):
        return f"Traffic Source from {self.source} using {self.medium} for {self.campaign} on {self.page}"
 
class Country(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='countries')
    date = models.DateField(default=timezone.now)
    total_visits = models.IntegerField(default=1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)  
    operating_system = models.ForeignKey(OS, on_delete=models.CASCADE)   
    peak_time = models.ForeignKey(PeakTime, on_delete=models.CASCADE)   
    Traffic_Source = models.ForeignKey(TrafficSource, on_delete=models.CASCADE)   

    def __str__(self):
        return str(self.location)

class UserVisit(models.Model):
    hashed_ip = models.CharField(max_length=64, unique=True)
    salt = models.CharField(max_length=16)
    user_cookie = models.CharField(max_length=255, blank=True, null=True)
    browser_fingerprint = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_visits = models.IntegerField(default=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hashed_ip} - Visits: {self.total_visits}"
    


 