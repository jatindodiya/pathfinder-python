import pygame
from tkinter import *


root = Tk()
root.title("Start Window")
#root.iconbitmap('pyc.ico')
screen_width = root.winfo_screenwidth()-100
screen_height = root.winfo_screenheight()-100

#pygame.init()
pygame.display.set_caption("Path Finder")

mainScreen = pygame.display.set_mode([screen_width,screen_height])  #main screen object and final setup

def onsubmit():
    global start
    global end
    global st
    global ed
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    print(st)
    print(ed)
    root.quit()
    root.destroy()

#--------------------------------------------------input window---------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------



def mydelay(miliSec):                                #this function we created gives appprox delay in milisec
    i = 0
    while i < miliSec:
        pygame.time.delay(1)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = miliSec+1
                pygame.quit()


def main():
    frame.pack()
    root.mainloop()
    #text = font.render(St)
    #win.blit(text, (650, 10))
    mydelay(5000)

main()


