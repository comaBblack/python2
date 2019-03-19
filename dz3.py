import random
#1

sum = 0
for i in range(2,100):
    for j in range(2,10):
        if i%j==0:
            sum+=1
print(sum)

#2
a = [1, 2 ,4 ,5 ,6 ,7 ,8, 32, 45, 66, 100]
b = []
for i in range (len(a)):
    if a[i]%2 == 0:
        b.append(i)
print(b)

#3
a = []
for i in range(0,12):
    a.append(random.randint(-10,50))
print(a)
for i in range(len(a)):
    min_ind = 0
    max_ind = 0
    if a[i]< a[min_ind]:

        min_ind = i
for i in range(len(a)):
    if a[i]>a[max_ind]:

        max_ind = i
a[min_ind], a[max_ind] = a[max_ind], a[min_ind]
print(a)

#5

a = []
max = -100
ind = 0
for i in range(0,10):
    a.append(random.randint(-50,50))
    if  (a[i] > max) and (a[i] <0):
        max = a[i]
        ind = i
print(f'Массив: {a} \nМаксимальное отрицательное число:{max},его индекс:{ind}')

#6
a = []
ind_max =0
ind_min =0
sum = 0
for i in range(0,12):
    a.append(random.randint(-10,50))
    if a[i] <a[ind_min]:
        ind_min = i
    if a[i] > a[ind_max]:
        ind_max = i
    if ind_min > ind_max:
        ind_max, ind_min = ind_min, ind_max

for i in range(ind_min + 1, ind_max):
    sum += a[i]
print(f'Массив: {a} \nСумма:{sum}')

#7
a = []
min1 = 0
min2 = 1
for i in range(0,12):
    a.append(random.randint(-10,50))

if a[min1] > a[min2]:
    min1, min2 = min2, min1

for i in range(2, len(a)):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print(a[min1], a[min2], a)

#8
N = 5
M = 4
matrix_arr = []

for i in range(M):
    user_arr = []
    user_sum = 0
    for j in range(N - 1):
        user_num = int(input('Введите число: '))
        user_arr.append(user_num)
        user_sum += user_num
        print(user_num, end=' ')
    user_arr.append(user_sum)
    print(user_sum)
    matrix_arr.append(user_arr)
print(matrix_arr)

#9
N = 3
M = 5

matrix_arr = []

for i in range(N):
    str_arr = random.sample(range(1, 100), M)
    matrix_arr.append(str_arr)
    print(str_arr)

max_min_num = 0
for i in range(M):
    min_num = matrix_arr[0][i]
    for j in range(N):
        if matrix_arr[j][i] < min_num:
            min_num = matrix_arr[j][i]
    if min_num > max_min_num:
        max_min_num = min_num
print(max_min_num)

