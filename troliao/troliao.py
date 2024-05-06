from gtts import gTTS
import os 
import pygame
import webbrowser
import speech_recognition as sr
import pyttsx3
import antigravity
import serial
import time
# robot_ear = sr.Recognizer()
# with sr.Microphone() as mic:
#     # mic = sr.MicroPhone()
#     # dùng with sẽ bật mic lên nghe , nghe xong tăt
#     print("Robot: I am Listening ")
#     audio = robot_ear.record(mic,duration=3)
#     try:
#     # nếu lỗi thì except xử lí 
#     # trả lại phần mình nói 
#         you = robot_ear.recognize_google(audio,language="vi-VN")
#     except:
#         you = ""
# print(you)

# you = "today1"
# # Khởi tạo pygame
# pygame.init()
# if you =="":
#     robot_brain = "I can't hear you, try again."
# elif "Hello" in you:        
#     robot_brain = "Hello Đình Phước."
# elif "today" in you:
#     robot_brain = "Hôm nay là chủ nhật ."
# elif "Bật đèn led" in you:
#     robot_brain = "Bật đèn thành công."
    
# else:
#     robot_brain = 'Hello Đình Phước đẹp trai nhất hành tinh'
        
# print(robot_brain)
    
#     # Tạo tệp âm thanh từ văn bản
# tts = gTTS(text=robot_brain, lang='vi')
# audio_file = f".mp3"
# tts.save(audio_file)
    
# # Phát âm thanh bằng pygame
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play()
    
# # Chờ cho âm thanh phát xong
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
print("ngo phuoc")
DataSerial = serial.Serial('COM3',9600)
time.sleep(2)
def Serial(s):
    DataSerial.write(s.encode('utf-8'))
i=0
while i <1000:
    you = input("Nhập từ muốn nói ")
    # Khởi tạo pygame
    pygame.init()
    if you =="":
        robot_brain = "I can't hear you, try again."
    elif "Hello" in you:        
        robot_brain = "Hello Đình Phước."   
    elif "today" in you:
        robot_brain = "Hôm nay là chủ nhật ."
    elif "Bật đèn 1" in you:
        # webbrowser.open('http://192.168.100.101/1/on',new=1)
        Serial("b1")
        robot_brain = "Bật đèn 1 thành công."
    elif "Bật đèn led 1" in you:
        # webbrowser.open('http://192.168.100.101/1/on',new=1)
        Serial("b1")
        robot_brain = "Bật đèn 1 thành công."
    elif "Bật đèn led 2" in you:
        robot_brain = "Bật đèn 2 thành công"
    elif "Tắt đèn led 1" in you:
        Serial("t1")
        # webbrowser.open('http://192.168.100.101/1/off',new=1)    
        robot_brain = "Tắt đèn 1 thành công."
    elif "Tắt đèn 1" in you:
        Serial("t1")
        # webbrowser.open('http://192.168.100.101/1/off',new=1)    
        robot_brain = "Tắt đèn 1 thành công."
    elif "Tắt đèn led 2" in you:
        Serial("t1")
        robot_brain = "Tắt đèn 2 thành công"
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
    i +=1