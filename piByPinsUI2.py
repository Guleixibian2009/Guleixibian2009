import pygame, math, random, time

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
        pass

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

        self.name = pygame.draw.line(screen, (0,0,0), (self.x1, self.y1), (self.x2, self.y2))

    def checkCollide(self) -> bool:
        for lineY in lineYlist:
            if inRange(lineY, self.y1, self.y2):
                pygame.draw.line(screen, (255,0,0), (self.x1, self.y1), (self.x2, self.y2))
                return True
            else:
                pass

    def checkInside(self) -> bool:
        return True if inRange(self.x2, 0, 1000) and inRange(self.y2, 0, 528) else False

    def getCoords(self) -> list[tuple()]:
        return [(self.x1, self.y1), (self.x2, self.y2)]

startPosList = []
endPosList = []
needleList = []
drawnLine = collidedline = 0
while drawnLine <= 1000:
    n = Needle()
    collided = n.checkCollide()
    inside = n.checkInside()
    coords = n.getCoords()
    if collided and inside:
        drawnLine += 1
        collidedline += 1
        startPosList.append(coords[0])
        endPosList.append(coords[1])
        needleList.append(n)
    elif (not collided) and inside:
        drawnLine += 1
        startPosList.append(coords[0])
        endPosList.append(coords[1])
        needleList.append(n)
    elif not inside:
        pass

print(1000 / collidedline)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    color = 0,0,0
    width = 1
    for lineY in lineYlist:
        pygame.draw.line(screen,color,(0,lineY),(1000,lineY),width)
    
    for x in range(1000):
        currentNeedle = needleList[x]
        startPos = startPosList[x]
        endPos = endPosList[x]
        pygame.draw.line(screen,color,startPos,endPos,width)
        if currentNeedle.checkCollide():
            pygame.draw.line(screen,(255,0,0),startPos,endPos,width)
        
    pygame.display.update()
    pygame.display.set_caption('Buffon')
