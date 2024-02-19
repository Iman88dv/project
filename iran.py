# from moviepy.editor import VideoFileClip

# video_clip = VideoFileClip("D:\\python class\\7ddec3eb4b40d2e11f2d39e51a683aec44841011-1080p.mp4")

# audio_clip = video_clip.audio
# print(audio_clip)
# output_path = "D:\\python class\\new.mp3"

# print("salam")
# audio_clip.write_audiofile("D:\python class\new")

from moviepy.editor import VideoFileClip

video_clip = VideoFileClip("D:\\python class\\0e7b2b61434956fadc0183ee603f9e7a52291845-360p.mp4")

audio_clip = video_clip.audio

output_path = "C:\\Users\\ASUS\\Desktop\\New folder (3).mp3"


audio_clip.write_audiofile(output_path)