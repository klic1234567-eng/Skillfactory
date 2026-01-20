"""
L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3+2

print(id(a))
print(id(b))
print(id(a) - id(b))

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)
"""
"""
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print( id(list_id_before) == id(list_id_after))
"""
"""
def get_text(str):
    s= set(str)
    return len(s)
print(get_text('        The Zen of Python'))
"""
"""
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)
"""
"""
L = list(map(int, input().split()))

print(not any(L))
"""
"""
numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep=', ')

# 2*x = 9
def linear_solve(a,b):
    return b/a
print(linear_solve(2, 9))


# 0*x = 1
print(linear_solve(0,1))
"""
"""
# D = b**2 - 4*a*c - дискриминант

def linear_solve(a,b,c):
   D = b**2 - 4*a*c
   return D

print(linear_solve(3,3,1))


def quadratic_solve(a,b,c):
    D = b**2 - 4*a*c
    if D>0:
        return D
    elif D==0:
        return -b/(2*a)
    else:
        return 'Нет вещественных корней'
"""
"""
def quadratic_solve(a, b, c):
    D = b**2 - 4*a*c
    if D<0:
        return f"{D} Нет вещественных корней"
    elif D==0:
        return -b/(2*a)
    else:
        return (-b - D ** 0.5) / (2 * a), (-b + D ** 0.5) / (2 * a)

print(quadratic_solve(list(map(float, input().split()))))
#print(quadratic_solve(L[0], L[1], L[2]))

#list(map(float, input('Введите').split()))
"""
"""
def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list((1,5,6)))

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(1234))
"""
"""
def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)
print(equal(21,3))
"""
"""
def e():
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        n += 1
last = 0
for a in e(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение
"""
iter_obj = iter("Hello!")

print(next(iter_obj))
