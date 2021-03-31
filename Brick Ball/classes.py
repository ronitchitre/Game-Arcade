import pygame

class Block(pygame.Rect):
    def __init__(self , list_info , color , dur):
        self.list_info = list_info
        self.color = color
        self.dur = dur
    def getting_hit(self):
        try:
            self.color[0] = self.color[0] - self.dur
        except:
            pass
        try:
            self.color[1] = self.color[1] - self.dur
        except:
            pass
        try:
            self.color[2] = self.color[2] - self.dur
        except:
            pass
        if(self.color[0]<=10 and self.color[1]<=10 and self.color[2] <= 10):
            del self
class Ball(pygame.Rect):
    def __init__(self , centre , radius , magnitude , direction = [0,0] ):
        self.center = centre
        self.radius = radius
        self.direction = direction
        self.magnitude = magnitude
