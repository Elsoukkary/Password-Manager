import random
import time
import tkinter as tk

# Creating Function
def generate():
    box.delete(0, tk.END)
    box.config(font = ("Arial", 8), width = 30)
    random.shuffle(Characters)
    value = charlen.get()
    value = int(value)
    passw = Characters[0 : value]

    box.insert(0, passw) 



#Setting Characters
Characters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P","A", "S", "D", "F", "G", "H", "J", "K", "L",
           "Z", "X", "C", "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
           "d", "f", "g", "h", "j", "k", "l","z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5",
           "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "{", "[", "}", "]", ";", ":", "'", "|", ",", ".", "<", ">", "/", "?", "~", "`"]


# Create Window
root = tk.Tk()
root.config(bg = "green")
root.geometry("400x200")
root.title("Password Generator")
root.iconbitmap('Icon.ico')


# Creating Tkinter Objects
title = tk.Label(root, text = "Password Generator", anchor = "center", font = ("Arial", 26), fg = "white", 
    padx = 40, pady = 10, bg = "green")
box = tk.Entry(root, width = 27, borderwidth = 5, bg = "white", fg = "green", justify="center",
    font = ("Arial", 10))
create = tk.Button(root, text = "Generate Password", bg = "white", fg = "green", font = ("Arial", 15), pady = 10,
    command = generate)
box.insert(0, "*****")
charlen = tk.IntVar()
charlen.set(16)
menu  =tk.OptionMenu(root, charlen, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
menu.config(bg="white", fg="green", font = ("Arial", 10))
menu["menu"].config(bg="white", fg="green", font = ("Arial", 10))

# Placing Tkinter Objects
title.grid(row = 0, column = 0, columnspan = 3)
box.grid(row = 1, column = 1, pady = 10, ipady = 3)
create.grid(row = 2, column = 1)
menu.grid(row = 1, column = 2, ipady = 3, ipadx = 3)


# Mainloop
root.mainloop()



