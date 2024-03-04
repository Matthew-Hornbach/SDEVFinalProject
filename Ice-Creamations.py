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

#Creates the window of the app, titles it, and makes it so you can't change the size
window = tk.Tk()
window.title("Ice-Creamations")
window.resizable(False, False)

HEIGHT = 700
WIDTH = 800

#Creates a canvas on the windows
canvas = tk.Canvas(window, height =HEIGHT, width = WIDTH, background="#00ffcc")
canvas.pack()

#Makes a frame that is a smaller border
frame = tk.Frame(window, bg = "gray")
frame.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)

iceCreamations = tk.Label(text="Ice-Creamations")

#Creates a list of the prices of each selection
price = {
    'Bowl': 3.99,
    'Cone': 2.99,
    'Taco': 4.99,
    'One Scoop': 1.99,
    'Two Scoops': 3.99,
    'Three Scoops': 5.99,
    'Vanilla': 1.99,
    'Chocolate': 1.99,
    'Strawberry': 1.99,
    "Chocolate Syrup": .99,
    "Whip Cream": 0.99,
    "Rainbow Sprinkles": 0.99,
    "Caramel": 1.99,
    "Reeses Cups": 1.99,
    "None": 0.00
}

"""Background image"""
backgroundImage = tk.PhotoImage(file = r"C:\\Users\\matth\\OneDrive\\Documents\\Software Development\\Final Project\\icecreambackground.png")
backgroundLabel = tk.Label(frame, image = backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

#Creates the order_report function so it takes the selections from the
#radioButtons and puts it into the text area
def order_report():
    orderReport.config(state=tk.NORMAL)
    orderReport.delete(1.0,tk.END)
    dishReport = i.get()
    orderReport.insert(tk.END,"Your Ice-Creamation", "underline")
    dishPrice = price.get(dishReport, 0)
    orderReport.insert(tk.END,f"\nDish: {dishReport} - ${dishPrice:.2f}")
    scoopsReport = s.get()
    scoopsPrice = price.get(scoopsReport, 0)
    orderReport.insert(tk.END,f"\nScoops: {scoopsReport} - ${scoopsPrice:.2f}")
    flavorReport = f.get()
    flavorPrice = price.get(flavorReport, 0)
    orderReport.insert(tk.END,f"\nFlavor: {flavorReport} - ${flavorPrice:.2f}")
    toppingsReport = t.get()
    toppingsPrice = price.get(toppingsReport, 0)
    orderReport.insert(tk.END,f"\nToppings: {toppingsReport} - ${toppingsPrice:.2f}")
    orderReport.insert(tk.END,"\n")
    orderReport.insert(tk.END,"\nTotal Cost", "underline")
    subTotalPrice = dishPrice + scoopsPrice + flavorPrice + toppingsPrice
    orderReport.insert(tk.END,f"\nSub Total: ${subTotalPrice:.2f}")
    taxPrice = (dishPrice + scoopsPrice + flavorPrice + toppingsPrice) * .2
    orderReport.insert(tk.END,f"\nTax: ${taxPrice:.2f}")
    totalPrice = (dishPrice + scoopsPrice + flavorPrice + toppingsPrice) + taxPrice
    orderReport.insert(tk.END,f"\nTotal: ${totalPrice:.2f}")
    orderReport.config(state=tk.DISABLED)

# Define a custom font
custom_font = tkFont.Font(family="Helvetica", size=12)

#Creates a button to print out your order with the selections and prices
orderButton = tk.Button(frame, text= 'Order Ice Cream', relief = 'solid',  bg = "white", fg = "black", activebackground = "black", activeforeground = "white", command = order_report)
orderButton.place(relx=.05, rely=.55, relwidth=.3, relheight=.3)

#Creates the text box where the order will go
orderReport = tk.Text(frame, height = 12, width = 30, bg = "#FFFF99", state = "disabled")
orderReport.place(relx=.4, rely=.5, relwidth=.55, relheight=.4)
orderReport.config(state=tk.NORMAL)
orderReport.insert(tk.END, "\n\n\n\n\n\n\tPlease Customize Your Ice-Cream", "bold",)

# Apply formatting to specific parts of the text using tags
orderReport.tag_configure("underline", underline=True)
orderReport.tag_configure("bold", font=tkFont.Font(weight="bold"))
orderReport.tag_configure("italic", font=tkFont.Font(slant="italic"))

"""Start of dish portion"""

#Makes a label that shows you what dishware you can choose
dishwareLabel = tk.Label(frame, text="Dish", relief = 'solid')
dishwareLabel.place(relx = 0, rely = 0, relwidth = 0.15, relheight = 0.1)

#Makes the variable a string and sets the selection of the buttons to none
i = tk.StringVar()
i.set(None)

#Creates the bowl button
bowl =  tk.Radiobutton(frame, text = "Bowl", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Bowl", variable=i)
bowl.place(relx = 0, rely = .1, relwidth = 0.15, relheight = 0.1)

#Creates the cone button
cone = tk.Radiobutton(frame, text = "Cone", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Cone",variable= i)
cone.place(relx = 0, rely = 0.2, relwidth = 0.15, relheight = 0.1)

#Creates the taco button
taco = tk.Radiobutton(frame, text = "Taco", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Taco",variable= i)
taco.place(relx = 0, rely = 0.3, relwidth = 0.15, relheight = 0.1)

"""End of dish portion"""


"""Start of scoop amount portion"""

#Makes the variable a string and sets the selection of the buttons to none
s = tk.StringVar()
s.set(None)

#Makes a label that shows you what amount of scoops you can choose
scoopsLabel = tk.Label(frame, text="Scoops", relief = 'solid')
scoopsLabel.place(relx = .2, rely = 0, relwidth = 0.15, relheight = 0.1)

#Creates the One Scoop radioButton
oneScoop = tk.Radiobutton(frame, text = "One Scoop", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="One Scoop",variable= s)
oneScoop.place(relx = .2, rely = 0.1, relwidth = 0.15, relheight = 0.1)

#Creates the Two Scoop radioButton
twoScoop = tk.Radiobutton(frame, text = "Two Scoops", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Two Scoops",variable= s)
twoScoop.place(relx = .2, rely = 0.2, relwidth = 0.15, relheight = 0.1)

#Creates the Three Scoop radioButton
threeScoop = tk.Radiobutton(frame, text = "Three Scoops", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Three Scoops",variable= s)
threeScoop.place(relx = .2, rely = 0.3, relwidth = 0.15, relheight = 0.1)

"""End of scoop amount portion"""

#Makes the variable a string and sets the selection of the buttons to none
f = tk.StringVar()
f.set(None)

#Makes a label that shows you what flavor you can choose
scoopsLabel = tk.Label(frame, text="Flavor", relief = 'solid')
scoopsLabel.place(relx = .4, rely = 0, relwidth = 0.15, relheight = 0.1)

#Creates the Vanilla radioButton
vanilla = tk.Radiobutton(frame, text = "Vanilla", relief = 'solid', bg = "#F3E5AB", fg = "black", activebackground = "black", activeforeground = "white", value="Vanilla",variable= f)
vanilla.place(relx = .4, rely = 0.1, relwidth = 0.15, relheight = 0.1)

#Creates the Chocolate radioButton
chocolate = tk.Radiobutton(frame, text = "Chocolate", relief = 'solid', bg = "#955743", fg = "black", activebackground = "black", activeforeground = "white", value="Chocolate",variable= f)
chocolate.place(relx = .4, rely = 0.2, relwidth = 0.15, relheight = 0.1)
#Creates the Strawberry radioButton
strawberry = tk.Radiobutton(frame, text = "Strawberry", relief = 'solid', bg = "#FF85EC", fg = "black", activebackground = "black", activeforeground = "white", value="Strawberry",variable= f)
strawberry.place(relx = .4, rely = 0.3, relwidth = 0.15, relheight = 0.1)

"""Start of toppings portion"""

#Makes the variable a string and sets the selection of the buttons to none
t = tk.StringVar()
t.set(None)

#Makes a label that shows you what toppings you can choose
toppingsLabel = tk.Label(frame, text="Toppings", relief = 'solid')
toppingsLabel.place(relx = .6, rely = 0, relwidth = 0.4, relheight = 0.1)

#Creates the Chocolate Syrup radioButton
chocolateSyrup = tk.Radiobutton(frame, text = "Chocolate\nSyrup", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Chocolate Syrup",variable= t)
chocolateSyrup.place(relx = .6, rely = 0.1, relwidth = 0.2, relheight = 0.1)
#Creates the Chocolate Sprinkles radioButton
chocolateSprinkles = tk.Radiobutton(frame, text = "Whip Cream", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Whip Cream",variable= t)
chocolateSprinkles.place(relx = .6, rely = 0.2, relwidth = 0.2, relheight = 0.1)

#Creates the Rainbow Sprinkles radioButton
rainbowSprinkles = tk.Radiobutton(frame, text = "Rainbow\nSprinkles", relief = 'solid', fg = "black", activebackground = "black", activeforeground = "white", value="Rainbow Sprinkles",variable= t)
rainbowSprinkles.place(relx = .6, rely = 0.3, relwidth = 0.2, relheight = 0.1)

#Creates the Caramel radioButton
caramel = tk.Radiobutton(frame, text = "Caramel", relief = 'solid',  bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Caramel",variable= t)
caramel.place(relx = .8, rely = 0.1, relwidth = 0.2, relheight = 0.1)
#Creates the Reeses Cups radioButton
reesesCups = tk.Radiobutton(frame, text = "Reeses Cups", relief = 'solid', bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="Reeses Cups",variable= t)
reesesCups.place(relx = .8, rely = 0.2, relwidth = 0.2, relheight = 0.1)
#Creates the None radioButton
none = tk.Radiobutton(frame, text = "None", relief = 'solid',  bg = "white", fg = "black", activebackground = "black", activeforeground = "white", value="None",variable= t)
none.place(relx = .8, rely = 0.3, relwidth = 0.2, relheight = 0.1)

#Calls to the mainloop function to start the application
window.mainloop()