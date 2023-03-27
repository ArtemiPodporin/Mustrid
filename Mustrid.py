from tkinter import *

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





raam.mainloop()
