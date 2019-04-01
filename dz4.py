import cProfile
#1

def b(a = 23103057693698):
    i = 0
    j = 0

    while a != 0:
        if a % 2 == 0:
            i += 1
        else:
            j += 1
        a //= 10
    return 'Четных - {}; Нечетных - {}'.format(i,j)
'''
print(cProfile.run('b()'))

5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 dz4.py:3(b)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
'''

#2
#Используя алгоритм «Решето Эратосфена»
def a():
    n = 1000
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
print(cProfile.run('a()'))
'''
1006 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 dz4.py:31(a)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}

'''
#Не используя алгоритм «Решето Эратосфена»
def b():
    k = 0
    i = 2
    j = 2
    not_simple = False
    number = 1000

    while True:
        while i > j:
            if i % j == 0 and i != j:
                not_simple = True
                break
            j += 1

        if not_simple == False:
            k += 1

        j = 2
        i += 1
        not_simple = False
        if k == number:
            break
    print(i - 1)
print(cProfile.run('b()'))
'''
5 function calls in 0.355 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.355    0.355 <string>:1(<module>)
        1    0.355    0.355    0.355    0.355 dz4.py:65(b)
        1    0.000    0.000    0.355    0.355 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''