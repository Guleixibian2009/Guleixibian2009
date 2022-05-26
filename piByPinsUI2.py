import pygame, math, random
import sys

print('''
This is a Python program to get the approximate value of PI. It simulated the Buffon's needle problem by dropping 1000 needles.
(With GUI this time!!!)
Here we go...
''')

lineYlist = [48, 96, 144, 192, 240, 288, 336, 384, 432, 480]

def inRange(n : int, start : int, end : float) -> bool:
    return start <= n <= end if end >= start else end <= n <= start

pygame.init()
screen = pygame.display.set_mode((1000,528))

class Sprite:
    def __init__(self):
        self.coordinates = None
    def coords(self):
        return self.coordinates

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class ParaLine(Sprite):
    def __init__(self, y: int) -> None:
        Sprite.__init__(self)
        self.y1 = self.y2 = y
        self.coordinates = Coords(0, y, 1000, y)
        ### Create line

class Needle(Sprite):
    def __init__(self) -> None:
        Sprite.__init__(self)
        self.x1 = random.randint(0, 1000)
        self.y1 = random.randint(0, 528)
        self.angle = random.randint(0, 180)
        
        if inRange(self.angle, 0, 90):
            self.x2 = self.x1 - math.cos(math.radians(90 - self.angle)) * 24
        elif inRange(self.angle, 91, 180):
            self.x2 = self.x1 + math.cos(math.radians(self.angle - 90)) * 24

        if inRange(self.angle, 0, 90):
            self.y2 = self.y1 - math.sin(math.radians(90 - self.angle)) * 24
        elif inRange(self.angle, 91, 180):
            self.y2 = self.y1 + math.sin(math.radians(self.angle - 90)) * 24

        self.name = None #####

    def checkCollide(self) -> bool:
        for lineY in lineYlist:
            if inRange(lineY, self.y1, self.y2):
                ### Red
                return True
            else:
                pass

    def checkInside(self) -> bool:
        return True if inRange(self.x2, 0, 1000) and inRange(self.y2, 0, 528) else False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))

    color = 0,0,0
    width = 1
    for lineY in lineYlist:
        pygame.draw.line(screen,color,(0,lineY),(1000,lineY),width)
    

    pygame.display.update()
    pygame.display.set_caption('Buffon')
