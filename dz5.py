import collections

#1
num = int(input('Введите количество предприятий:'))
company = collections.defaultdict(list)
profits = 0
sum = 0
for i in range(num):
    name = input(f'Введите имя {i +1} компании:')
    for j in range(4):
        profit = int(input(f'Введите прибыль за {j+1} квартал:'))
        profits += profit
    company[name] = profits
    sum = sum +profits

s_profit = sum/num
print(f'Средняя прибыль за год: {s_profit}')
a = []
for i in company:
    if company[i]< s_profit:
        a.append(i)
    print(f'Предприятия с прибылью ниже средней: {a}')
b = []
for j in company:
    if company[i]> s_profit:
       b.append(i)
    print(f'Предприятия с прибылью ниже средней: {b}')

#2
nums = collections.defaultdict(list)

for i in range(2):
    j = input(f'Введите {i + 1}-е шестнадцатеричное число: ')
    nums[i + 1] = list(j)
print(nums)

lst = [int(''.join(i), 16) for i in nums.values()]

print(f'Сумма введенных чисел: {list(hex(sum(lst)).upper())}')
print(f'Произведение введенных чисел : {list(hex(lst[0] * lst[1]).upper())}')








