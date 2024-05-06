from googletrans import Translator
from gtts import gTTS
import os 
import pygame

import speech_recognition as sr
import pyttsx3
robot_ear = sr.Recognizer()
with sr.Microphone() as mic:
    # mic = sr.MicroPhone()
    # dùng with sẽ bật mic lên nghe , nghe xong tăt
    print("Robot: I am Listening ")
    audio = robot_ear.listen(mic) #nghe = mic 
    # audio = robot_ear.record(mic,duration=3)
    try:
    # nếu lỗi thì except xử lí 
    # trả lại phần mình nói 
        # you = robot_ear.recognize_google(audio,language="vi-VN")
        you = robot_ear.recognize_google(audio)
        print("You -->: {}".format(you))
    except:
        you = ""
print(you)
# Khởi tạo pygame
pygame.init()
if you =="":
    robot_brain = "I can't hear you, try again."
elif you == "hello":        
    robot_brain = "Hello Đình Phước."
elif you == "today":
    robot_brain = "Hôm nay là thứ Bảy."
elif you == "Bật đèn led":
    robot_brain = "Bật đèn thành công."
else:
    robot_brain = 'Hello Đình Phước đẹp trai nhất hành tinh'
        
print(robot_brain)
    
    # Tạo tệp âm thanh từ văn bản
tts = gTTS(text=robot_brain, lang='vi')
audio_file = f"{i}.mp3"
tts.save(audio_file)
    
# Phát âm thanh bằng pygame
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()
    
# Chờ cho âm thanh phát xong
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)