#speech nicognition : nhận dạng giọng nói 
#mình nói vào máy tính trả lại 
import speech_recognition as sr
import pyttsx3
robot_ear = sr.Recognizer()
with sr.Microphone() as mic:
    # mic = sr.MicroPhone()
    # dùng with sẽ bật mic lên nghe , nghe xong tăt
    print("Robot: I am Listening ")
    audio = robot_ear.listen(mic) #nghe = mic 
try:
    # nếu lỗi thì except xử lí 
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print(you)



