# num1 = int(input('write num'))
# num2 = int(input('write num'))

# a = num1 + num2
# b = num1 - num2
# c = num1 * num2
# d = num1 / num2

# print ('plus', a)
# print ('minus', b)
# print ('umnoj', c)
# print ('delenie', d)

# a = 30
# b = 60 

# s = a*b

# print("area of ​​a rectangle is equal to =",s)


# a = int(input('znachenie a '))
# c = int(input('znachenie c '))
# b = c**2 - a**2
# print(b**0.5)



# number = int(input("Введите число: "))

# if number % 2 == 0:
#     print(f"{number} - четное число")
# else:
#     print(f"{number} - нечетное число")



# num_c = int(input("Введите количество чисел: "))

# total = 0 

# for i in range(num_c):
#     num = float(input(f"Введите число {i + 1}: "))
#     total += num

# print(f"Сумма введенных чисел: {total}")

# word = "Привет"
# for letter in word:
#     print(letter)


# x = input("enter int")
# print("input data type ", type(x))

# if x.isdigit() == True:
#     x = int(x)
#     print("true data type", type(x))
# else:
#         print("x is not number")

# age = 22
# height = 177
# age = age + 1
# height = height + 1
# print("age ", age,"height ", height)


# a = int(input("number "))
# n = int(input("stepen "))

# c = a ** n

# print(c)


# a = int(input("number "))

# if a % 2 == 0:
#     print('четное число ')
# else:
#     print('не четное число')


# a = 1
# b = 1.0

# print(a == b)
# print(a is b)

# print('a' in 'avc')
# print('v' in 'avc')
# print('d' in 'avc')


# n = 100 
# print('n = ', n)
# if 0 < n < 200:
#     print('n is between 0 and 200')


# x = True
# y = False

# print(x and y)
# print(x or y)
# print(not y)
# print(not x)

# num = int(input("enter an int "))
# result = ( num >= 0 and num <= 0 and num %2 == 0)
# print('is the... ', result)


# a = int(input("number "))
# result = ( a >= 100 and a <= 300 and a % 2 ==0)
# print(result)


# year = int(input())

# result = ( year % 4 ==0 and year % 100 != 0) or year % 400 == 0
# print(result)

# a = int(input())

# res = (a >= 100 and a < 1000)

# print(res)

# num = int(input())

# res = (num % 5 == 0)

# print(res)

# age = int(input())

# res = age >= 18 

# print(res)


# age = int(input())

# if age < 20:
#     print('ur discount') 
# else :
#     print('ur too old')

# num = int(input())

# if num % 3 == 0 :
#     print(f"{num} is multiple of 3")
# else:
#     print(f"{num} is not multiple of 3")

# pas = "hello"

# s = input()

# if pas == s :
#     print("ur welcome")
# else:
#     print("wrong password")

# ur_score = int(input("enter ur score "))

# if ur_score > 1500:
#     print("ur master")
# if ur_score < 1500 and ur_score > 1000:
#     print("ur good")
# if ur_score < 1000:
#     print("u noob")
 
# num = int(input("enter number "))

# if num >= 0:
#     print(f"{num} is natural")
# else:
#     print(f"{num} is not natural")

# w = input("enter words ")
# word_list = w.split(',')
# print(word_list)




# n1, n2, n3 = input('ent three integers separated by ,:').split(',')
# n1, n2, n3 = int(n1), int(n2), int(n3)
# print(n1, n2, n3)


# age = int(input("enter ur age "))

# if  age < 10:
#     print("u are kid")
# if  age < 20 and age > 10:
#     print("u are youth")
# if age > 30:
#     print("u are adult")


# age = int(input("Enter ur age "))
# height = int(input("Enter ur height "))

# if age >= 5 and height >= 140:
#     print("You can eneter")
# else:
#     print("You can not eneter")

# num = int(input("ent int "))
# if num >= 0:
#     if num == 0:
#         print("its 0")
#     else:
#         print("its positive")
# else:
#     print("its negative")


# score = int(input("Enter studdent score "))

# if score >= 90 and score <= 100:
#     print("Student Grade A")
# if score >= 80 and score < 90:
#     print("Student Grade B")
# if score >= 70 and score < 80:
#     print("Student Grade C")
# if score >= 60 and score < 70:
#     print("Student Grade D")
# if score < 60:
#     print("Student Grade F")





# apple = int(500)
# grape = int(600)
# melon = int(800)
# orange = int(200)


# user_choice = int(input("Enter int 1-4 "))
# quantity = int(input("enter kg "))


# if user_choice == 1:
#     print("apple price ", apple * quantity)
# if user_choice == 2:
#     print("grape price ", grape * quantity)
# if user_choice == 3:
#     print("melon price ", melon * quantity)
# if user_choice == 4:
#     print("orange price ", orange * quantity)
# else:
#     print("error")





# vowel = "aeiou"
# ur_letter = input("check letter ")

# if ur_letter in vowel:
#     print("letter is vowel")
# else:
#     print(f"{ur_letter} is consonant")




# a = int(input("Enter int 1 "))
# b = int(input("Enter int 2 "))

# if a % b == 0:
#     print(f"{a} is a multiple {b}")
# else:
#     print(f"{a} is not a multiple {b}")





# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# choise = input("Введи 'четные' или 'нечетные' ")


# if choise == "четные" :
#     for num in num :
#         if num % 2 == 0:
#             print(num)
# elif choise == "нечетные" :
#     for num in num :
#         if num % 3 == 0 :
#             print(num)
# else:
#     print("не верный выбор")



# КОД НИЖЕ НИХЕРА НЕ ПОНЯЛ 

# num = int(input("enter the number "))

# if num <=1 :
#     is_prime = False
# elif num <= 3:
#     is_prime = True
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break


# if is_prime:
#     print(f"{num} is normal number")
# else:
#     print(f"{num} is not normal number")


# *************************
# 7.10.23
# *************************


# import random

# num = random.randrange(2)
# print(num)

# if num == 0:
#     print("орел")
# else:
#     print("решка")




# a = int(input("Введите 1 число "))
# b = int(input("Введите 2 число "))

# c = input("Введите операцию +,-,*,/ ")

# if c == "+" :
#     print('Результат' ,a + b)
# elif c == "-":
#     print('Результат' ,a - b)
# elif c == "*":
#     print('Результат' ,a * b)
# elif c == "/":
#     print('Результат' ,a / b)
# else:
#     print('Error')




# x = int(input("enter x "))
# y = int(input("enter y "))

# if x > 0 and y > 0 :
#     print("is the 1 quadrant")
# elif x < 0 and y > 0 :
#     print("is the 2 quadrant")
# elif x < 0 and y < 0 :
#     print("is the 3 quadrant")
# elif x > 0 and y < 0 :
#     print("is the 4 quadrant")
# if  x == 0:
#     print("error")


# *************************
# 11.10.23
# *************************



# print("*" * 50)
# print("Menu")
# print("Burger, Pizza, Banana")

# choice = input("enter ur choice ")

# if choice == "Burger" or choice == "burger":
#     print(f"ur choice is {choice}")
# elif choice == "Pizza" or choice == "pizza":
#     print(f"ur choice is {choice}")
# elif choice == "Banana" or choice == "banana":
#     print(f"ur choice is {choice}")



# for i in range (0,-5,-1):
#     print(i)


# s = 0
# for i in range (1,101):
#     s += i
# print("sum of num from 1 to 10 is ", s)


# print(sum(range(1,11)))



# s = int(input("enter num "))
# f = int(input("enter factorial "))

# for i in range(1, s+1):
#     f = f * i
# print(str(s)+"!", f)



# num = [11, 22, 33, 44, 55, 66]
# s = 0
# for n in num :
#     s = s + n
#     print('n = ', s)


# st = "hello"
# print(list(st))


# for i in "Hello":
#     print(i, end = " ")
# for i in "Hello":
#     print(i, end = " ")






# s = 0
# for i in range(2,101,2):
#     s += i
# print(s)



# for i in [1,2,3,4]:
#     print("i = ", i**2)


# import random
# n = random.randint(1,3)

# if n == 1:
#     c_choice = "Left"
# elif n == 2:
#     c_choice = "midle"
# elif n == 3:
#     c_choice = "right"

# user = input("left, midle, right ")

# if user == c_choice:
#     print ("its save")
# else:
#     print ("its goal")

# сделай то же самое ток с луп


# import random

# def soccer_game():
#     goals = 0  # Инициализация счета голов
#     while True:  # Начало бесконечного цикла
#         # Генерируем случайный выбор для вратаря: 1 (лево), 2 (центр), 3 (право)
#         goalkeeper_choice = random.randint(1, 3)
        
#         # Запрашиваем выбор игрока
#         player_choice = input("Выберите направление (1 - лево, 2 - центр, 3 - право) или введите 0 для выхода: ")
        
#         if player_choice == "0":
#             # Если игрок ввел 0, завершаем игру и выводим счет
#             print(f"Игра завершена. Счет: {goals} голов.")
#             break
        
#         # Проверяем, совпал ли выбор игрока с выбором вратаря
#         if int(player_choice) == goalkeeper_choice:
#             print("Сейв! Вы выбрали правильное направление.")
#         else:
#             print("Гол! Выбор игрока не совпал с выбором вратаря.")
#             goals += 1  # Увеличиваем счет голов

# # Запускаем игру
# soccer_game()

# *************************
# 14.10.23
# *************************

# i = 0 
# while i < 5:
#     print("hello")
#     i = i + 1


# n = int(input("enter a number to sum up to: "))
# s = 0
# i = 1 
# while i <=n:
#     s = s + i
#     i += 1 
# print(f'sum of 1 to {n} is {s}')

# sel = None 
# while sel not in ["scissors", "rock", "paper"]:
#     sel = input("Choose among scissors, rock, paper ")
# print(f"choosen value {sel}")



# n = -1 
# while n <=0:
#     n = int(input("enter a positive num to sum up to "))
# s = 0
# for i in range(1, n+1):
#     s = s + i 
# print(f"sum of 1 to {n} is {s}")



# import random as rd
# print(rd.random(1,100))

# import random as rd
# num = [10,20,30,40,50,60]
# print(rd.choice(num))

# st = "progaramming"

# for ch in st:
#     if ch in ('a','e', 'i','o','u'):
#         break
#     print(ch)
# print("end")

# for i in range(2,10):
#     for j in range(1,10):
#         print('{}x{} = {:2d}'.format(i, j, i*j))
#     print ()


# for i in range(2):
#     for j range(1,10):
#         print('{}x{} = {:2d}'.format(i, j, i*j))
#     print()


# a = ["scissors", "rock", "paper"]

# win = 0

# sel = None 
# while sel not in ["scissors", "rock", "paper"]:
#     sel = input("Choose among scissors, rock, paper ")
#     comp_choice = rd.choice(a)
#     print(f"Comp choice is {comp_choice}")
#     print(f"ur choice {sel}")


# if comp_choice == "rock" and sel == 'scissors'or comp_choice == "paper" and sel == 'rock' or comp_choice == "scissors" and sel == 'paper':
#     print("u lose")
# elif comp_choice == sel:
#     print("drow")
# else:
#     win += 1
#     print(f"win {win}")


# total = 0 
# answ = "yes"
# while answ == "yes":
#     num = int(input('enter the num : '))
#     total = total + num
#     answ = input('continue? (yes/no)')
# print("sum is : ", total)



# print("Guess a number between 1 to 100")
# ch = int(input("Enter number "))
# a = rd.randint(1,100)
# while a != ch :
#     if a > ch :
#         print("higher")
#     elif a < ch:
#         print("lower")
#     ch = int(input("Enter number "))
#     if a == ch:
#         print("win")
    
# num = int(input("Enter num "))

# if -6 <= num <= 6:
#     result = True
# else:
#     result = False
# print(result)


# a = int(input("Enter num a "))
# b = int(input("Enter num b "))
# c = int(input("Enter num c "))

# if a < b < c:
#     result = True
# else:
#     result = False
# print(result)

# ***18.10.23***

# h = int(input("enter height "))
# a = 0 
# days = 1

# while a <= h:
#     a = a + 7
#     if a >= h:
#         break
#     days += 1
#     a = a - 5
# print(days)




# score_list = [80, 2.3, 90, 90, 95]
# print(score_list[-1])

# pr1 = ['David Doe', 20, 1, 180.0, 100.0]
# pr2 = ['John Smith', 25, 1, 170.0, 70.0]

# pList = pr1 + pr2
# print(pList)


# a = ['a', 'b', 'c', 'd', 'e']
# a.append('f')
# print(a)



# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]
# l1.extend(l2)
# l1.append("sdafsd") #append polnostiu
# l1.extend('DSASD') #extend po bukfam
# print(l1)


# nlist = [11, 22, 33, 44, 55]
# # print(nlist)

# nlist.remove(44)
# print(nlist)


# n = nlist.pop()
# print("pop try", n)
# print(nlist)

# del nlist[3]
# print(nlist)



# alist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(alist[1:])
# print(alist[0:5])
# # print(alist[:5])
# print(alist[0::2])
# print(alist[0:4:2])
# print(alist[-7::2])

# blist = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# btuple[0] = 1

# print(btuple)

# list_1 = [3, 5, 7]
# list_2 = [2, 3, 4, 5, 6]

# for j in list_1:
#     for i in list_2:
#         a = j * i
#         print(f"{j} * {i} = {a}")

# print(max(alist))
# print(min(alist))
# print(sum(alist))

# nlist = [0, '']
# print(any(nlist))


# alist.insert(4, "sdds")
# alist.insert(5, 2131)

# print(alist)


# print(alist[::-1])


# alist.sort()
# alist.sort()

# alist.reverse()






# print(alist)






# abc = ['abc', 'bcd', 'bcdefg', 'acbba', 'opg']


# print(min(abc))
# print(max(abc))

# a = input("enter text ")

# if a == a[::-1]:
#     print("true")
# else:
#     print("false")


# ***21.10.23***




# person = {'Name': 'David', 'Age': 26, 'Weight': 82}

# print(type(person))
# print(person['Age'])


# student = {201: 'joe', 202: 'joee', 203: 'troy'}
# print(student[201],student[203])

# person["Age"] = 20
# print(person['Age'])

# del person["Age"]
# print(person)

# del person['home']
# print(person)



# print('David' in person.values())
# print(('Name','David') in person.items())
# print(person.items())

# d1 = {'Name': 'David', 'Age': 26 }
# d2 = {'Age': 26, 'Name': 'David'}

# print(d1==d2)


# import json
# data = '{"title": "The old man and The sea ", "ISBN": "12345", "Author":"Ernest Hemingway"}'
# json_data = json.loads(data)

# with open('book.json', 'w') as f:
#     json.dump(json_data, f, indent='\t')



# market = {'apple': 500, 'banana': 400, 'grape': 530, 'melon': 650}

# a = input('enter fruits ')
# # b = int(input('enter count '))

# # if a in market:
# #     print(f'{a} total {market[a] * b}')

# # if a in market:
# #     print(f'fruits cost {a} {market[a]}')


# phone_book = {1:22, 2:33, 3:44, 4:55}
# print(phone_book)


# a = input()

# dic = [f'a: {a}']
# print(dic)


# print(f'1234567890987654321')
# print('{0:4d}, {0:5d}, {0:6d}')


# print('{0:.3f}'.format(3.1234567))

# for i in range(2, 11, 2):
#     print(f'{i:3d} {i*i:4d} {i*i*i:5d}')


# lis = [11, 22, 33, 44]
# print(lis * 2)

# ran = tuple(range(5))*3
# print(ran) 


# tp = (1,1,1,2,3,4)
# print(tp.count(1))


# a = ('a', 'b','c')
# a = ('a', 'b','f')

# print(ord('c'))


# t1 = 'a', 'b', 'c'
# t2 = ('a', 'b', 'c')
# t3 = ('d', 'e')

# print(t1 == t2)
# print(t1 > t3)
# print(t1 < t3)
# print(t2 < t3)

# print([t2 + t3])

# print(type(t1))




# a = [1, 2, 3, 4, 5, 6]

# res = [num for num in a if num % 3 == 0]
# print(res)

# b = [1, 2,  4, 5]

# res2= [num for num in b if num % 3 == 0]
# print(res2)


# numbers = [1, 2, -3, -4, 5, 6]

# count = 0
# for num in numbers:
#     if num > 0:
#         count += 1
# print(count)



# lis = 100, 121, 120, 130, 140, 120, 122, 123, 190, 125

# print(f'Daily sales record {lis}')

# c = 0

# for i in lis:
#     i > i + 1 
#     c += 1 
#     if c >= 10:
#         break
# print(c)

# доделай !!!


# ***28.10.23***



# a = (1, 2)
# print(a[0])

# c = (3,4)
# x,y = c
# print(x)



# a = 100
# b = 200
# print(f'before swap : a = {a} b={b} ')

# a,b = b,a
# print(f'after swap : a = {a} b={b} ')

tup = (1,2,3,4,5,6,7,8,9,9,9,9)

# for num in tup:
