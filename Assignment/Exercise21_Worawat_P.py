from tkinter import *
import math

def LeftClickButton(event):
    result = ()
    bmi = float(textBoxWeight.get())/math.pow((float(textBoxHeight.get())/100),2)
    if bmi >= 30.0:
        result = "อ้วนมาก"
    elif 25.0 <= bmi < 30 :
        result = "อ้วน"
    elif 23.0 <= bmi < 25.0:
        result = "น้ำหนักเกิน"
    elif 23.0 <= bmi < 25.0:
        result = "น้ำหนักเกิน"
    elif 18.6 <= bmi < 23.0:
        result = "น้ำหนักปกติ เหมาะสม"
    else:
        result = "ผอมเกินไป"
    labelResult.configure(text=result)

mainWindow = Tk()
labelHeight = Label(mainWindow, text = "ส่วนสูง (Cm)").grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow, text = "น้ำหนัก (Kg)").grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
BmiCalculator = Button(mainWindow,text="Calculate")
BmiCalculator.grid(row=2,column=0)
BmiCalculator.bind('<Button-1>',LeftClickButton)
labelResult = Label(mainWindow, text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
mainWindow.mainloop()

