import random as rd
from time import sleep
aLetter = 'ABCDEFJHIGKLMNOPQRSTUVWXYZ'
uLetter = 'abcdefjhigklmnopqrstuvwxyz'
num = '0123456789'

lenth = int(input("Введите кол-во ссылок: "))
while lenth > 0:  
    print("     ")    
    all = aLetter + uLetter + num
    a = 16
    url = "".join(rd.sample(all,  a))
    print("discord.gift/" + url)
    
    lenth = lenth - 1
sleep(5000)  