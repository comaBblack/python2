import random
#1

a=1
while a!= '0':
    a = str(input('Введите знак +, -, *, / или 0 для завершения программы'))
    if a == '+':
        num1 = int(input('Введите первое число:'))
        num2 = int(input('Введите второе число:'))
        sum = num1 + num2
        print(sum)
    if a== '-':
        num1 = int(input('Введите первое число:'))
        num2 = int(input('Введите второе число:'))
        r = num1 - num2
        print(r)
    if a == '*':
        num1 = int(input('Введите первое число:'))
        num2 = int(input('Введите второе число:'))
        pr = num1 * num2
        print(pr)
    if a =='/':
        num1 = int(input('Введите делимое:'))
        num2 = int(input('Введите делитель:'))
        if num2 !=0:
            d = num1/num2
            print(d)
        else:
            print('Делить на 0 нельзя')
    else:
        print('Вы ввели недопустимый знак, попробуйте ещё раз')

    if a == '0':
        break

#2
i = 0
j = 0
a = int(input('Введите число:'))
while a != 0:
    if a % 2 == 0:
        i += 1
    else:
        j += 1
    a //= 10
print('Четных - {}; Нечетных - {}'.format(i,j))


#3
a = int(input('Введите число'))
b = 0
while a>0:
    b = b*10 + a%10
    a = a//10
print(b)

#6
k = 10
a = random.randint(0,100)
ans = int(input('Введите число:'))
if ans == a:
    print('Вы угадали')

elif ans !=a:
    while ans!=a and k>1:
        k= k-1
        print('Неверно, у вас осталось {} попыток'.format(k))
        ans = int(input('Введите число:'))
        if k == 1:
            print('Вы не угадали. Загаданное число - {}'.format(a))

#7
a = 0
b = 0
n = int(input('Введите число:'))
for i in range(1,n+1):
    a = a+i

b = n*(n+1)/2
print('{} = {}'.format(a,b))

#8
a = int(input("Введите число:"))
b = int(input("Введите цифру:"))
sum = 0
while a!= 0:
    c = a % 10
    if b == c:
        sum += 1
    a = a// 10

print(f"Цифр {b} - {sum}")
#9
num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
a1 = 0
a2 = 0
b = num1
c = num2
while b >0:

    a1 = a1 + b%10
    b = b//10
while c >0:

    a2 = a2 + c % 10
    c = c // 10
if a1>a2:
    print('Число - {} \nСумма цифр - {}'.format(num1,a1))
else:
    print('Число - {} \nСумма цифр - {}'.format(num2, a2))

#4
#Объясните, пожалуйста, почему не работает
n = int(input("Введите число:"))
a = 1.0
sum = 0
while n > 0:
    a = a*(-0,5)
    sum = sum + a
    n -= 1
print(sum)


