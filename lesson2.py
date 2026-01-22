"""
yesno = input("Введите Y, если хотите авторизоваться, или N,
             если хотите продолжить работу как анонимный пользователь: ")

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
    print("some data from database")
@is_auth
def change_profile():
    print("Profile has been changed")

from_db()
change_profile()

"""
"""
USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("Введите Y, если хотите авторизоваться, или N,
             если хотите продолжить работу как анонимный пользователь: ")

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

def is_auth(func):
    def wrapper():
        if auth:
            #print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

def has_access(func):
    def wrapper():
        avto=False
        if auth and username != None:
            for i in USERS:
                if username == i:
                    avto = True
        if avto == True:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()
"""
"""
L = ['THIS', 'IS', 'LOWER', 'STRING']

#def lower(str):
#    return str.lower

print(list(map(str.lower,L)))
"""
"""
# Из заданного списка вывести только положительные элементы
def positive(x):
    return x %2== 0  # функция возвращает только True или False

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))

some_list=[-2, -1, 0, 1, -3, 2, -3]
print([i %2== 0 for i in some_list ])
"""
"""
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

sorted_points = sorted(data, key=lambda x: x[0]/x[1]**2)
print(sorted_points)

sorted_points1 = min(data, key=lambda x: x[0]/x[1]**2)
print(sorted_points1)
"""
a = ["это", "маленький", "текст", "обидно"]
#print(list(map(len(a),a)))
#print(len(i) for i in a)
print(list(map(str.upper, a)))
