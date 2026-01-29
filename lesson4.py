"""
class User:
    def __init__(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role

    def create_task(self, project, description):
       project.add_task(self, description)

class Team:
   def __init__(self, name, members=[]):
       self.name = name
       self.members = members

   def add_member(self, user):
       self.members.append(user)

   def show_members(self):
       print(f'Team {self.name} members:')
       for i, user in enumerate(self.members):
           print(f'№{i + 1}, login: {user.login}, name: {user.name}')

   def get_team_size(self):
       return len(self.members)

class Task:
   def __init__(self, description):
       self.description = description


class Project:
   def __init__(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")
"""
"""
class Team:
    def __init__(self,name, team_size, capital):
       self.name = name
       self.team_size = team_size
       self.capital = capital

    def show_info(self):
       print(f"Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}")


team1 = Team('OpenAI', 100, 1000000)
team1.show_info()
# Team name: OpenAI, team size: 100, capital: 1000000
"""
"""
class AreaPoint:
    def __init__(self, i, j, height=15):
        self.i = i
        self.j = j
        self.height = height

    def __repr__(self):
        return f"AreaPoint(i={self.i}, j={self.j}, height={self.height})"

# Создаем двумерный список area_list
area_list = []
for i in range(3):
    row = []
    for j in range(3):
        point = AreaPoint(i, j, 15)  # Создаем объект AreaPoint
        row.append(point)
    area_list.append(row)
"""
"""
class Person:
    def __init__(self,name = None, age = None, gender = None, occupation = None):
    #def __init__(self,name , age , gender , occupation ):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
    def set_attributes(self,lists):
        for list,atibut in lists.items():
            #print(list, atibut)
            if hasattr(self, list):  # Проверяем, существует ли атрибут
                setattr(self, list, atibut)
    def show_card(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}")

p1 = Person()
p1.set_attributes({'name': 'Elon', 'age': 51, 'gender': 'Male', 'occupation': 'CEO', 'company': 'Tesla'})
p1.show_card()
# Name: Elon
# Age: 51
# Gender: Male
# Occupation: CEO
p2 = Person(name='Mark', occupation='Expert')
p2.set_attributes({'name': 'Bob', 'occupation': 'Worker', 'company': 'StenWoods'})
p2.show_card()
# Name: Bob
# Age: None
# Gender: None
# Occupation: Worker
"""
"""

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.check = False
        self.S = 0
    def is_triangle(self):
        if (self.a+self.b)>self.c and (self.a+self.c)>self.b and (self.b+self.c)>self.a:
            self.check =True
        return self.check
    def get_triangle_area(self):
        if self.is_triangle() == True:
            p = 0.5 * (self.a+self.b+self.c)
            self.S = (p*(p-self.a)*(p-self.b)*(p-self.c))** 0.5
        return self.S



t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())

# False


print(Triangle(a = 3, b = 4, c = 5).get_triangle_area())

# 6.0

print(Triangle(a = 3, b = 10, c = 16).get_triangle_area())

# 0

"""

class Queue:
    def __init__(self):
        self.items=[]
        self.check = True

    def enqueue(self,element):
        self.items.append(element)
        #print(self.items)
    def is_empty(self):
        if len(self.items) == 0:
            self.check = True
        else:
            self.check = False
        #print(self.check)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        #print(self.items)
    def show_queue(self):
        ret=''
        for element in self.items:
            ret += str(element) + ' '
        print(ret)
        return ret



# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()

# 3
