print("-------------------------------------------")
print("    Welcome to Zilva Shop         ")
print("-------------------------------------------")

a = input("Username : ")
b = input("Password : ")
t = "THB"

if a == "Zilva" and b == "1234":
    print("Log in Successful !!!")
    print("-------------------------------------------")
    print("                Product List               ")
    print("-------------------------------------------")
    print("1.Case          1,500 ",t)
    print("2.Cpu           6,500 ", t)
    print("3.Mainboard     5,500 ", t)
    print("4.Harddisk      3,500 ", t)
    print("5.Graphic Card  7,500 ", t)
    p = input("Which is you want to buy?(1-5)")
    amount = int(input("How many do you want?"))
    n = "Piece"
    if p == "1" :
        print("Your order is Case         : ",amount,n,"Total",1500*amount,t )
    elif p == "2" :
        print("Your order is Cpu          : ",amount,n,"Total", 6500*amount,t )
    elif p == "3" :
        print("Your order is Mainboard    : ",amount,n,"Total", 5500*amount,t )
    elif p == "4" :
        print("Your order is Harddisk     : ",amount,n,"Total", 3500*amount,t )
    elif p == "5" :
        print("Your order is Graphic Card : ",amount,n,"Total", 7500*amount,t )
    else:
        print("Please come back Later")
    print("Thanks you.See you next time.")
else:
    print("Log in Failed")