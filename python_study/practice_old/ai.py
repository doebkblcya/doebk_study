""" num1 = 1
num2 = 2

result = num1 + num2

print(result) """

#整数相加
""" text = input('请输入：')

nums = text.split(' ')
result = 0

while len(nums):
    num = int(nums.pop())

    result += num

print(f'结果为：{result}') """

#for 语句


""" sbs = ['小谁','咋了了','哦哦哦']

while True:
    print('当前名单：',sbs)

    name = input('请输入学生姓名输入n结束：')

    if name == 'n':
        break
    else:
        sbs.append(name)

two_words_count = 0
three_words_count = 0

for name in sbs:
    words_count = len(name)
     
    if words_count == 2:
        two_words_count += 1
    elif words_count ==3:
        three_words_count += 1
    
print(f"三个字的有{three_words_count}个，两个字的有{two_words_count}个") """

#函数
""" def check_pw(password):
    if len(password) < 3:
        return False
    else:
        return True
    
while True:
    pw = input('请输入密码登录：')

    if check_pw and pw == 'abcd':
        print('登陆成功')
        break
    else:
        print('密码错误或者不合理，重新：')

while True:
    panduan = input('是否修改密码输入y：')

    if panduan == 'y':
        break
    else:
        print('bye')

while True:
    pw = input('现在可以修改密码请输入新的：')

    if check_pw(pw):
        print('success')
        break
    else:
        print('fail') """

#集合
""" numbers = set()

numbers.add(3)
numbers.add(2)
numbers.add(1)

print(numbers)

table = {'name':'-','age':0}

while table['name'] == '-' or table['age'] == 0:
    my_name = input('请输入你的姓名：')
    my_age = input('请输入你的年龄:')

    if my_name:
        table['name'] = my_name
    
    if my_age:
        table['age'] = int(my_age)
    
print(table) """

""" fail_count = 0
allow_input = True

while allow_input:
    message = f"已经输入错{fail_count }次  请输入密码："
    pw = input(message)

    if pw == "123456":
        print("stupid")
        fail_count += 1
    
    if fail_count == 3:
        print("over")
        allow_input = False """

#类
""" class player:

    def __init__(self):
        self.hp = 100

p1 = player()
p2 = player()

p1.hp -= 10
p2.hp -= 20

print(f'玩家1剩余生命值{p1.hp}')
print(f'玩家2剩余生命值{p2.hp}') """

#类的构造方法

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

for sb in students:
    total_score = sb.sum_score()
    print(f'学生{sb.name}年龄{sb.age}成绩{total_score}')
 """

""" class unit:

    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

class hero(unit):
    
    def __init__(self, hp, power,name):
        super().__init__(hp, power)
        self.name = name

hero_name = input('取个名字:')

Hero =  hero(100,10,hero_name)
Enemy = unit(100,10)

print(f'玩家状态:英雄{Hero.name},hp{Hero.hp},pw{Hero.power}')
print(f'敌人状态:hp{Enemy.hp},pw{Enemy.power}')
 """

