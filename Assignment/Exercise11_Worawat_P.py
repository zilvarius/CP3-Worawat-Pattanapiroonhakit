userInput = int(input("Added number : "))
for x in range(userInput):
    y = (userInput*2)-1
    space = 0
    sign = 0
    for i in range(y):
        if i < (userInput-1)- x or i > (userInput-1)+x and i != (userInput-1):
            space = space + 1
        else:
            sign = sign + 1
    print(" "*int(space/2),"*"*sign," "*int(space/2))