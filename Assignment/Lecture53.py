def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

Price = int(input("add price : "))
print("Total is : ",vatCalculate(Price))