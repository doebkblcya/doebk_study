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
#     try:
#         input_age = int(args[1])
#     except:
#         print('wrong')
#         continue

#     """ input_scores = args[2:] """

#     student = Student(input_name,input_age)

#     students.append(student)

# lines = []

# for sb in students:
#     lines.append(f'{sb.name} {sb.age}\n')
#     """ total_score = sb.sum_score() """
#     print(f'学生{sb.name}年龄{sb.age}')

# file = open('C:/Users/songqiheng/Desktop/student.txt','w')
# file.writelines(lines)
# file.close()

""" import random


class unit:

    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def show_info(self):
        print(f'单位状态:hp{self.hp}')
    
    def atttack(self,target):
        damage = self.power + random.randint(-10,10)
        target.hp -=damage
        print(f'受到的{damage}点伤害')

        if target.hp <= 0:
            return True

class hero(unit):
    
    def __init__(self, hp, power,name):
        super().__init__(hp, power)
        self.name = name
    
    def show_info(self):
        print(f'英雄{hero_name}状态:hp{self.hp}')

hero_name = input('取个名字:')

Hero =  hero(100,10,hero_name)
Enemy = unit(100,10)

Hero.show_info()
Enemy.show_info()

while True:
    if Hero.atttack(Enemy):
        print('victory')
        break
    else:
        Enemy.show_info()

    if Enemy.atttack(Hero):
        print('defeat')
        break
    else:
        Hero.show_info() """

""" class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def are_segments_intersect(p1, p2, q1, q2):
    # 判断线段p1p2和线段q1q2是否相交
    def cross_product(p, q, r):
        return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)

    return (cross_product(p1, p2, q1) * cross_product(p1, p2, q2) < 0) and \
        (cross_product(q1, q2, p1) * cross_product(q1, q2, p2) < 0)


def connect_points(points):
    # 按照x坐标排序，如果x坐标相同，则按照y坐标排序
    sorted_points = sorted(points, key=lambda p: (p.x, p.y))

    n = len(sorted_points)
    edges = []

    # 连接第一个点和第二个点
    edges.append((sorted_points[0], sorted_points[1]))

    # 逐个连接点
    for i in range(2, n):
        current_point = sorted_points[i]
        prev_point = edges[-1][1]

        # 判断当前点与最后一条边是否相交
        while any(are_segments_intersect(prev_point, current_point, e[0], e[1]) for e in edges):
            # 寻找一个不与其他边相交的点
            current_point = next(p for p in sorted_points if
                                 not any(are_segments_intersect(p, current_point, e[0], e[1]) for e in edges))

        # 连接当前点与最后一条边的终点
        edges.append((prev_point, current_point))

    # 连接最后一个点和第一个点
    last_point = edges[-1][1]
    first_point = edges[0][0]
    if are_segments_intersect(last_point, first_point, edges[-1][1], edges[0][0]):
        intersect_point = next(
                                p for p in sorted_points if not any(are_segments_intersect(p, first_point, e[0], e[1]) for e in edges))
        edges[-1] = (last_point, intersect_point)
        edges.append((intersect_point, first_point))
    else:
        edges.append((last_point, first_point))

    return edges

points = [Point(-8, 0), Point(-3, 11), Point(2, 6), Point(-2, 13),Point(0,18),Point(-4,12)]
edges = connect_points(points)
for edge in edges:
    print(edge[0].x, edge[0].y, "->", edge[1].x, edge[1].y) """

""" def is_rotation_1(S, T):
    if len(S) != len(T):
        return False
    S = S + S
    return T in S


def is_rotation_2(S, T):
    if len(S) != len(T):
        return False
    n = len(S)
    for i in range(n):
        if S[i] == T[0]:
            j = 0
            while j < n and S[(i + j) % n] == T[j]:
                j += 1
            if j == n:
                return True
    return False

s = 'plea'
t = 'leap'
print("空间效率较高 " + s + " " + t + " " + str(is_rotation_1(s, t)))  # True
print("时间效率较高 " + s + " " + t + " " + str(is_rotation_2(s, t)))  # True

s='qwertyuiop'
t='wertyuiopq'
print("空间效率较高 " + s + " " + t + " " + str(is_rotation_1(s, t)))  # True
print("时间效率较高 " + s + " " + t + " " + str(is_rotation_2(s, t)))  # True

s='-.h+AcnS)ojAJ[GgXAqg>p:\Cjho~}$mhF!+gb7>FpJ%Yg|d`G'
t='uQ|T-whtllL`wr}@Lz/oBURD`OV%x05w;gVc}bbfPoO(fG0c&e'
print("空间效率较高 " + s + " " + t + " " + str(is_rotation_1(s, t)))  # True
print("时间效率较高 " + s + " " + t + " " + str(is_rotation_2(s, t)))  # True    
 """

""" import datetime

d = datetime.datetime(2024,10,17,19,15,00)
n = datetime.datetime.now()
t = datetime.date.today()

print(d)
print(n)
print(t) """

""" def main():

    def show_messaage(text):
        import datetime
        now = datetime.datetime.now()
        print(f'{now} 机器人："{text}"')

    show_messaage('hello')

    while True:
        text = input('请输入消息输入n退出：')

        if text == 'n':
            print('再见')
            break
        else:
            show_messaage('牛逼了')

main()      """      

""" class Student:
    
    class Scores:
        def __init__(self,s):
            self.ch = int(s[0])
            self.en = int(s[1])

        def sum(self):
            return self.ch + self.en

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.scores = self.Scores(s)

    def show_info(self):
        print(f'{self.name} 总分{self.scores.sum()}')

text = input('请输入')

args = text.split(' ')
input_name = args[0]
input_age = args[1]
input_scores = args[2:]

s = Student(input_name,input_age,input_scores)

s.show_info() """

# def pd(text):
#     return text % 2 == 0

# def play():
#     text = int(input('请输入：'))

#     if pd(text):
#         print(f'{text}是偶数')

#     else:
#         print(f'{text}是奇数')
    
#     play()

# play()

# print('hello')