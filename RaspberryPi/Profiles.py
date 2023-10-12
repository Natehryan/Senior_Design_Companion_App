import mysql.connector

class Profiles(actList, image, name):
    def __init__(self, actList, image, name):
        self.actList = actList
        self.image = image
        self.name = name



profiledb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = profiledb.cursor()

mycursor.execute("CREATE DATABASE Profiles")
