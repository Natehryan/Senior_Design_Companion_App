import mysql.connector

actList = ''
image = ''
name = ''
description = ''
active = True
class Profiles(id, actList, image, name, description, active):
    def __init__(self, id, actList, image, name, description, active):
        self.id = id
        self.actList = actList
        self.image = image
        self.name = name 
        self.description = description
        self.active = active
      
    def setInactive(active):
        active = False

    def setActive(active):
        active = True
    
    def writeEntry(id, actList, image, name, description, active):
        #if it is not already there write the entry, otherwise change entry
        lines = set(open('profiles.txt').readlines())
        inLine = False
        newLine = [id, ', ', actList, ', ', image,  ', ', name,  ', ', description,  ', ', active]
    
        for line in lines:
            if str(id) in line:
                line = line.replace(newLine)
                inLine = True
        
        if inLine == False:
            with open('profiles.txt', 'a') as f:
                f.write(newLine)
                f.write('\n')
        else: 
            with open('profiles.txt', 'w') as f:
                f.write(lines)
                f.write('\n')
        
        




profiledb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = profiledb.cursor()

mycursor.execute("CREATE DATABASE Profiles")
