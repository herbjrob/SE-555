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
        
    def update (self, robots):
        
        self.x, self.y = move(self.x, self.y, self.angle-180, self.speed)
        self.counter += 1
        
        if self.counter > 400:
            self.dead = True
            
        # collission detection loop 
        if robots:
            for i in robots:
                if collide(self.x, i.x, self.y, i.y, 40, 5):
                    i.dead = True
                    self.dead = True
        
    