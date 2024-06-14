# CLOCK PROGRAM
import time
from tkinter import *



def update():
    time_string = time.strftime("%I:%M:%S %p") 
    time_label.config(text=time_string)  

    day_string = time.strftime("%A")  # display day of the week
    day_label.config(text=day_string)

    date_string = time.strftime("%B %d, %Y")  # display date of the week
    date_label.config(text=date_string)

   
    window.after(1000, update)  


window = Tk()
window.title("Digital Clock")
time_label = Label(window, font=("Arial", 50), fg="#00ff00", bg="Black")
time_label.pack()

day_label = Label(window, font=("Consolas", 25))
day_label.pack()

date_label = Label(window, font=("Consolas", 30))
date_label.pack()

update()  
window.mainloop()
