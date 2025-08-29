# utils.py

# بعد ذلك، سنقوم بإنشاء دالة لتوليد الملح وحاش عنوان الـ IP باستخدام خوارزمية SHA-256. سنستخدم مكتبة hashlib لتوليد الحاش ومكتبة os لتوليد الملح العشوائي.



import hashlib
import os

def generate_salt(length=16):
    return os.urandom(length).hex()

def hash_ip(ip, salt):
    return hashlib.sha256((ip + salt).encode('utf-8')).hexdigest()