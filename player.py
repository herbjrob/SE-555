import math
from extras import move
import bullets
import random as r

spuds = []

class Robot ():
    
    def __init__(self, x, y, color, speed, fireRate):
        
        #initialise position variables
        
        self.x = x
        self.y = y
        self.angle = r.randrange(360)
        self.speed = speed
        self.fireRate = fireRate * 100
        self.color
        self.score = 0
        
        #control variables
     
        self.shoot = 0
        self.fireCounter = 0
        
        #misc
        self.dead = False
        
        
    def turn (self, l, r):
        
        if l> r:
            self.angle -= 1
        elif r>l:
            self.angle += 1
    
    def updateLocation (self, forward, reverse):
        
        if forward > reverse:
            self.x, self.y = move(self.x, self.y, self.angle, self.speed)
        elif forward < reverse:
            self.x, self.y = move(self.x, self.y, self.angle-180, self.speed)
        
    
    def shoot(self, trigger):
        if self.fireCounter < self.fireRate:
            self.fireCounter += 1
           
        elif trigger > 0.5:
            #creates a starting location for the bullet that is separated from the robot
            separation = 10
            x, y = move(self.x, self.y, self.angle, separation) 
            spuds.append(bullets.Bullet(x, y, self.angle, 5))
            
        
    def update (self, left, right, forward, reverse, shoot):
        
        #Turning control
        self.turn(left,right)
        
        #movement control
        self.updateLocation(forward, reverse)
        
    
    def updateScore(self, value):
        self.score += value
    