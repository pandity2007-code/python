# install an external module and use it perform an operration of your intersest
# we use an external modulr which name is = pyttsx3
# we can install the module from the terminal and use it .

import pyttsx3
pyttsx3.speak("I will speak this text")
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("jay shree ram")
engine.runAndWait()