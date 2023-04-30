from django.shortcuts import render
import os
import speech_recognition as sr
import moviepy.editor as mp
from moviepy.editor import *
from gtts import gTTS
import time
import re

def index(request):
   if request.method == 'POST':
      
      # Load the video file
      clip = mp.VideoFileClip(f'{os.getcwd()}/video2.mp4')

      # Extract the audio from the video
      audio = clip.audio

      # Save the audio to a temporary file
      audio.write_audiofile("temp.wav")

      r = sr.Recognizer()
      with sr.AudioFile(f'{os.getcwd()}/temp.wav') as source:
         audio = r.record(source)
      text = r.recognize_google(audio)
      var = ''.join(text)
      text1 = var.replace('first name','Ankit')
      text2 = text1.replace('company name','Devtrust')

      # Choose language and create audio file
      language = 'en'
      tts = gTTS(text=text2, lang=language) 

      # Save audio file
      tts.save('updated_audio.mp3')

      # Play audio file
      os.system('updated_audio.mp3')
      video = mp.VideoFileClip(f'{os.getcwd()}/video2.mp4')

      # Load audio file
      audio = mp.AudioFileClip('updated_audio.mp3')

      # Replace audio in video
      video = video.set_audio(audio)

      # Save updated video
      video.write_videofile('new_video.mp4')

   return render(request,'index.html')