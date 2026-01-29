"""
class User:
    login = 'user_login'
    role = 'Python Developer'


u1 = User()
u2 = User()

print(u1.login, u1.role)
print(u2.login, u2.role)

print(u1.__dict__, u2.__dict__)

# user_login Python Developer
# user_login Python Developer
# {} {}


u1.login = 'Esbern'
u1.role = 'React developer'

print(u1.login, u1.role)
print(u2.login, u2.role)

print(u1.__dict__, u2.__dict__)

# Esbern React developer
# user_login Python Developer
# {'login': 'Esbern', 'role': 'React developer'} {}
"""
"""
simple_str = 'hello'
print(type(simple_str))
print(dir(simple_str))
"""
"""
class Student:
    course = "Data Science"

class Group:
    members = []

s1 = Student()
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1
s2 = Student()
s2.name = 'Лев'
s2.surname = 'Сергеев'
s2.semester = 1
result = s1.__dict__
print(result)

Group.members = s1,s2
result = Group.members
print(result)

"""
"""
class User:
    def set_attrs(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role

    def create_task(self, project, description):
       project.add_task(self, description)

class Team:
   def init_team(self, name, members=[]):
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
   def create_task(self, description):
       self.description = description


class Project:
   def create_project(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task()
           task.create_task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")

"""
"""
class User:
    def set_private_key(self,string):
        self.private_key=string
        #return private_key

    def show_private_key(self):
       print(f"Приватный ключ пользователя '{self.private_key}'")

user1 = User()
user1.set_private_key('uox00b_12x')
user1.show_private_key()
print(user1.show_private_key())
"""



class PasswordChecker:
    def set_password_range(self,mini,maxi):
        self.min_len = mini
        self.max_len = maxi
    def check_passwords(self,list_pass):
        arr = list()
        for password in list_pass:
            if self.max_len > len(password) > self.min_len:
                arr.append(True)
            else:
                arr.append(False)
        return arr

checker1 = PasswordChecker()
checker1.set_password_range(5, 10)
print(checker1.min_len, checker1.max_len)

# 5 10

print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))

# [False, True, False]
