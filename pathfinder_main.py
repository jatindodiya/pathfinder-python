import pygame
from tkinter import *
import os

# -----------------------------------color define-----------------------------------------
red = (178, 34, 34)
orange = (255, 110, 0)
blue = (30, 144, 255)
pink = (255, 105, 180)
black = (0, 0, 0)
aqua = (0, 255, 255)
white = (220, 220, 220)

# -----------------------------------------------------------------------------------------
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
root = Tk()
root.title("Start Window")
# root.iconbitmap('pyc.ico')
screen_width = root.winfo_screenwidth() - 50  # screen window width
screen_height = root.winfo_screenheight() - 100  # screen window height

# --------------------------------------------------------------------------------------------
# number between 2 - 200
sizeofarr = 20
# --------------------------------------------------------------------------------------------
screen_width = screen_width - screen_width % sizeofarr
screen_height = screen_height - screen_height % sizeofarr

pygame.init()
pygame.display.set_caption("Path Finder Algorithm visualisation")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30, True)
mainScreen = pygame.display.set_mode([screen_width, screen_height + 30])  # main screen object and final setup



# ------------------------------------------------------------------------------------------------
# message box
messagebox = pygame.draw.rect(mainScreen, black, (0, screen_height, screen_width, 30))
# -------------------------------------------------------------------------------------------------

class rectangle(object):
    def __init__(self, x, y, width, height, posx, posy):
        self.x = x
        self.y = y
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = white
        self.stpoint = False
        self.edpoint = False
        self.wall = False

    def drawrect(self):
        pygame.draw.rect(mainScreen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def changecolor(self, color):
        self.color = color
        pygame.display.update()

    def start(self, color):
        self.color = color
        self.stpoint = True
        pygame.draw.rect(mainScreen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def end(self, color):
        self.color = color
        self.edpoint = True
        pygame.draw.rect(mainScreen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def path(self):
        pass


def onsubmit():
    # global st
    # global ed
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    spots[int(st[0])][int(st[1])].start(orange)
    spots[int(ed[0])][int(ed[1])].end(blue)
    print(st)
    print(ed)
    root.quit()
    root.destroy()


def displayMessage(message, fontSize, height):
    fonts = pygame.font.SysFont('comicsans', fontSize)
    text = fonts.render(message, 0, (255, 0, 0))
    mainScreen.blit(text, (200, height))
    pygame.display.update()


# ----------------------------------------------------------------------------------------------------
# this is space for grid spot


spotHeight = screen_height // sizeofarr
sizeof = screen_width // spotHeight
print(sizeofarr)
print(sizeof)
spots = [[0 for i in range(sizeofarr)] for j in range(sizeof)]
for i in range(sizeof):
    for j in range(sizeofarr):
        spots[i][j] = rectangle(i * spotHeight, j * spotHeight, spotHeight - 1, spotHeight - 1, i, j)

for row in spots:
    for spot in row:
        spot.drawrect()

# --------------------------------------------------input window------------------------------------------
frame = Frame(root)
label = Label(frame, text='Start(x,y): ')
startBox = Entry(frame)
label1 = Label(frame, text='End(x,y): ')
endBox = Entry(frame)
submit = Button(frame, text='Submit', command=onsubmit)
submit.grid(columnspan=2, row=3)
label1.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)


# ------------------------------------ Algorithms ---------------------------------------------------
def astar():
    pass


# ---------------------------------------------------------------------------------------------------

def mydelay(miliSec):          # this function we created gives appprox delay in milisec
    i = 0
    while i < miliSec:
        pygame.time.delay(1)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = miliSec + 1
                pygame.quit()


frame.pack()
root.mainloop()
run = True
while run:
    mydelay(100)
    pygame.display.update()
