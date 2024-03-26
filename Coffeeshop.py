#Also have one in C++ to enchance skills


print ("Hello, Welcome to the Omar's shop!\n")
print ("My name is Aal I will be assistanting you today!!\n")

name = input ("What is your name?\n")

if name == "Aal" or name == "Ali":
    print ("Not possible there could not be two of us")
    exit()

print ("Hello " + name + " nice to meet you.\n")

print ("Here is the beverages we currently have\n")

menu = "Expresso, Latte, Americano, Frappuccino, Caramel, Mocha, Black coffee"

print ("What will you like to drink?\n" + menu)

order = input ()

quantity = input ("How many would you like?: \n")

if order == "Expresso":
    price = 4.50

elif order == "Latte":
    price = 5.75

elif order == "Americano":
    price = 3.25

elif order == "Frappucino":
    price = 5.25
    want_whipped_cream = input("Will you like to add whip cream? (yes/no)\n")
    if  want_whipped_cream == "yes":
        price = 6.25
    else:
        pass

elif order ==  "Caramel":
    price = 4.35
    want_extra_caramel = input("Will you like any extra caramel? (yes/no)\n")
    if want_extra_caramel == "yes":
        price  = 5.15
    else:
        pass

elif order == "Mocha":
    price  = 5.65

elif order == "Black Coffee":
    price = 4.56

else :
    print ("Sorry we currently do not have that drink yet")
    price = 0


total = int(quantity) * price

print ("Your total will come out as $" + str(total) + " Thank you for your purchase")

