from modulefinder import packagePathMap
from struct import pack
from tkinter import * 
from turtle import width
from PIL import ImageGrab
import io
from random import *

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=700, height=500, background="white")
tahvel.grid()

#1 eest
tahvel.create_rectangle(500,50,  260,150, fill="blue")
tahvel.create_rectangle(500,100,   260,150, fill="black")
tahvel.create_rectangle(500,200,   260,150, fill="white")

#2 bahama
tahvel.create_rectangle(25,50,  260,150, fill="#24cde0")
tahvel.create_rectangle(25,100,   260,150, fill="yellow")
tahvel.create_rectangle(25,200,   260,150, fill="#24cde0")
tahvel.create_polygon(25,50, 110,125, 25,200, fill="black")

#3 vene 
tahvel.create_rectangle(25,250,  250,300, fill="white")
tahvel.create_rectangle(25,350,   250,300, fill="red")

#1
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
k=7
x0=0
y0=0
x1=550
y1=550
for i in range(k):
    x0+=50
    y0+=50
    x1-=50
    y1-=50
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="yellow")
tahvel.grid()

ps = tahvel.postscript(colormode='color')
x1=tahvel.winfo_width()
y1=tahvel.winfo_height()

ImageGrab.grab().crop((0,0,x1,y1)).save("image.jpg")
raam.mainloop()


#2

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=400, height=400, background="white")

square_size = 50

for row in range(8):
    for col in range(8):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        if (row+col) % 2 == 0:
            color = "white"
        else:
            color = "black"
        tahvel.create_rectangle(x1, y1, x2, y2, fill=color)

tahvel.grid()

raam.mainloop()

#3
colors=["black","cyan","magenta","red","blue","gray","yellow","green","lightblue","pink","gold"]
raam2=Tk()
raam2.title("Ringi")
tahvel2=Canvas(raam2, width=600, height=600, background="white")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):
    x0+=p 
    y0+=p
    x1-=p
    y1-=p 
    tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))



tahvel2.grid()

raam2.mainloop()

raam.mainloop()
