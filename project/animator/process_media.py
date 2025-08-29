
# process_media.py

import sys
import os
import subprocess

# def animate_image(image_path, audio_path, output_video_path):
#     # خطوة 1: تحويل الصورة إلى فيديو ثابت
#     video_path = image_path.rsplit('.', 1)[0] + '.mp4'
#     subprocess.call([
#         'ffmpeg', '-y', '-loop', '1', '-i', image_path, '-c:v', 'libx264',
#         '-t', '5', '-pix_fmt', 'yuv420p', video_path
#     ])

#     # خطوة 2: استخدام First Order Motion Model لتحريك الفيديو
#     animated_video_path = 'animated_temp.mp4'
#     subprocess.call([
#         'python', 'scripts/first_order_motion/first_order_motion.py',
#         '--source', video_path,
#         '--output', animated_video_path
#     ])

#     # خطوة 3: استخدام Wav2Lip لمزامنة الشفاه مع الصوت
#     final_video_path = output_video_path
#     subprocess.call([
#         'python', 'scripts/wav2lip/wav2lip.py',
#         '--face', animated_video_path,
#         '--audio', audio_path,
#         '--outfile', final_video_path
#     ])

#     # تنظيف الملفات المؤقتة
#     os.remove(video_path)
#     os.remove(animated_video_path)

# if __name__ == "__main__":
#     if len(sys.argv) != 4:
#         print("Usage: python process_media.py <image_path> <audio_path> <output_video_path>")
#         sys.exit(1)
    
#     image = sys.argv[1]
#     audio = sys.argv[2]
#     output = sys.argv[3]
#     animate_image(image, audio, output)


import sys
from moviepy.editor import VideoFileClip, AudioFileClip

def process_media(image_path, audio_path, animated_video_path):
    # يمكنك إضافة معالجة الفيديو هنا باستخدام MoviePy
    # على سبيل المثال، دمج الصورة والصوت في فيديو:
    video_clip = VideoFileClip(image_path)
    audio_clip = AudioFileClip(audio_path)

    # دمج الصوت مع الفيديو
    final_video = video_clip.set_audio(audio_clip)

    # كتابة الفيديو الناتج إلى المسار المحدد
    final_video.write_videofile(animated_video_path, codec='libx264')

if __name__ == "__main__":
    # تأكد من تلقي المعلمات من سطر الأوامر
    if len(sys.argv) != 4:
        print("Usage: python process_media.py <image_path> <audio_path> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    audio_path = sys.argv[2]
    animated_video_path = sys.argv[3]

    process_media(image_path, audio_path, animated_video_path)