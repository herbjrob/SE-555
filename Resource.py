import random as r
from extras import move, collide
from PyQt5.QtCore import Qt

class Resource ():
    
    def __init__(self, x, y, xmin, xmax, ymin, ymax, radius = 10, reward = 50):
        
        #initialise position variables
        
        self.x = x
        self.y = y
        self.color = Qt.green
        
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        
        self.reward = reward
        
        self.radius = radius
        
    def update (self,robots):
            
        # collission detection loop 
        if robots:
            for i in robots:
                if collide(self.x+self.radius/2, i.x, self.y+self.radius/2, i.y, i.radius, self.radius):
                  
                    i.updateScore(self.reward)
                    self.x = r.randint(self.xmin, self.xmax)
                    self.y = r.randint(self.ymin, self.ymax)
        