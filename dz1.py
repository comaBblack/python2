import random

#1
num = int(input('Введите число:'))
a = num//100
b = num%10
c = num//10 - a*10
sum = a + b+ c
pr = a*b*c
print('Сумма цифр числа {} =  {}'.format(num, sum))
print('Произведение цифр числа {} = {}'.format(num, pr))

#2
print(5 & 6)
print(5 | 6)
print(5 ^ 6)
print(5 << 2)
print(5 >> 2)

#3

x1 = int(input('Введите координату x первой точки:'))
y1 = int(input('Введите координату y первой точки:'))
x2 = int(input('Введите координату x второй точки:'))
y2 = int(input('Введите координату y второй точки:'))

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print('Уравнение прямой: y = {}x + {}'.format(k,b))

#4
ask = int(input('1. Целое \n 2. Вещественное \n 3. Символ \n Я хочу:'))
if ask == 1:
    a = int(input('Нижняя граница промежутка:'))
    b = int(input('Верхняя граница промежутка:'))
    print(random.randint(float(a), float(b)))
elif ask == 2:
    a = float(input('Нижняя граница промежутка:'))
    b = float(input('Верхняя граница промежутка:'))
    print(random.uniform(a, b))
else:
    a = ord(input('Нижняя граница промежутка:'))
    b = ord(input('Верхняя граница промежутка:'))
    print(chr(random.randint(a, b)))
   
#5
a = ord(input("Введите букву:"))
b = ord(input("Введите ещё одну:"))

print("Место в алфавите первой буквы: ", a -96)
print("Место в алфавите второй буквы: ", b -96)
print("Букв между ними: ", abs(b - a) - 1)

#6
a = chr(int(input("Введите номер буквы в алфавите:")))
print(a)

#7
print("Введите длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")


#8

a = int(input('Введите год:'))

if (a%4==0 and a%100 !=0) or a%400==0:
    print('Год високосный')
else:
    print('Год не високосный')


#9
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))

if ((a > b and a < c) or (a > c and a < b)):
    print(a)
elif ((b > a and b < c) or (b > c and b < a)):
    print(b)
else:
    print(c)