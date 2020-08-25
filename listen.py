import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

print("You: "+you)

if you == "":
    robot_brain == "I can't hear you, try again"
elif you == "hello":
    robot_brain == "Hello teacher"
elif you == "today":
    robot_brain = "monday"
else: 
    robot_brain = "I'm good"

print(robot_brain)