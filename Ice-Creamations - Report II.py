"""
Project: Ice-Creamations_Final Project.py
Author: Matthew Hornbach
Date Last Modified: 2/22/2024
Description: The application will ask the user to pick either a cone or bowl with optional sizings. 
The application will then ask the user how many scoops of ice cream they would like and then what flavor. 
The application will then ask them what toppings they would want on their ice cream and 
finally it will give you the option to cash out or add to your order. 
"""

import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
ice_cream = []

HEIGHT = 700
WIDTH = 800

canvas = tk.Canvas(window, height =HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(window, bg = "gray")
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

iceCreamations = tk.Label(text="Ice-Creamations")

def get_dish():
    dishSelection.config(text=i.get())

# Makes a label that shows you what dishware you can choose
dishware = tk.Label(frame, text="Dish")
dishware.place(relx = 0, rely = 0, relwidth = 0.15, relheight = 0.1)

i = tk.StringVar()
i.set(None)
# Creates the bowl button
bowl =  tk.Radiobutton(frame, text = "  Bowl  ", bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Bowl", variable=i, command =get_dish)
bowl.place(relx = 0, rely = .1, relwidth = 0.15, relheight = 0.1)

# Creates the cone button
cone =  tk.Radiobutton(frame, text = "  Cone  ", bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Cone",variable= i, command =get_dish)
cone.place(relx = 0, rely = 0.2, relwidth = 0.15, relheight = 0.1)

dishSelection = tk.Label(frame, text="Dish Selection",bg = "white", fg = "black", activebackground = "black", activeforeground = "white")
dishSelection.place(relx = 0, rely = 0.3, relwidth = 0.15, relheight = 0.1)



window.mainloop()