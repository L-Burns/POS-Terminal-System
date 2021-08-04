import datetime
import pandas as pd

pos_orders = open("pos_orders.txt", "a")
clock = datetime.datetime.now()
print("Lo's Concessions!")


employeeID = input("Enter employee ID: ")
print("Welcome, " + employeeID + "!")
print(clock)

menu = {'Item': ["Hamburger", "Cheeseburger", "Hotdog", "Chili Cheese Dog", "Cheese Pizza", "Pepperoni Pizza", "Nachos", "Salted Pretzel", "Popcorn", "Boxed Candy", "Bottled Soda", "Bottled Water"], 'Price': [3.00, 4.50, 3.00, 5.00, 3.50, 4.50, 6.00, 3.00, 2.50, 4.00, 3.00, 3.00]}

df = pd.DataFrame(menu)
df.index += 1
print(df)

question = input("Are you ready to order? ")
total = 0

while question == 'yes' or 'y':
    pos_orders = open("pos_orders.txt", "a")
    order = int(input("What would you like? "))

    if order == 1:
        print("If you're done ordering, press 0.")
        total = total + 3.0
        pos_orders = open("pos_orders.txt", 'a')
        pos_orders.write("Hamburger" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 2:
        print("If you're done ordering, press 0.")
        total = total + 4.5
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Cheeseburger" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 3:
        print("If you're done ordering, press 0.")
        total = total + 3.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Hotdog" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 4:
        print("If you're done ordering, press 0.")
        total += 5.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Chili Cheese Dog" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 5:
        print("If you're done ordering, press 0.")
        total += 3.5
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Cheese Pizza" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 6:
        print("If you're done ordering, press 0.")
        total += 4.5
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Pepperoni Pizza" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 7:
        print("If you're done ordering, press 0.")
        total += 6.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Nachos" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 8:
        print("If you're done ordering, press 0.")
        total += 3.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Salted Pretzel" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 9:
        print("If you're done ordering, press 0.")
        total += 2.5
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Popcorn" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 10:
        print("If you're done ordering, press 0.")
        total += 4.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Boxed Candy" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 11:
        print("If you're done ordering, press 0.")
        total += 3.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Bottled Soda" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 12:
        print("If you're done ordering, press 0.")
        total += 3.0
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Bottled Water" + '\n')
        pos_orders.close()
        print(total)
        continue
    elif order == 0:
        print(total)
        pos_orders = open("pos_orders.txt", "a+")
        pos_orders.write("Total: ")
        pos_orders.write(str(total))
        pos_orders.write('\n')
        pos_orders.write('\n')
        pos_orders.close()
        break






