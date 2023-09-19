# Import the required module for text 
# to speech conversion
import pyttsx3
  
# initialize Text-to-speech engine
engine = pyttsx3.init()
  
# convert this text to speech
text = "Halt"
engine.say(text)
# play the speech
engine.runAndWait()

# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)