# tup = (1,2,3,4,5,6,7,8,9,9,9,9)

# mostCount = max(set(tup),
# key=tup.count)
# print(mostCount)


# tup = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a','b'), ('a','b'), ((),), '']

# lis = []

# for i in tup:
#     if bool(i) == False:    
#         continue
#     lis.append(i)
# print(lis)

# lis = [[1,2,3],[4,5,6],[7,8,9]]

# # for i,j,k in lis:
# #     print(i,j,k)

# for i in lis:
#     for j in i:
#         print(j, end=' ')
#     print()


# import copy
# li = [[1,2,3], [4,5,6], [7,8,9]]
# l1 = li
# print(l1)

# l1[0][0] = 90
# print(l1)
# print(li)

# li1 = copy.deepcopy(li)
# li1[0][0] = 90
# print (li)
# print (li1 is li)


# lis1 = [1,2,3,4,5]
# lis2 = []
# for i in lis1:
#     line = []
#     for j in range(i):
#         line.append(0)
#         print(j, end = ' ')
#     lis2.append(line)

#     print()

# for i in range(3):
#     line = []
#     for j in range(3):
#         line.append(0)
#     lis1.append(line)
# print(lis1)


# lis1 = []
# lis2 = []

# for i in range(4):
#     line = []
#     for j in range(16):
#         # line.append(1)
#         print(j, end = ' ')
#     lis2.append(line)
#     print()

# h = 5
# for i in range(h):
#     for j in range(h -i - 1):
#         print(' ', end='',)
#     for k in range(2 * i +1):
#         print('*', end='')    
#     print()
    
# for i in range(h -2,-1,-1):
#     for j in range(h -i - 1):
#         print(' ', end='',)
#     for k in range(2 * i +1):
#         print('*', end='')    
#     print()

# li = [i **2 for i in [1,2,3,4,5] ]
# li1 = [i for i in range(10) if i % 2 ==0 ]

# print(li)
# print(li1)


# l1 = [[0] * i for i in [1,2,3,4]]
# print(l1)


# сделать фигуры из 0 через лист в одну строку  


# 4.10.23

# str1 = ['b','b','b','b','c']
# dic = {}
# for ch in str1: 
#     if ch not in dic.keys():
#         dic[ch] = 0
#     dic[ch] += 1 
# print (dic)



# str1 = ['b','b','b','b','c']
# dic = {}
# for ch in str1: 
#     dic.setdefault(ch, 0)
#     dic[ch] += 1
#     print(list(dic.items()))
# print (dic)



# dic = {'a': 10,'b': 20,'c':30,'d':40}
# dic.update(a = 90, f = 1111)
# dic2 = {2 :'two'}
# dic2.update({2 : 'TWO'})
# a = dic.get('a')
# for dic, num in dic.items():
#     print(dic, ':', num)
# # print(dic.pop('a'))
# # print(dic.popitem())
# # print(dic.values())
# # print(a)
# # print(dic.items())


# # print(dic2)


# file_name = "new.txt"

# word_c = 0

# # with open(file
# #_name, "r") as file:
# #     content = file.read()
# #     words = content.split()
# #     word_c = len(words )
# # print(f"word coint {word_c}")


# with open (file_name, "r") as file:
#     content = file.read()
#     words = content.split()
#     for  word in words:
#         word = word.strip(".,!?").lower()
#         if word: 
#             if word in word_c:
#                 word_c[word] +=1 
#             else:
#                 word_c[word] = 1
# for word,count in word_c.items():
#     print(f"{word}:{count}")






# file_name = "new.txt"
# word_count = {}

# with open(file_name, "r") as file:
#     content = file.read()
#     words = content.split()
    
#     for word in words:
#         word = word.strip(".,!?\"'-").lower()
#         if word:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1


# most_common_word = max(word_count, key=word_count.get)
# most_common_count = word_count[most_common_word]
# print(f"most common word is {most_common_word} {most_common_count}")



# for word, count in word_count.items():
#     print(f"{word}: {count}")



# s = "  ##### welcome, to, python  #####   "
# print (s.rstrip('#'))


# s = ['a','b','c']
# res = ','.join(s)
# print(res)




# s = 'abcdflghebxnfurs'
# clist = list(s)
# print(clist)
# res = ''.join(clist)
# print(res)
# print(s)

# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.title(), s.startswith('H'))
# print(s.endswith('c', 1, 3))
# print(s.endswith('c', 1, 10))


# text = '123,456,789'
# replaceAll = text.replace(',','')
# replace1 = text.replace(',','')

# text = input('write text ')
# text = 'А в Енисее - синева.'
# remove = [":", ';',',','.','-',' ']
# text.lower()

# for ch in remove:
#     text = text.replace(ch, '')
#     text = text.lower()
# print(text)

# if text == text[::-1]:
#     print('true')
# else:
#     print("False")



# 8.11.23

# keys = ['a','b']
# x = dict.fromkeys(keys, 100)
# print(x)

# from collections import defaultdict

# student_tup = (('211','David Doe','010-010')),(('212','John Smith', '012-012')),(('213','Jane Carter','013-013'))
# res = []

# for i in range(len(student_tup)):
#     student = {}
#     student[student_tup[i][0]] = [student_tup[i]][1],student_tup


# from datetime import *
# # today = dt.datetime.now()
# # print(today.replace(month= 12, day=25))
# today = date.today()
# print(today)

# import time 
# seconds = time.time()
# print('time after epoxy ', seconds)

# import time 
# unix = time.time()
# localtime = time.localtime


# import math as m
# # print(m.pow(3,3))
# # print(m.fabs(-99))
# # print(m.ceil(3.3))
# # print(m.floor(3.3))
# # print(m.log(100,10))
# # print(m.sqrt(25))
# # print(m.pi)


# from datetime import datetime 

# start = datetime(2001, 12, 3)
# date = datetime.now()
# d = date - start
# print(d.days)

# lis = ['mon', 'tue','wed', 'wed']
# print(set(lis))


# num = {2,1,3}
# # num.add(5)
# # num.remove(5)
# # if 1 in num:
# #     print('yes')
# print(num)


# s1 = {1,2,3,4,5,6,7}
# s2 = {1,2,3,4,5,6,7,2,4,9,8}
# s3 = {1,2,3,4,5,6,7,2,4,9,8,12,123,11,14}
# print(s1&s2&s3)
# print(s1|s2|s3)
# print(s1^s2^s3)


# 11.11.23

# a = {1,2,4,3,5,6,7,8}
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))
# print(sorted(a))


# a = [10,20,30]
# b = ('ten','twenty','thirty')
# for val in zip(a,b):
#     print(val)


# my_list = [(1,2),(4,5),(4,2),(3,1),(9,4)]
# n_list = ('first', 'second', 'third', 'fourth', 'fifth' )
# a = int(input('Enter int 1 '))
# b = int(input('Enter int 2 '))
# # for val in zip(my_list,n_list):
# #     for a in my_list or b in my_list:
# #         my_list = my_list.index(a,b)
# #         print(f"There is {(a,b)} at the {val}")   
# if (a,b) in my_list:






# def print_str():
#     print('*******')
# print_str()

# def get_sum (start, end):
#     s = 0 
#     for i in range(start, end +1):
#         s += i
#     return s
# x = get_sum(1,10)
# print(x)

# def print_str(n):
#     for i in range(n):
#         print("*******")
# a = int(input("Enter int "))
# print_str(a)



# def print_sum(a,b):
#     res = a + b
#     print(f"{a} + {b} = {res} ")


# print_sum(10,20)




# def greet (*names):
#     for name in names:
#         print(f"Hello {name}")

# greet('a','b','c')
# greet('James', 'tomas')



# def sum_n (*numbers):
#     res = 0 
#     for n in numbers:
#         res += n 
#     return res

# print(sum_n(10,20,30))









# def div(a, b = 2):
#     return a / b

# print(div(4))
# print(div(4,8))





# def print_str():
#     print('welcome')
# print_str()
# print_str()



# def number (a = 100 ,b = 200):
#     print(f'The greater of 100 and 200 is : {max(a,b)}')
#     print(f'The greater of 100 and 200 is : {min(a,b)}')

# number()
    



# def mile (a = 1.61):
#     b = int(input('Enter a mile '))
#     res = a * b
#     print(f'{b} mile = {res}')

# mile()




# def fah ():
#     b = int(input('Enter a celsius '))
#     res = b * 9/5 + 32
#     print(f'{b} celsius = {res} degrees Fahrenheit')

# fah()



# birth = '1998.05.13'
# print(birth.count("."))
# print(max(birth))


# import string
# scr_str = string.ascii_lowercase
# # print(f'scr_str = {scr_str}')
# # scr_str = string.ascii_lowercase
# # print(f'scr_str = {scr_str}')
# # dst_str = scr_str[3:] + scr_str[:3]
# # print(f'dst str = {dst_str}')
# # n = scr_str.index('A')
# # print(f'the index of src_str')
# # a = input('Enter the text ')

# dst_str = scr_str[3:] + scr_str[:3]
# # print(f'dst str = {dst_str}')
# user_input = input('Enter th text ')

# def caeser_cipher():
#     for char in user_input:
#         if char.isalpha():
#             index = scr_str.index(char)
#             res = index + 3
            
#             # print(res)
#             # print(index)


# caeser_cipher()


# import string
# def cipher(a):
#     idx = scr_str.index(a)
#     return dst_str[idx]

# scr_str = string.ascii_lowercase
# dst_str = scr_str[3:] + scr_str[:3]
# src = input('Enter text ')
# print('Encrypted text: ')



# def num (a= 9, b = 2, c = 6):
#     print(f'The average value of 9,2,6 is {(a + b + c)/3}')
#     print(f'The average max of 9,2,6 is {max(a,b,c)}')
#     print(f'The average min of 9,2,6 is {min(a,b,c)}')

# num()



# def bank():
#     a = int(input('Enter ur money '))
#     year = int(input('Enter years '))
#     for i in range(year):
#         a *= 1.10
#         print(f'{i+1} years ur bank will be {round(a)}')
        

# bank()



# 15.10.23


# def factorial(n):
#     if n <=1:
#         return
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# def fact(n):
#     f = 1 
#     for i in range(1, n + 1):
#         f *= i
#     return f 
# print(fact(1000))





# def fib(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(10))





# from timeit import *

# def fib_1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return fib_1(n-1) + fib_1(n-2)

# t3 = Timer()
# print("fib_1(30) * 20 times :" , t3.timeit(number=20))


# dic = {0:0, 1:1}
# def fib_2(n):
#     if n in dic:
#         return dic[n]
#     dic[n] = fib_2(n-1) + fib_2(-2)
#     return dic[n]

# t2 = Timer()
# print("fib_2(30) * 20 times : " ,t2.timeit(number = 20))







# n = int(input())
# def q1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else :
#         return q1(n-1) + q1(n-2)

# print (q1(n))


# n = int(input('enter n '))

# def dit(n):
#     if n == 0:
#         return 0
#     else:
#         return 2 * dit(n-1)

# print(dit(5))

# str1 = "1"
# print(id(str1))

# eval("100+200")
# print(eval("100+200"))



# def q3(n):
#     if n == 0:
#         return 0
#     else:
#         return (1+(n-1))/





# add = lambda x,y: x + y

# print(add(20,5))




# a = [1,2,4,5,6]

# square_a = list(map (lambda x: x**2, a))
# print(square_a)




# ages = [34,15,39,20,18,54]
# print('adults list: ')
# for a in filter(lambda x : x >= 19, ages):
#     print(a, end=' ')



from functools import reduce

# a = [1,2,3,4,5]
# n = reduce(lambda x,y: x + y, a )
# print(n)



# n_list = [1,2,3,4,5,6,7,8,9,10]
# for a in filter(lambda x: x %2 == 0, n_list):
#     print(a, end = (' '))


# n_list = ['a','b','c']
# n = list(map(lambda x: x.upper(), n_list ))
# print(n, end = (' '))


# nlist = list(range(1,101))

# n = reduce(lambda x,y: x + y, nlist)
# print(n)


# nlist = list(range(1,11))
# for n in filter(lambda x: x % 2 == 0, nlist):
#     print(n, end = (' '))


# *************
# try:
#     b = 2 / 0
#     a = 1 + 'hundred'
# except ZeroDivisionError:
#     print('error', e)

# def devide(x,y):
#     try:
#         res = x/y
#     except ZeroDivisionError:
#         print()
# *****************







# a = iter([10,20,30])
# print(next(a),next(a),next(a))


# riiter = iter(range(3))
# # print(next(riiter) , next(riiter) , next(riiter))
# # print(next(riiter))
# # # print(next(riiter))
# # # print(next(riiter))

# for riiter in range(3):
#     s += 



# a = list(range(1,8))
# a = [x**2 for x in a]
# print(a)

# a = list(range(15,30))
# print([x for x in a if x > 19])


# a = list(range(10))
# print([x * x for x in a if x %2 == 0])


# s = input('enter int' ).split()
# lst = [int(x) for x in s]
# print(lst)
# print([int(x) for x in input('enter mult int ').split()])*********************************************



# product = [x * y for x in range(1,4) for y in [2,4,6]]
# print(product)


# print(list(filter(lambda x : (x % 2 == 0 and x% 3 == 0 ), range(1,31))))
# print([n for n in range(1,31) if n % 2 ==0 and n % 3 == 0 and n % 5 == 0])









# scores = [100,90,95,80,70,0,80,90,0,100,75,20,30,50,90,90,90,80]
# scores_split = [scores[i * 3: (i + 1 ) * 3] for i in range(6)]
# print(scores_split)
# # print(list(filter(lambda x : (x != 0) , scores_split)))
# print([(x for x in scores_split if x > 0 ), scores_split  ])





# x = 10 
# y = 11 
# def foo():
#     x = 20 
#     def bar():
#         a = 30 
#         print(a,x,y)
#     bar()
#     x = 40
#     bar()

# foo()



# def prcounter():
#     counter = 200
#     print('counter = ', counter)

# counter = 100
# prcounter()
# print('counter = ', counter)




# def prcounter():
#     global counter
#     counter = 200
#     print('counter = ', counter)

# counter = 100
# prcounter()
# print('counter = ', counter)



# def call(func):
#     func()
# def greet():
#     print('hello')
# print('callfunc(greet) func')
# call(greet)



# def plus (a,b):
#     return a + b
# def minus(a,b):
#     return a - b
# l_list = [plus,minus]
# a = l_list[0](100,200)
# b = l_list[1](100,200)
# print(f'a = {a}')
# print(f'b = {b}')


# def add(a,b):
#     return a + b
# def f(g,a,b):
#     return g(a,b)
# print(f(add, 3,4))


# def decorate (style = 'italic'):
#     def italic(s):
#         return '<i>' + s + '</i>'
#     def bold(s):
#         return '<b>' + s + '</b>'
#     if style  == 'italic':
#         return italic
#     else:
#         return bold
# dec = decorate()
# print(dec('hello'))
# dec2 = decorate('bold')
# print(dec2('hello'))



# n1 = 1 
# def fu1():
#     def fu2():
#         global n1
#         n1 += 1
#         print(n1)
#     fu2()
# print(fu1())




# def fu1():
#     n1 = 1
#     def fu2():
#         global n1
#         n1 += 1
#         print(n1)
#     fu2()
# print(fu1())


# def fu1():
#     n1 = 1
#     def fu2():
#         nonlocal n1
#         n1 += 1
#         print(n1)
#     fu2()
# print(fu1())





# def f():
#     a = 777
#     def g():
#         a = 100
#         def h():
#             nonlocal a
#             a = 333
#         h()
#         print(f'level 2 a = {a}')
#     g()
#     print(f'level 1 a = {a}')

# f()

# def closure ():
#     a = 2 
#     def mult(x):
#         return a *x
#     return mult

# c = closure()
# print(c(1),c(2),c(3))



# def makecount():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1 
#         return count
#     return counter 

# c1 = makecount()
# c2 = makecount()

# print('c1', c1())
# print('c1', c1())
# print('c1', c1())
# print('c2', c2())



# def calc():
#     a = 3 
#     b = 5
#     def mult(x):
#         return a * x + b
#     return mult

# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))


# def calc():
#     a = 2 
#     b = 3
#     return lambda x : a * x + b

# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))



# def calc():
#     a = 2
#     b = 3
#     total = 0
#     def mult(x):
#         nonlocal total
#         total = total + a *x + b
#         return total

#     return mult
# c = calc()
# print(c(1),c(2),c(3))





# def say_hi():
#     a = "hi"
#     def say_hello():
#         nonlocal a 
#         a = 'hello'
#         return a
    



# print(say_hello())

# def calc():
#     a = 3 
#     b = 5
#     def mul(x):
#         return lambda x : a * 5 + b

# print (calc())





# import turtle as t 

# t.setup(width=400, height=400)
# for i in range (2):
#     t.forward(100)
#     t.left(90)
# t.done()

# # tx1 = 'life is too life life life short u need python'
# tx2 = 'the ,est moomments Life'

# # match = re.search('life',tx1)
# # print (match.group())

# # # print(re.search('life',tx1))
# # # print(re.search('life',tx2))


# import re


# # text = 'please call 010-0141--1234'
# # regex = re.compile('(\d{3})-(\d({4}-\d{4}))')
# # match_obj = regex.search(text)
# # print(match_obj.group())
# tx2 = 'the ,est moomments Life'

# print(re.search('[Ll]ife',tx2))




import  re 
# tx1 = 'Life'
# tx2 = 'no life life life'
# tx3 = 'boo life'

# print(re.search('life$', tx1))
# print(re.search('life$', tx3))
# print(re.search('life$', tx2))

# print(re.search('ab*','cabababababbababababab'))
# print(re.search('ab+','cdamvab'))
# print(re.findall('[a]b',' ab ab AB  ababab'))











# def count_words(text):
#     words = re.findall(r'\b\w+\b', text)
#     return len(words)

# ur_text = input('enter ur text ')
# word_count = count_words(ur_text)
# print(f'word count here = {word_count}')






class Cat:
    def __init__(self, name, color):
        pass
    def meow(self):
        pass
    def run(self):
        pass
    def walk(self):
        pass

nabi = Cat ('nabi','black')
nero = Cat ('nero','white')



