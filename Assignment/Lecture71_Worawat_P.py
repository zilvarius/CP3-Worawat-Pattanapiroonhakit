menuList = []
priceList = []

def  showBill():
    totalPrice = 0
    print("************* Food Detail ***************")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total price : ",totalPrice, "THB")

while True:
    menuName = input("Please enter menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()