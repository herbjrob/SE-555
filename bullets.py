from extras import move, collide
class Bullet ():
    
    def __init__(self, x, y, angle, speed, radius = 2):
        
        #initialise position variables
        
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed 
        self.radius = radius
        
        #misc        
        self.counter = 0
        self.dead = False
        
    def update (self, robots):
        
        self.x, self.y = move(self.x, self.y, self.angle, self.speed)
        self.counter += 1
        
        if self.counter > 400:
            self.dead = True
            
        # collission detection loop 
        if robots:
            for i in robots:
                if collide(self.x, i.x, self.y, i.y, i.radius, self.radius):
                    i.dead = True
                    self.dead = True
        
    