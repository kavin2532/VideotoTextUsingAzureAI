import moviepy as mp 
import speech_recognition as sr 
import soundfile
video = mp.VideoFileClip(r"D:\WeekEndRide\videoplayback.mp4") 
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile(r"D:\WeekEndRide\videoplayback.wav") 

r = sr.Recognizer()
data, samplerate = soundfile.read(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k.wav")
soundfile.write(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k22.wav", data, samplerate, subtype='PCM_16')
audio_file = sr.AudioFile(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k22.wav")

with audio_file as source:
	audio = r.record(source)
	text = r.recognize_google(audio)
	print(text)
