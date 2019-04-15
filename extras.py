import math

def move (xin, yin, angle, speed):
    x = xin + math.cos(angle*math.pi/180) * speed
    y = yin + math.sin(angle*math.pi/180) * speed 
    return x, y