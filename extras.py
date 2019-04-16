import math

def move (xin, yin, angle, speed):
    x = xin + math.cos(angle*math.pi/180) * speed
    y = yin + math.sin(angle*math.pi/180) * speed 
    return x, y

def collide(x1, x2, y1, y2, r1, r2):
    #using some pythagoras to determine if objects have collided
    if (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) < (r1+r2)*(r1+r2):
        return True
    else:
        return False