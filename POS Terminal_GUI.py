from tkinter import *
from tkinter import ttk

pos = Tk()
pos.title("Lo's Concessions")
pos.geometry("1920x1080")

# making the function for the command option of the food button


def hb_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.00)
    order_panel.insert(END, "Hamburger \t\t\t\t3.00\n")


def cb_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(4.50)
    order_panel.insert(END, "Cheeseburger \t\t\t\t4.50\n")


def hd_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.00)
    order_panel.insert(END, "Hotdog \t\t\t\t3.00\n")


def ccd_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(5.00)
    order_panel.insert(END, "Chili Cheese Dog \t\t\t\t5.00\n")


def cpizza_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.50)
    order_panel.insert(END, "Cheese Pizza \t\t\t\t3.50\n")


def ppizza_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(4.50)
    order_panel.insert(END, "Pepperoni Pizza \t\t\t\t4.50\n")


def nachos_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(6.00)
    order_panel.insert(END, "Nachos \t\t\t\t6.00\n")


def pretzel_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.00)
    order_panel.insert(END, "Salted Pretzel \t\t\t\t3.00\n")


def popcorn_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(2.50)
    order_panel.insert(END, "Popcorn \t\t\t\t2.50\n")


def candy_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(4.00)
    order_panel.insert(END, "Boxed Candy \t\t\t\t4.00\n")


def soda_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.00)
    order_panel.insert(END, "Bottled Soda \t\t\t\t3.00\n")


def water_order_taking():
    total = 0.00
    price = lambda a: a
    total += price(3.00)
    order_panel.insert(END, "Bottled Water \t\t\t\t3.00\n")


def clear_button():
    order_panel.delete(1.0, END)


receipt = open("receipts.txt", "a")

# this function will grab the order from the order panel and write it to the receipts text file


def print_receipt():
    receipt.write(order_panel.get(1.0, END))
    receipt.close()
    order_panel.delete(1.0, END)
# this allows another order to be taken after the previous order has been completed
    pos.mainloop()

# opening all the photos for the buttons


hamburger = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\burger.png").subsample(2, 2)
cheeseburger = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\cheeseburger.png").subsample(2, 2)
hotdog = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\hotdog.png").subsample(2, 2)
ccdog = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\chilidog.png").subsample(5, 5)
cpizza = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\cpizza.png").subsample(4, 4)
ppizza = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\ppizza.png").subsample(2, 2)
nachos = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\nachos.png").subsample(2, 2)
pretzel = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\pretzel.png").subsample(6, 6)
popcorn = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\popcorn.png").subsample(2, 2)
candy = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\candy.png").subsample(6, 6)
soda = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\soda.png").subsample(2, 2)
water = PhotoImage(file=r"D:\PycharmProjects\PersonalProjects\water.png").subsample(2, 2)

button = Button(pos, text="Hamburger", image=hamburger, compound=TOP, bg="#FFFFFF", command=hb_order_taking).grid(row=2, column=1, columnspan=1, padx=5, pady=5)
button = Button(pos, text="Cheeseburger", image=cheeseburger, compound=TOP, bg="#FFFFFF", command=cb_order_taking).grid(row=2, column=3, columnspan=1)
button = Button(pos, text="Hotdog", image=hotdog, compound=TOP, bg="#FFFFFF", command=hd_order_taking).grid(row=2, column=5, columnspan=1)
button = Button(pos, text="Chili Cheese Dog", image=ccdog, compound=TOP, bg="#FFFFFF", command=ccd_order_taking).grid(row=2, column=7, columnspan=1)
button = Button(pos, text="Cheese Pizza", image=cpizza, compound=TOP, bg="#FFFFFF", command=cpizza_order_taking).grid(row=3, column=1, columnspan=1)
button = Button(pos, text="Pepperoni Pizza", image=ppizza, compound=TOP, bg="#FFFFFF", command=ppizza_order_taking).grid(row=3, column=3, columnspan=1)
button = Button(pos, text="Nachos", image=nachos, compound=TOP, bg="#FFFFFF", command=nachos_order_taking).grid(row=3, column=5, columnspan=1)
button = Button(pos, text="Salted Pretzel", image=pretzel, compound=TOP, bg="#FFFFFF", command=pretzel_order_taking).grid(row=3, column=7, columnspan=1)
button = Button(pos, text="Popcorn", image=popcorn, compound=TOP, bg="#FFFFFF", command=popcorn_order_taking).grid(row=4, column=1, columnspan=1)
button = Button(pos, text="Boxed Candy", image=candy, compound=TOP, bg="#FFFFFF", command=candy_order_taking).grid(row=4, column=3, columnspan=1)
button = Button(pos, text="Bottled Soda", image=soda, compound=TOP, bg="#FFFFFF", command=soda_order_taking).grid(row=4, column=5, columnspan=1)
button = Button(pos, text="Bottled Water", image=water, compound=TOP, bg="#FFFFFF", command=water_order_taking).grid(row=4, column=7, columnspan=1)


clear_button = Button(pos, text="Clear", command=clear_button, fg="#FFFFFF",  bg="#FF0800", activebackground="#B31717", width="25", height="5", font="Impact 18").grid(row=5, column=1, columnspan=2)

done_button = Button(pos, text="Done", command=print_receipt, fg="#FFFFFF", bg="#00FF2A", activebackground="#08A813", width="25", height="5", font="Impact 18").grid(row=5, column=5, columnspan=2)

order_panel = Text(pos)
order_panel.grid(row=2, rowspan=3, column=9)

# undo_button = Button(pos, text="Undo", fg="#000000", command=order_panel.edit_undo).grid(row=9, column=1)

pos.mainloop()
