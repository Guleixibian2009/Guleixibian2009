# -*-Coding:UTF-8-*-

# Preparing and Vars
import math, random, time
from tkinter import *

print('''This is a Python program to get the approximate value of PI. It simulated the Buffon's needle problem by dropping 1000 needles.
(With GUI this time!!!)
Here we go...
''')

lineYlist = [48, 96, 144, 192, 240, 288, 336, 384, 432, 480]

def inRange(n : int, start : int, end : float) -> bool:
    return start <= n <= end if end >= start else end <= n <= start

# Init the tkinter window
class Game:
    def __init__(self) -> None:
        self.tk = Tk()
        self.tk.title("Simulate Buffon's needle problem")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=1000, height=528, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.running = True
        self.total = 0

    def mainloop(self) -> None:
        while self.running:
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

class Sprite:
    def __init__(self, game):
        self.game = game
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
    def __init__(self, game: Game, y: int) -> None:
        Sprite.__init__(self, game)
        self.y1 = self.y2 = y
        self.coordinates = Coords(0, y, 1000, y)
        game.canvas.create_line(self.coordinates.x1, self.coordinates.y1, self.coordinates.x2, self.coordinates.y2, fill="black")

class Needle(Sprite):
    def __init__(self, game: Game) -> None:
        Sprite.__init__(self, game)
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

        self.name = game.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

    def checkCollide(self, game: Game) -> bool:
        for lineY in lineYlist:
            if inRange(lineY, self.y1, self.y2):
                game.canvas.itemconfig(self.name, fill="red")
                game.total += 1
                return True
            else:
                pass

    def checkInside(self) -> bool:
        return True if inRange(self.x2, 0, 1000) and inRange(self.y2, 0, 528) else False
                

g = Game()
drawnLine = 0
collidedline = 0
for lineY in lineYlist:
    paraLine = ParaLine(g, lineY)
while drawnLine < 1000:
    needle = Needle(g)
    collided = needle.checkCollide(g)
    inside = needle.checkInside()
    if collided and inside:
        drawnLine += 1
        collidedline += 1
    elif (not collided) and inside:
        drawnLine += 1
    elif not inside:
        g.canvas.itemconfig(needle.name, fill='whitesmoke')

print(1000 / collidedline)
def on_closing():
    g.running = False

g.tk.protocol("WM_DELETE_WINDOW", on_closing)
g.mainloop()
