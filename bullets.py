class Bullet ():
    
    def __init__(self, x, y, angle, speed):
        
        #initialise position variables
        
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed       
        
        #misc        
        self.counter = 0
        self.dead = False
        
    def update (self):
        
        self.x, self.y = move(self.x, self.y, self.angle-180, self.speed)
        self.counter += 1
        
        if self.counter > 400:
            self.dead = True
        
    