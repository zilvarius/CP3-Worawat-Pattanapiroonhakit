def login():
    userName = input("User Name : ")
    passWord = input("Password : ")
    if userName == "admin" and passWord == "1234":
        return True
    else:
        return False
def showMenu():
    print("*****************Welcome****************")
    print("1.Vat Calculator")
    print("2 Price Calculator")
def menuSelect():
    userSelected = int(input(">>>"))
    return userSelected
def vatCal(totalPrice):
    return totalPrice+(totalPrice*7/100)
def priceCal():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCal(price1+price2)


if login() == True:
    print("Log in Sucess!!")
    showMenu()
    runCal = menuSelect()
    if runCal == 1:
        priceInput = int(input("Add price : "))
        print("Total is : ",vatCal(priceInput))
    elif runCal  == 2:
        print("Total : ",priceCal())
    else:
        print("Try again..")

else:
    print("Username or Password Incorrect.")

