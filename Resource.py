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
        
        #misc        
        self.counter = 0
        self.dead = False
        
    def update (self):
        
        if self.dead:
            self.dead = True
            
        # collission detection loop 
        if robots:
            for i in robots:
                if collide(self.x, i.x, self.y, i.y, i.radius, self.radius):
                  
                    self.dead = True
                    i.updateScore(self.reward)
        