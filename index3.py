import random
import module
# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def meow(self):
#         pass
#     def run(self):
#         pass
#     def walk(self):
#         pass
#     def meow(self):
#         print('meow meowmeowmeowmeow')
#     def __str__(self):
#         return f'Cat (name = '+self.name+', color = '+self.color+')'




# nabi = Cat ('nabi','black')
# nero = Cat ('nero','white')
# nabi.meow()
# nero.meow()

# print(nabi)
# print(nero)



# class Circle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b


#     def area(self):
#         return self.a * self.b

# c1 = Circle(4, 5)
# print(c1.area())

# def is_empty(stack):
#     return True if len(stack) == 0 else False

# stack = []
# print(is_empty(stack))




# stack = Stack()
# stack.push('banana')
# stack.push('apple')
# stack.push('tomato')
# stack.pop()
# stack.push('strawberry')
# stack.push('grapes')
# stack.pop()
# print(stack.stack)








# 29.11.23*******************************************************************************************8


nums = [11,22,33,44,55,53]
x = 54
# def seq_search(s,x):
#     for i in s:
#         if i == x:
#             return i
#     return -1 

# res = seq_search(s,x)

# if res != -1:
#     print(x)
# else:
#     print(f'{x} not found')


# def seq_search(nums, x):
#     for i in range(len(nums)):
#         if x == nums[i]:
#             return print(i)
#     return print(-1)

# seq_search










# nums = [11,32,12,43]


# def find_largest(nums):
#     largest = 0 
#     for i in range(1, len(nums)):
#         if nums[largest] < nums[i]:
#             largest = i
#             print (largest)
#     return largest
#     print (largest)

















# num = list(range(1, 101))

# def bin(num,x):
#     low = 0
#     high = len(num) -1
#     while  low <= high:
#         mid = (low + high) //2
#         quess = num[mid]
#         if quess == x:
#             return mid
#         elif quess < x:
#             low = mid +1 
#         else:
#             high = mid - 1
#     return -1 

# x = 51
# res = bin(num,x)
# if res != -1:
#     print(f'{x} is {res}')
# else:
#     print(f'{x} not found')

# num = list(range(20,100,10))


# def search(num, x) :




# x = int(input(" "))
# pos = search(num,x)
# print(f'{x} should be inserted at position {pos}')
# num.insert(pos,x)
# print(num)






# class Hashtable:
#     def __init__(self, size):
#         self.size = size
#         self.table = {}
#         for i in range(size):
#             self.table[i] = []

#     def hash(self,key):
#         return key % self.size
    
#     def get(self, key):
#         return self.table[self.hash(key)]
#     def put(self, key, value):
#         bucket = self.table[self.hash(key)]
#         if value not in bucket:
#             bucket.append(value)

# table = Hashtable(8)
# books = ['The Little Prince', 'The Old Man and the Sea', 'Beauty and the Beast', 'The Last Leaf']

# for book in books:
#     key = sum(map(ord, book))
#     table.put(key, book)
# for key in table.table.keys():
#     print(key, table.table[key])


# table = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C',
#         100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'XI', 5:'V', 4:'VI', 1:'I'
# }


# def to_rom(num):
#     rom_num = ''
#     i = 0
#     while num > 0:
#         for x in range(num // table[i]):
#             rom_num += table[i]
#             num -= table[i]
#         i += 1
#     return rom_num


# num = int(input('Input a num '))
# print(to_rom(num))


# до делай перевод арабских чисел в рисмкие***********************







# import module
# import random 

# a = list(range(10,101,10))
# b = [10, 40,20,30,50,90,70,80]
# random.shuffle(a)

# # def bubble_sort(arr):
# #     n = len(arr)

# #     for i in range(n):
# #         for j in range(0, n - i -1):
# #             if arr[j] > arr[j+1 ]:
# #                 arr[j], arr[j+1] = arr[j +1], arr[j]


# # print(module.bubble_sort(b))
# # print(module.selection_sort(b))
# # print(module.insertion_sort(b))
# # print(module.merge_sort(b))
# print(module.quick_sort(b))


# сравнить сортировки *************************************************







# def coin_change(coins, amount):
#     changes = []
#     for coin in coins:
#         num_coins = amount // coin
#         amount %= coin
#         changes.append((coin, num_coins))
#     return changes

# coins = [500, 100, 50, 10]

# while True:
#     amount = int(input('Введите сумму: '))
    
#     if amount <= 0:
#         break  # Выход из цикла при вводе неположительного значения

#     changes = coin_change(coins, amount)
#     print("Сдача для суммы", amount, ":", changes, "Общее количество монет:", len(changes))


# def max_subsequence_sum(arr):
#     current_sum = max_sum = arr[0]

#     for number in arr[1:]:
#         current_sum = max(number, current_sum + number)
#         max_sum = max(max_sum, current_sum)

#     return max_sum

# sequence = [-2, 1,-3,4,-1,2,1,-5,4]
# result = max_subsequence_sum(sequence)

# print("Maximum sum of consecutive values:", result)





# a m e r x l t o 
# 9 5 4 3 2 0 8 1 

# a  m e r r y  x m a s  t o  a l l

# 3                 9     8 1  9 0 0



# 9 + 5 + 2 + 4 


