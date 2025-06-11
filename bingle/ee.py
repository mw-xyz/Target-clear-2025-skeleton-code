def checker(UserInput):
    counter = 0
    for char in UserInput:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

UserInput = ""
while UserInput != "q":
    UserInput = input("enter thingy or press q to quit: ")
    if checker(UserInput):
        print("yes")
    else:
        print("no")
