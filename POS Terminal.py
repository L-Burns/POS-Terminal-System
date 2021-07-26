import datetime
import pandas as pd

# pos_orders = open("pos_orders.txt", "a")
clock = datetime.datetime.now()
print("Lo's Concessions!")

#def login():
# employeeID = input("Enter employee ID: ")
#    if employeeID == 14787:
#        print("Welcome, Lo!")
#        print(clock)
#    else:
#        print("Invalid employee ID!")
# login()

employeeID = input("Enter employee ID: ")
print("Welcome, " + employeeID + "!")
print(clock)

menu = {'Item': ["Hamburger", "Cheeseburger", "Hotdog", "Chili Cheese Dog", "Cheese Pizza", "Pepperoni Pizza", "Nachos", "Salted Pretzel", "Popcorn", "Boxed Candy", "Bottled Soda", "Bottled Water"], 'Price': [3.00, 4.50, 3.00, 5.00, 3.50, 4.50, 6.00, 3.00, 2.50, 4.00, 3.00, 3.00]}

df = pd.DataFrame(menu)
df.index += 1
print(df)
# print(df.iloc[2-1]['Item'])
# df.at[1, 'Item'] = 3.00
# print(df.at[1, 'Item'])

order = input("What would you like? ")
total = ""
while order != "":
    order = input("What would you like? ")
    total = 0
    pos_orders = open("pos_orders.txt", "a")

    if order == 1:
        total = total + 3
#        pos_orders = open("pos_orders.txt", 'w')
        pos_orders.write("Hamburger" + '\n')
#        pos_orders.close()
    elif order == 2:
        total = total + 4.5
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Cheeseburger" + '\n')
        pos_orders.close()
    elif order == 3:
        total = total + 3.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Hotdog" + '\n')
        pos_orders.close()
#     elif order == 4:
#        total += 5.0
#        pos_orders = open("pos_orders.txt", "a+")
#        pos_orders.write("Chili Cheese Dog" + '\n')
#        pos_orders.close()
#     elif order == 5:
#        total += 3.5
#        pos_orders = open("pos_orders.txt", "a+")
#        pos_orders.write("Cheese Pizza" + '\n')
#        pos_orders.close()
#     elif order == 6:
#        total += 4.5
#        pos_orders = open("pos_orders.txt", "a+")
#        pos_orders.write("Pepperoni Pizza" + '\n')
#     elif order == 7:
#        total += 6.0
#        pos_orders = open("pos_orders.txt", "a+")
#        pos_orders.write("Nachos" + '\n')
#     elif order == 8:
#        total += 3.0
#       pos_orders = open("pos_orders.txt", "a+")
#       pos_orders.write("Salted Pretzel" + '\n')
#     elif order == 9:
#        total += 2.5
#       pos_orders = open("pos_orders.txt", "a+")
#       pos_orders.write("Popcorn" + '\n')
#     elif order == 10:
#        total += 4.0
#       pos_orders = open("pos_orders.txt", "a+")
#       pos_orders.write("Boxed Candy" + '\n')
#     elif order == 11:
#        total += 3.0
#       pos_orders = open("pos_orders.txt", "a+")
#       pos_orders.write("Bottled Soda" + '\n')
#     elif order == 12:
#        total += 3.0
#       pos_orders = open("pos_orders.txt", "a+")
#       pos_orders.write("Bottled Water" + '\n')
#       pos_orders.close()
    else:
        print("Your total is: " + str(total))
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write(" Total: " + str(total) + '\n')
        pos_orders.close()





