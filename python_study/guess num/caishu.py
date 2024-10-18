import random

num = random.randint(1,10)

while True:
    guess = int(input('输入数字:'))

    if guess == num:
        print('win')
        break

    elif guess > num:
        print('bigger')
    else:
        print('smaller')
    