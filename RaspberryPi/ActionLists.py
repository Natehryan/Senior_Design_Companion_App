#By: Nathaniel Ryan
#Can you tell that Python is not my primary language

# Import the required module for text 
# to speech conversion
import pyttsx3
#import face_recognition

#class of images of people belonging to certain lists, not functional
#class People:
 #   person

 # initialize Text-to-speech engine
engine = pyttsx3.init()
  


class Action:
    def __init__(self, act):
        self.act = act

#alarm class to raise alarm and inform person who triggered the alarm that they are not allowed to be there
#use text to speech and lights.
class Alarm():

    # convert this text to speech
    text = "You are Not Permitted here"
    engine.say(text)
    # play the speech
    engine.runAndWait()

#permit class for people who are allowed to be there, 
#inform them of such, then go back to patrolling without bothering them again
class Permit():
    # convert this text to speech
    text = "You are Permitted here"
    engine.say(text)
    # play the speech
    engine.runAndWait()

    

#uses text to speech to request the person to halt, not functional
class RequestThemToHalt():
    # convert this text to speech
    text = "Halt"
    engine.say(text)
    # play the speech
    engine.runAndWait()
    #wait for update from user


#Push request to app user if person is allowed to be there, not functional
class QueryUser(Action):
    action

#action class for all behaviours
class ActionList:
    #initialize the class with a dictionary of actions, all set to false
    def __init__(self):
        self.acts = {'Query':'false', 'Alarm':'false', 'RequestThemToHalt':'false', 'Permit':'false'}

    #add actions to action lists, not functional, should just update the relevant dictionary action
    def AddAction(self, act):
        self.acts[act] = 'true'

    #remove actions from action lists, not functional
    def RemoveAction(self, act):
        self.acts[act] = 'false'

    #run to perform actions from action list
    def PerformActions(self):
        #iterate through all acts in the dictionary and run the true ones
        for i in self.acts:
            if(self.acts[i] == True):
                self.acts.keys(i) #I dont actually think this will work but thats a problem for later

        

#Create 5 people, one for each plausible combination of actions
whiteList = ActionList()
blackList = ActionList()
greyList = ActionList()

whiteList.AddAction(Permit)
blackList.AddAction(Alarm)
