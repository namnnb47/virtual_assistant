import speech_recognition
from datetime import date, datetime
import pyttsx3

robot_mount = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm listening")
	audio = robot_ear.listen(mic)

print("Robot: ...")
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

print("You: "+you)


# Robot process
today = date.today()
current_date = today.strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%H hour %M minutes %s seconds")


if you == "":
    robot_brain = "Robot: I can't hear you, try again"
elif you == "bye":
	robot_brain = "Robot: Bye teacher"
elif you == "hi siri":
    robot_brain = "Robot: Hi teacher"
elif you == "time":
    robot_brain = "Robot: "+ current_time
elif you == "Today":
    robot_brain = "Robot: Today is " + current_date
else: 
    robot_brain = "Robot: I'm good"

print(robot_brain)


robot_mount.say(robot_brain)
robot_mount.runAndWait()