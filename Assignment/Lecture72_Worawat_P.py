menuList = []

def  showBill():
    totalPrice = 0
    print("************* Food Detail ***************")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total price : ",totalPrice, "THB")

while True:
    menuName = input("Please enter menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])

showBill()