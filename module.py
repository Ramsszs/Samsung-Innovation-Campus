from random import randint
def max(x,y):
    if x < y:
        return y
    else:
        return x


def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n -1)


def bubble_sort(arr1):
    n = len(arr1)

    for i in range(n):
        print (arr1)
        for j in range(0, n - i -1):
            if arr1[j] > arr1[j+1 ]:
                arr1[j], arr1[j+1] = arr1[j +1], arr1[j]



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print (arr)
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        print (arr)

        key = arr[i]
        j = i - 1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half) 

        i = j = k = 0

        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1 


 
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)