valid = False
while not valid:
    try:
        n = int(input("enter a number"))
        while n%3 == 0:
            print("bye")
        valid = True
    except ValueError:
        print("invalid")
