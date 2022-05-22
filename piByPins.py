# -*-Coding:UTF-8-*-
import math, random

lineYlist = [12, 24, 36, 48, 60, 72, 84, 96, 108]

def inRange(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start

print('''This is a Python program to get the approximate value of PI. It simulated the Buffon's needle problem 10 times by dropping 100000 needles each time.
Here we go...
''')

class Pin:
    def __init__(self) -> None:
        # [0]: angle [1]: y1 [2]: y2
        self.coords = [random.randint(0, 180), random.randint(0, 120), None]
        self.angle = self.coords[0]

        if inRange(self.angle, 0, 45):
            self.coords[2] = self.coords[1] - math.sin(math.radians(90 - self.coords[0])) * 6
        elif inRange(self.angle, 46, 90):
            self.coords[2] = self.coords[1] - math.sin(math.radians(90 - self.coords[0])) * 6
        elif inRange(self.angle, 91, 135):
            self.coords[2] = self.coords[1] + math.sin(math.radians(self.coords[0] - 90)) * 6
        elif inRange(self.angle, 136, 180):
            self.coords[2] = self.coords[1] + math.sin(math.radians(self.coords[0] - 90)) * 6
        else:
            print('Some error occured when calculating y2!')

    def checkCollide(self, y1: int, y2: int) -> bool:
        self.collided = [False, False, False, False, False, False, False, False, False]
        count = 0
        for lineY in lineYlist:
            if inRange(lineY, y1, y2):
                self.collided[count] = True
            else:
                self.collided[count] = False
            count += 1

        if True in self.collided:
            return True
        else: 
            return False

for i in range(10):
    totalCollided = 0
    for x in range(100000):
        pin = Pin()
        ifCollided = pin.checkCollide(pin.coords[1], pin.coords[2])
        # print(pin.coords[0], pin.coords[1], pin.coords[2], ifCollided)
        if ifCollided:
            totalCollided += 1

    print(100000 / totalCollided)