from tkinter import *
from tkinter import colorchooser

window = Tk()

button = Button(window, text="버튼을 클릭하세요")
button.pack()

# button["fg"] = "yellow"
# button["bg"] = "green"

# button["fg"] = "#254194"
# button["bg"] = "#4287f5"

color = colorchooser.askcolor()
button["fg"] = color[1]
color = colorchooser.askcolor()
button["bg"] = color[1]

window.mainloop()