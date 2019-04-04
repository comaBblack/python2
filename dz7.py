import random

#1

mas = [random.randint(-100,100) for i in range(15)]
print('Исходный массив:', mas)

def bubble(mas):
    n = 1
    a = 0
    while n < len(mas):
        for i in range(len(mas) - n):
            if mas[i] < mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
                a +=1
        if a == 0:
            break
        n +=1
    return mas

print('Отсортированный массив:',bubble(mas))



#2
mas = [random.randint(-100,100) for i in range(15)]
print('Исходный массив:', mas)

def merge(mas):
    if len(mas) >1:
        center = len(mas)//2
        left = mas[:center]
        right = mas[center:]

        merge(left)
        merge(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mas[k] = left[i]
                i += 1
            else:
                mas[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            mas[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            mas[k] = right[j]
            j += 1
            k += 1
        return mas

print('Отсортированный массив:',merge(mas))



#3
mas = [random.randint(-100,100) for i in range(15)]
print('Исходный массив:', mas)

def mediana(mas):
    for i in range(len(mas)):
        count_min = 0
        count_max = 0
        for j in range(len(mas)):
            if mas[j] != mas[i]:
                if mas[j] > mas[i]:
                    count_min += 1
                else:
                    count_max += 1
        if  count_min == count_max:
            print(f'{i}-й элемент {mas[i]} медиана')
            break


k = 11
source_list = [random.randint(-100, 100) for _ in range(2 * k + 1)]

print(mediana(mas))

