from PIL import Image
import numpy as np

class Profiles:
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

    def getImage(self):
        return self.image
    
    def getDescription(self):
        return self.description
    
    def getName(self):
        return self.name

    def getID(self):
        return self.id
    
    def getActList(self):
        return self.actList

    def getActive(self):
        return self.active
    
    def convertImage(self, image):
        img = Image.open(image)
        array = np.array(img)

        r,g,b = np.split(array,3,axis=2)
        r=r.reshape(-1)
        g=r.reshape(-1)
        b=r.reshape(-1)

        bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
        zip(r,g,b)))
        bitmap = np.array(bitmap).reshape([array.shape[0], array.shape[1]])
        bitmap = np.dot((bitmap > 128).astype(float),255)
        im = Image.fromarray(bitmap.astype(np.uint8))
        im.save(image)

    def writeEntry(id, actList, image, name, description, active):
        #if it is not already there write the entry, otherwise change entry
        with open('profiles.txt', 'a') as f:
            f.write("")
        lines = set(open('profiles.txt').readlines())
        inLine = False
        
        newLine = [str(id), ', ', actList, ', ', str(image),  ', ', name,  ', ', description,  ', ', active]
    
        for line in lines:
            if name in line and description in line:
                line = line.replace('True', 'False')
                inLine = True
        
        if inLine == True: 
            with open('profiles.txt', 'w') as f:
                for line in lines:
                    if str(image) in line and description in line and str(active) in line:
                        line = line.replace('True', 'False')
                    f.write(line)
        
        with open('profiles.txt', 'a') as f:
            for word in newLine:
                f.write(str(word))
            f.write('\n')
           

p = Profiles(id, "whiteList", 'handsome-cheerful-man-with-happy-smile_176420-18028.png', "genericus", "for the glory of Rome", True)
#p.setImage('handsome-cheerful-man-with-happy-smile_176420-18028.png')
p.writeEntry("whiteList", p.getImage(), "genericus", "for the glory of Rome", True)