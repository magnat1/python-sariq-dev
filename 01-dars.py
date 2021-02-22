# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:33:26 2021

@author: hp
"""

#print("Hello world")
#print(4**3)

#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#yosh = 2021 - yil
#print("Siz " , yosh ," yoshda ekansiz")


#b_son = int(input("Birinchi sonni kiriting:"))
#i_son = int(input("Ikkinchi sonni kiriting:"))
#add = b_son + i_son
#multiple = b_son * i_son


#LISTLAR BILAN ISHLASH;
#hayvonlar = ["it","mushuk","sigir","ot","quyon","echki","sigir"]
#hayvonlar.append("qo'y")
#hayvonlar.insert(0,"toy")
#del hayvonlar[1]
#hayvonlar.remove("sigir")
#print(hayvonlar)

#LISTLARNI SARTIROVKA QILISH;
#cars = ["mercedez-benz","volvo","tayota","audi","bmw","tesla"]
#cars.sort()
#cars.sort(reverse = True)
#print(cars)
#print(sorted(cars))
#cars.reverse()
#print(cars)
#print(sorted(cars,reverse=True))

#RANGE SINTAKSISI;
#sonlar = list(range(0,10))
#print(sonlar)
#toq_sonlar = list(range(1,11,2))
#print(toq_sonlar)
#juft_sonlar = list(range(0,11,2))
#print(juft_sonlar)

#LISTLARNI KESISH;
#cars = ["bmw","audi","merc","bugatti","mazda","kia"]
#print(cars[0:3]) # 0-indeksdan 3-elementgacha chiqaradi 
#print(cars[2:5]) # 2-indexdan 5-elementgacha chiqaradi
#print(cars[:3]) # 0-indeksdan 3-elementgacha chiqaradi
#print(cars[1:]) # 1-indeksdan oxirigacha chiqaradi

#LISTLARDAN NUSXA OLISH;
#my_cars = cars[:]
#my_cars.append("slaom")
#print(my_cars)
#print(cars)

#FOR TSIKLI

#sonlar = list(range(11))
#sonlar_kv = []
#for son in sonlar:
#    sonlar_kv.append(son**2)
#print(sonlar)
#print(sonlar_kv)   

#friends = []
#print("5ta yaqin do'stingizni kiriting!")
#for n in range(5):
#    friends.append(input(f"{n+1}-do'stingizni ismini kiriting:"))
#print(friends)    

#ismlar = ["Ali","Vali","Suhrob","Hasan","Sobir"]
#for n in ismlar:
#    print("Sahifamizga xush kelibsiz ", n)
#print("Kod",len(ismlar), "marta takrorlandi")  


#IF ELSE Tushunchasi
#ism = input("Ismingizni kiriting:\n")
#if ism.lower() !="ali":
#    print(f"Uzr {ism.title()}, biz Alini kutayapmiz")
#else :
#    print("Salom Ali")

#login = input("Login parol kiriting: ")
#if len(login) <=5:
#    print("Login 5harfdan uzun bo'lishi kerak!")

#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2021 - yil < 18:
#    print(f"Yoshingiz {2020 - yil}da ekan")
#    print("Kirish mumkin emas!")
#else :
#    print("Xush kelibsiz!")  

#x ,y = 50,20
#print("x>y") if x>y else print(x<y)   

#menu = ["osh","somsa","kabob","shashlik","norin"]
#buyurtma = ["osh","somsa","manti","shashlik"]

#if buyurtma:
#    for taom in buyurtma:
#        if taom in menu:
#            print(f"Menyuda {taom} bor")
#        else :
#            print(f"Kechirasiz, menyuda {taom} yo'q")
#else :
#    print("Savatcha bo'sh")

#mahsulotlar = ["banan","uzum","shaftoli","olma","anor","nok","o'rik",
#"limon","xurmo","anjir"]
#savat = []

#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))
    
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else :
#        print(f"Kechirasiz,do'konda {mahsulot} yo'q")


mahsulotlar = ["banan","uzum","shaftoli","olma","anor","nok","o'rik",
"limon","xurmo","anjir"]
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))
    
bor_mahsulotlar = []
mavjud_emas = []
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else :
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print(f"Kechirasiz, do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
if bor_mahsulotlar:
    print(f"Do'konimizda siz so'ragan quyidagi mahsulotlar bor:")
    for mahsulot in bor_mahsulotlar:
        print(mahsulot)
        
#son = int(input("Istalgan butun son kiriting:"))
#for n in range(2,11):
#    if  (son % n == 0):
#        print(f"{son} soni {n} songa qoldiqsiz bo'linadi va javob {son/n} chiqadi")


#Xatolar bilan ishlash

        
        
        