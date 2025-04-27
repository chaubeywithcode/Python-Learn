a = int(input("Enter a lucky number: "))

match a:
    case 1:
        print("You won a charger")
    case 3: 
        print("You won $3")
    case 6:
        print("You won camera")
    case _:
        print("Better luck next Time")