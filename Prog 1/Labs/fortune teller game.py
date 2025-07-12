want_fortune = True
print("\nWelcome to the online fortune teller game!\n")
while want_fortune:
    color = input("\nPick a color (red, green, yellow, and blue): ")
    if color == "red":
        number = int(input("Pick a number, either 1 or 2: "))
        if number == 1:
            print("\nYou will get an A on your next exam.")
        elif number == 2:
            print("\nYou will meet someone who will become a very close friend.")
        else:
            print("\nWrong number! Try again...")
    elif color == "green":
        number = int(input("Pick a number, either 3 or 4: "))
        if number == 3:
            print("\nYou will find love soon.")
        elif number == 4:
            print("\nYour crush will ask you out tomorrow.")
        else:
            print("Wrong number! Try again...")
    elif color == "blue":
        number = int(input("Pick a number, either 5 or 6: "))
        if number == 5:
            print("\nYou will soon realize your purpose.")
        elif number == 6:
            print("\nYou will unlock your fullest potential and change the world.")
        else:
            print("\nWrong number! Try again...")
    elif color == "yellow":
        number = int(input("Pick a number, either 7 or 8: "))
        if number == 7:
            print("\nThe rest of your week will go as you wish.")
        elif number == 8:
            print("\nA long-awaited event will finally occur today.")
        else:
            print("\nWrong number! Try again...")
    else:
        print("\nWrong color! Try again...")

    cont = input("\nWould you like to play again? (yes/no) ")
    if cont == "yes":
        want_fortune = True
    elif cont == "no":
        want_fortune = False
        print("Ok bye then.")
    else:
        print("\nWrong option! Try again...")
