import math
from extras import move
import bullets
import random as r

spuds = []

class Robot ():
    
    def __init__(self, x, y, color, speed, fireRate, wallWidth, wallHeight):
        
        #initialise position variables
        
        self.x = x
        self.y = y
        self.angle = r.randrange(360)
        self.speedMax = speed
        self.speed = 0
        self.fireRate = fireRate * 100
        self.color = color
        self.score = 0
        
        self.wallWidth = wallWidth
        self.wallHeight = wallHeight
        
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
        accel = 0.1
        if forward > reverse and self.speed< self.speedMax:
            self.speed+= accel
        elif forward < reverse and self.speed > 0-self.speedMax:
            self.speed -= accel
    
        x, y = move(self.x, self.y, self.angle, self.speed)
        
        if x-20 < 0 or x+20 > self.wallWidth or y-20 < 0 or y+20 > self.wallHeight:
            self.angle += 180
        else:
            self.x = x
            self.y = y
    
    def shoot(self, trigger):
        if self.fireCounter < self.fireRate:
            self.fireCounter += 1
           
        elif trigger > 0.5:
            #creates a starting location for the bullet that is separated from the robot
            separation = 25
            x, y = move(self.x, self.y, self.angle, separation) 
            spuds.append(bullets.Bullet(x, y, self.angle, 5))
            
        
    def update (self, left, right, forward, reverse, shoot, bullets):
        
        #Turning control
        self.turn(left,right)
        
        #movement control
        self.updateLocation(forward, reverse)
        #bullets.appen
        return shoot
    def updateScore(self, value):
        self.score += value
    