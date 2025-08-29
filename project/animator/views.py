 # pip install djangorestframework opencv-python dlib

# في مجلد backend/
# pip install django djangorestframework opencv-python dlib corsheaders
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
import subprocess
from animator.models import *
from .serializers import * 
 
 




# class MediaUploadViewSet(viewsets.ModelViewSet):
#     queryset = MediaUpload.objects.all()
#     serializer_class = MediaUploadSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             media = serializer.save()
#             # مسار الصورة والصوت
#             image_path = os.path.join(settings.MEDIA_ROOT, media.image.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, media.audio.name)
#             animated_video_path = os.path.join(settings.MEDIA_ROOT, 'animated', f'animated_{media.id}.mp4')

#             # استدعاء سكريبت بايثون لمعالجة الفيديو
#             subprocess.call(['python', 'process_media.py', image_path, audio_path, animated_video_path])

#             # تحديث نموذج MediaUpload بمسار الفيديو
#             media.animated_video = f'animated/animated_{media.id}.mp4'
#             media.save()

#             return Response({'animated_video_url': media.animated_video}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


# import sys
# from moviepy.editor import VideoFileClip, AudioFileClip

# def process_media(image_path, audio_path, animated_video_path):
#     # يمكنك إضافة معالجة الفيديو هنا باستخدام MoviePy
#     # على سبيل المثال، دمج الصورة والصوت في فيديو:
#     video_clip = VideoFileClip(image_path)
#     audio_clip = AudioFileClip(audio_path)

#     # دمج الصوت مع الفيديو
#     final_video = video_clip.set_audio(audio_clip)

#     # كتابة الفيديو الناتج إلى المسار المحدد
#     final_video.write_videofile(animated_video_path, codec='libx264')

# if __name__ == "__main__":
#     # تأكد من تلقي المعلمات من سطر الأوامر
#     if len(sys.argv) != 4:
#         print("Usage: python process_media.py <image_path> <audio_path> <output_path>")
#         sys.exit(1)

#     image_path = sys.argv[1]
#     audio_path = sys.argv[2]
#     animated_video_path = sys.argv[3]

#     process_media(image_path, audio_path, animated_video_path)






# import os
# import subprocess
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings
# from .models import MediaUpload
# from .serializers import MediaUploadSerializer


# class MediaUploadViewSet(viewsets.ModelViewSet):
#     queryset = MediaUpload.objects.all()
#     serializer_class = MediaUploadSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             media = serializer.save()
#             # مسار الصورة والصوت
#             image_path = os.path.join(settings.MEDIA_ROOT, media.image.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, media.audio.name)
#             animated_video_path = os.path.join(settings.MEDIA_ROOT, 'animated', f'animated_{media.id}.mp4')

#             # تأكد من وجود المجلد للملفات المتحركة
#             animated_directory = os.path.join(settings.MEDIA_ROOT, 'animated')
#             if not os.path.exists(animated_directory):
#                 os.makedirs(animated_directory)

#             # تحقق من وجود ملفات الصورة والصوت
#             if not os.path.exists(image_path):
#                 return Response({'error': f'Image file not found: {image_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("image_path")

#             if not os.path.exists(audio_path):
#                 return Response({'error': f'Audio file not found: {audio_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("audio_path")

#             # استدعاء سكريبت بايثون لمعالجة الفيديو
#             # result = subprocess.call(['python', 'process_media.py', image_path, audio_path, animated_video_path])
#             result = subprocess.call(['python', './process_media.py', image_path, audio_path, animated_video_path])

#             if result != 0:
#                 return Response({'error': 'Failed to process media.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             print("process_media")
#             # تحديث نموذج MediaUpload بمسار الفيديو
#             media.animated_video = f'animated/animated_{media.id}.mp4'
#             media.save()

#             return Response({'animated_video_url': media.animated_video}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# import os
# import subprocess
# from django.conf import settings
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MediaUpload
# from .serializers import MediaUploadSerializer

# class MediaUploadViewSet(viewsets.ModelViewSet):
#     queryset = MediaUpload.objects.all()
#     serializer_class = MediaUploadSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             media = serializer.save()
#             # مسار الصورة والصوت
#             image_path = os.path.join(settings.MEDIA_ROOT, media.image.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, media.audio.name)
#             animated_video_path = os.path.join(settings.MEDIA_ROOT, 'animated', f'animated_{media.id}.mp4')

#             # تأكد من وجود المجلد للملفات المتحركة
#             animated_directory = os.path.join(settings.MEDIA_ROOT, 'animated')
#             if not os.path.exists(animated_directory):
#                 os.makedirs(animated_directory)

#             # تحقق من وجود ملفات الصورة والصوت
#             if not os.path.exists(image_path):
#                 return Response({'error': f'Image file not found: {image_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("image_path")

#             if not os.path.exists(audio_path):
#                 return Response({'error': f'Audio file not found: {audio_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("audio_path")

#             # استدعاء سكريبت بايثون لمعالجة الفيديو
#             process_media_path = os.path.join(os.path.dirname(__file__), 'process_media.py')
#             result = subprocess.call(['python', process_media_path, image_path, audio_path, animated_video_path])
#             if result != 0:
#                 return Response({'error': 'Failed to process media.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             print("process_media")

#             # تحديث نموذج MediaUpload بمسار الفيديو
#             media.animated_video = f'animated/animated_{media.id}.mp4'
#             media.save()

#             return Response({'animated_video_url': media.animated_video}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# import os
# import subprocess
# from django.conf import settings
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MediaUpload
# from .serializers import MediaUploadSerializer

# from .process_media import process_media

# class MediaUploadViewSet(viewsets.ModelViewSet):
#     queryset = MediaUpload.objects.all()
#     serializer_class = MediaUploadSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             media = serializer.save()
#             # مسار الصورة والصوت
#             image_path = os.path.join(settings.MEDIA_ROOT, media.image.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, media.audio.name)
#             animated_video_path = os.path.join(settings.MEDIA_ROOT, 'animated', f'animated_{media.id}.mp4')

#             # تأكد من وجود المجلد للملفات المتحركة
#             animated_directory = os.path.join(settings.MEDIA_ROOT, 'animated')
#             if not os.path.exists(animated_directory):
#                 os.makedirs(animated_directory)

#             # تحقق من وجود ملفات الصورة والصوت
#             if not os.path.exists(image_path):
#                 return Response({'error': f'Image file not found: {image_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("image_path")

#             if not os.path.exists(audio_path):
#                 return Response({'error': f'Audio file not found: {audio_path}'}, status=status.HTTP_400_BAD_REQUEST)
#             print("audio_path")

#             # استدعاء سكريبت بايثون لمعالجة الفيديو
#             # process_media_path = os.path.join(os.path.dirname(__file__), 'process_media.py')


#             # result = subprocess.call(['python', process_media_path, image_path, audio_path, animated_video_path])
#             result = process_media( image_path, audio_path, animated_video_path)

            
#             if result != 0:
#                 return Response({'error': 'Failed to process media.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             print("process_media")

#             # تحديث نموذج MediaUpload بمسار الفيديو
#             media.animated_video = f'animated/animated_{media.id}.mp4'
#             media.save()

#             return Response({'animated_video_url': media.animated_video}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



import os
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import MediaUpload
from .serializers import MediaUploadSerializer

# استيراد دالة المعالجة من ملف process_media.py في نفس المجلد
from .process_media import process_media


class MediaUploadViewSet(viewsets.ModelViewSet):
    queryset = MediaUpload.objects.all()
    serializer_class = MediaUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            media = serializer.save()
            # مسار الصورة والصوت
            image_path = os.path.join(settings.MEDIA_ROOT, media.image.name)
            audio_path = os.path.join(settings.MEDIA_ROOT, media.audio.name)
            animated_video_path = os.path.join(settings.MEDIA_ROOT, 'animated', f'animated_{media.id}.mp4')

            # تأكد من وجود المجلد للملفات المتحركة
            animated_directory = os.path.join(settings.MEDIA_ROOT, 'animated')
            if not os.path.exists(animated_directory):
                os.makedirs(animated_directory)

            # تحقق من وجود ملفات الصورة والصوت
            if not os.path.exists(image_path):
                return Response({'error': f'Image file not found: {image_path}'}, status=status.HTTP_400_BAD_REQUEST)
            print("image_path")

            if not os.path.exists(audio_path):
                return Response({'error': f'Audio file not found: {audio_path}'}, status=status.HTTP_400_BAD_REQUEST)
            print("audio_path")

            # استدعاء الدالة لمعالجة الفيديو
            result = process_media(image_path, audio_path, animated_video_path)
            if result != 0:
                return Response({'error': 'Failed to process media.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            print("process_media")

            # تحديث نموذج MediaUpload بمسار الفيديو
            media.animated_video = f'animated/animated_{media.id}.mp4'
            media.save()

            return Response({'animated_video_url': media.animated_video}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)