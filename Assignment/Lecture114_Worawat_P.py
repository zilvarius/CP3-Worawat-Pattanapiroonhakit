from typing import List
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime
import math

c = CurrencyRates()
c_code = CurrencyCodes()
base_currency = ""
second_currency = ""
day = 0

def currency_input(): #อยากทราบวิธีแก้ bug กด enter เฉยๆไม่พิมพ์อะไรเลยแล้วผ่านลูป while ไปได้
    cur_list = c.get_rates("").keys()
    print("-" * 50)
    print("Currency List : Please add your currency code !!")
    print("-" * 50)
    for curcode in cur_list:
        print(curcode, c_code.get_currency_name(curcode))
    print("-" * 50)
    print("Please add 2 currency code to analysis : ")
    base_currency = input("First Currency : ").upper()
    second_currency = input("Second Curency : ").upper()
    while base_currency and second_currency not in c.get_rates("").keys():
        print("Currency Symbol incorrect!")
        print("Add currency again : ")
        base_currency = input("First Currency : ").upper()
        second_currency = input("Second Currency : ").upper()
    return [base_currency, second_currency]

def currency_analys():
    cur_als = currency_input()
    day = int(input("How many day to analysis? (Within 30 Days)")) #ติดปัญหา debug Error เมื่อพิมพ์ตัวอักษรไม่ใช่ตัวเลข
    while day < 1 or day > 30:
         print("Sorry please add number again.")
         day = int(input("How many day to analysis? (Within 30 Days)"))
    winrate = 0
    withdraw = 0
    equal = 0
    date = datetime.datetime.now()
    for curals in range(day):
        previous_date = date - datetime.timedelta(1)
        win_tick = float(c.get_rate(cur_als[0], cur_als[1], date)) \
                   - float(c.get_rate(cur_als[0], cur_als[1], previous_date))
        if win_tick < 0:
            point = 0
            equal = 0
        elif win_tick < 1 and win_tick * 100000000000000000000 == 0.0 :
            point = 0
            equal = 1
        else:
            point = 1
            equal = 0
        date = previous_date
        previous_date = previous_date - datetime.timedelta(1)
        winrate = winrate + point
        withdraw = withdraw + equal
    print(cur_als[0], "win rate is : ",(winrate/(day-withdraw)*100), " % in",day - withdraw, "Days")
    print("Not active day  : ", withdraw, " Days")

currency_analys()





