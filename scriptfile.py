import moviepy as mp 
import speech_recognition as sr 

# Load the video 
video = mp.VideoFileClip(r"D:\WeekEndRide\videoplayback.mp4") 

# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile(r"D:\WeekEndRide\videoplayback.wav") 
