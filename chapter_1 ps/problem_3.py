# uses pyttsx3 to speak out a personalized introduction 
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Self-introduction text
intro = """
Hello everyone! first of all thankyou for giving me this opportunity to introduce myself .
My name is Yash Pandit. I am from Aligarh 
I am a student and I am passionate about learning new technologies.
currently i am pourshuing my B.tech from Acharya Narendra Dev University in Computer science engg.
I enjoy programming, problem-solving, and exploring engineering concepts.
Thank you for listening to my introduction.
"""

# Convert text to speech
engine.say(intro)
engine.runAndWait()