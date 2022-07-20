'''
    All utility realated function implemantation
    1. speak function
    2. speech recognition
'''
import pyttsx3


class Utility():
    def __init__(self) -> None:
        self.name = "jarvis"


    def speak(self,msg):
        self.engine = pyttsx3.init()
        self.engine.say(msg)
        self.engine.runAndWait()


    def listen(self):
        pass