""" class unit:

    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def show_info(self):
        print(f'单位状态:hp{self.hp},pw{self.power}')

class hero(unit):
    
    def __init__(self, hp, power,name):
        super().__init__(hp, power)
        self.name = name
    
    def show_info(self):
        print(f'英雄{hero_name}状态:hp{self.hp},pw{self.power}')

hero_name = input('取个名字:')

Hero =  hero(100,10,hero_name)
Enemy = unit(100,10)

Hero.show_info()
Enemy.show_info() """

#乘法口诀表
""" for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t') """


""" class Student:

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.scores = s
    
    def sum_score(self):
        total = 0

        for score in self.scores:
            total += int(score)
    
        return total

students = []

file = open('C:/Users/songqiheng/Desktop/student.txt','r')
lines = file.readlines()
file.close()

for line in lines:
    if line:
        args = line.split(' ')
        name = args[0]
        age = int(args[1])
        scores = args[2:]

        students.append(Student(name,age))

while True:
    text = input('请输入姓名和年龄和成绩：')
    
    if text == 'n':
        break
    
    args = text.split(' ')
    
    input_name = args[0]
    input_age = int(args[1])
    input_scores = args[2:]

    student = Student(input_name,input_age,input_scores)

    students.append(student)

lines = []

for sb in students:
    lines.append(f'{sb.name}{sb.age}\n')
    total_score = sb.sum_score()
    print(f'学生{sb.name}年龄{sb.age}成绩{total_score}')

file = open('C:/Users/songqiheng/Desktop/student.txt','w')
file.writelines(lines)
file.close() """

# class Student:

#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#         """ self.scores = s """
    
# """     def sum_score(self):
#         total = 0

#         for score in self.scores:
#             total += int(score)
    
#         return total """

# students = []

# file = open('C:/Users/songqiheng/Desktop/student.txt','r')
# lines = file.readlines()
# file.close()

# for line in lines:
#     if line:
#         args = line.split(' ')
#         name = args[0]
#         age = int(args[1])
#         """ scores = args[2:] """

#         students.append(Student(name,age))

# while True:
#     text = input('请输入姓名和年龄：')
    
#     if text == 'n':
#         break
    
#     args = text.split(' ')
    
#     input_name = args[0]
#     input_age = int(args[1])
#     """ input_scores = args[2:] """

#     student = Student(input_name,input_age)

#     students.append(student)

# lines = []

# for sb in students:
#     lines.append(f'{sb.name}{sb.age}\n')
#     """ total_score = sb.sum_score() """
#     print(f'学生{sb.name}年龄{sb.age}')

# file = open('C:/Users/songqiheng/Desktop/student.txt','w')
# file.writelines(lines)
# file.close()

# defence = 10

# def hurt(damage):
#     global defence
#     damage -= defence
#     defence -= 1

#     def def_break():
#         nonlocal damage

#         if damage > 50:
#             global defence
#             defence = 0
#             damage = 1
#             print('cnm')

#     def_break()

#     if damage <=0:
#         def show(text):
#             print(text)
#         m = 'sb'
#         show(m)
#         return
    
#     def show(text):
#         print(text)
    
#     message = f'is{damage}'
#     show(message)

# hurt(100)
# hurt(15)
# hurt(15)

# class Unit:

#     def __init__(self,hp,power):
#         self.__hp = hp
#         self.power = power

# class Hero(Unit):
    
#     def __init__(self, hp, power,name):
#         super().__init__(hp, power)
#         self.name = name

# hero_name = input('取个名字:')

# hero =  Hero(100,10,hero_name)
# enemy = Unit(100,10)
# # hero.__hp += 100

# print(f'name{hero.name} power{hero.power}')
# # print(f'玩家状态:英雄{hero.name},hp{hero.__hp},power{hero.power}')
# # print(f'敌人状态:hp{enemy.__hp},power{enemy.power}')

# class Unit:
#     count = 0

#     def __init__(self,hp):
#         self.hp = hp
#         self.dead = False
#         Unit.count += 1

#     def hurt(self,damage):
#         self.hp -= damage
#         print(f'受到{damage}点伤害')

#         if self.hp <= 0:
#             self.dead = True
#             Unit.count -= 1
#             print(f'死了一个，剩{Unit.count}个')

# import random
# units = [Unit(10),Unit(15),Unit(20)]
# game_over = False

# while not game_over:

#     for unit in units:
#         if not unit.dead:
#             damage = random.randint(0,10)
#             unit.hurt(damage)

#             if Unit.count == 1:
#                 game_over = True
#                 break

# print('结束')

# class Unit:
#     count = 0

#     @staticmethod
#     def random_id():
#         import random
#         return f'id_{random.randint(1,10000)}'
    
#     @classmethod
#     def show_board(cls):
#         print(f'有{cls.count}个单位')
    
#     def __init__(self,hp):
#         self.id = self.random_id()
#         self.hp = hp
#         Unit.count += 1

# u1 = Unit(100)
# u2 = Unit(90)
# print(f'id为{u1.id} {u2.id}')
# u2.show_board()

# print('gameover')
# input('123:')

for i in ('hello'):
    print(i)