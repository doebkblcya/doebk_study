# nums = range(0,101)
# answer = 0
# for num in nums:
#     answer = answer + num
# print(answer)

# import random

# wins = 0
# loses = 0
# ties = 0

# def start():
#     print('请输入r、p或s来选择：石头 (r)、剪刀 (s)、布 (p)')
#     action = input().lower()
#     while action not in ['r', 'p', 's']:
#         print("无效输入，请输入 'r'（石头）、's'（剪刀）或 'p'（布）:")
#         action = input().lower()
#     return action

# def random_action():
#     ene_action = random.choice(['r','p','s'])
#     return ene_action

# def win():
#     print('赢了')
#     wins += 1
# def lose():
#     print('输了')
#     loses += 1
# def tie():
#     print('平局')
#     ties += 1
    
# while True:
#     start()
#     random_action()
    
#     if action == ene_action:
#         tie()
#     elif action == 'r' and ene_action == 'p':
#         lose()
#     elif action == 'r' and ene_action == 's':
#         win()
#     elif action == 'p' and ene_action == 'r':
#         win()
#     elif action == 'p' and ene_action == 's':
#         lose()
#     elif action == 's' and ene_action == 'r':
#         lose()
#     elif action == 's' and ene_action == 'p':
#         win()

#     print('再来一次？输入no退出，回车继续')
#     again = input()
#     if again == 'no':
#         break

# import random

# class Game:
#     def __init__(self):
#         self.wins = 0
#         self.loses = 0
#         self.ties = 0
    
#     def win(self):
#         print('赢了')
#         self.wins += 1
#     def lose(self):
#         print('输了')
#         self.loses += 1
#     def tie(self):
#         print('平局')
#         self.ties += 1
    
#     def decide(self,player_action,computer_action):
#         if player_action == computer_action:
#             self.tie()
#         elif (player_action == 'r' and computer_action == 's') or (player_action == 'p' and computer_action == 'r') or (player_action == 's' and computer_action == 'p'):
#             self.win()
#         else:
#             self.lose()
    
#     def show_score(self):
#         print(f'当前比分 - 胜: {self.wins}, 负: {self.loses}, 平: {self.ties}')
    
#     def main(self):
#         while True:
#             print('请输入r、p或s来选择：石头 (r)、剪刀 (s)、布 (p)')
#             player_action = input().lower()
#             while player_action not in ['r', 'p', 's']:
#                 print("无效输入，请输入 'r'（石头）、's'（剪刀）或 'p'（布）:")
#                 player_action= input().lower()
#             computer_action = random.choice(['r','p','s'])
            
#             print(f'电脑选择了: {computer_action}')
#             self.decide(player_action,computer_action)
            
#             self.show_score()
            
#             print('再来一次？输入no退出，回车继续')
#             again = input().lower()
#             if again == 'no':
#                 break

# game = Game()
# game.main()


# import random
# import tkinter as tk
# from tkinter import messagebox

# # 初始化计数器
# wins = 0
# loses = 0
# ties = 0

# # 判断输赢的函数
# def decide(player_action, computer_action):
#     global wins, loses, ties
#     if player_action == computer_action:
#         result = '平局'
#         ties += 1
#     elif (player_action == 'r' and computer_action == 's') or \
#          (player_action == 'p' and computer_action == 'r') or \
#          (player_action == 's' and computer_action == 'p'):
#         result = '赢了'
#         wins += 1
#     else:
#         result = '输了'
#         loses += 1
#     return result

# # 显示当前比分
# def show_score():
#     score_label.config(text=f'当前比分 - 胜: {wins}, 负: {loses}, 平: {ties}')

# # 转换函数，将 r、p、s 转换为 石头、布、剪刀
# def action_to_text(action):
#     if action == 'r':
#         return '石头'
#     elif action == 'p':
#         return '布'
#     elif action == 's':
#         return '剪刀'

# # 玩家选择
# def player_choice(choice):
#     global wins, loses, ties
#     player_action = choice
#     computer_action = random.choice(['r', 'p', 's'])
    
#     computer_label.config(text=f'电脑选择了: {action_to_text(computer_action)}')

#     result = decide(player_action, computer_action)
#     result_label.config(text=f'结果: {result}')
#     show_score()

# # 创建主窗口
# window = tk.Tk()
# window.title('石头剪刀布')

# # 设置窗口大小
# window.geometry('600x500')

# # 显示电脑选择
# computer_label = tk.Label(window, text="电脑选择了: ", font=("Arial", 12))
# computer_label.pack(pady=20)

# # 显示结果
# result_label = tk.Label(window, text="结果: ", font=("Arial", 12))
# result_label.pack(pady=20)

# # 显示分数
# score_label = tk.Label(window, text="当前比分 - 胜: 0, 负: 0, 平: 0", font=("Arial", 12))
# score_label.pack(pady=20)

# # 玩家按钮
# button_frame = tk.Frame(window)
# button_frame.pack(pady=20)

# rock_button = tk.Button(button_frame, text="石头 (r)", width=10, command=lambda: player_choice('r'))
# rock_button.grid(row=0, column=0, padx=5)

# paper_button = tk.Button(button_frame, text="布 (p)", width=10, command=lambda: player_choice('p'))
# paper_button.grid(row=0, column=1, padx=5)

# scissors_button = tk.Button(button_frame, text="剪刀 (s)", width=10, command=lambda: player_choice('s'))
# scissors_button.grid(row=0, column=2, padx=5)

# # 启动窗口
# window.mainloop()

# import random

# # 判断输赢的函数
# def decide(player_action, computer_action):
#     if player_action == computer_action:
#         return '平局'
#     elif (player_action == 'r' and computer_action == 's') or \
#          (player_action == 'p' and computer_action == 'r') or \
#          (player_action == 's' and computer_action == 'p'):
#         return '赢了'
#     return '输了'

# # 获取有效的玩家输入
# def get_player_choice():
#     valid_choices = ['r', 'p', 's']
#     while True:
#         player_action = input("请输入r、p或s来选择：石头 (r)、剪刀 (s)、布 (p): ").strip().lower()
#         if player_action in valid_choices:
#             return player_action
#         print("无效输入，请输入 'r'（石头）、's'（剪刀）或 'p'（布）:")

# # 显示当前比分
# def show_score(wins, loses, ties):
#     print(f'当前比分 - 胜: {wins}, 负: {loses}, 平: {ties}')

# # 主程序
# def main():
#     wins, loses, ties = 0, 0, 0  # 初始化计数器

#     while True:
#         # 获取玩家输入
#         player_action = get_player_choice()

#         # 电脑随机选择
#         computer_action = random.choice(['r', 'p', 's'])
#         print(f'电脑选择了: {action_to_text(computer_action)}')

#         # 判断输赢并更新计数器
#         result = decide(player_action, computer_action)
#         if result == '平局':
#             ties += 1
#         elif result == '赢了':
#             wins += 1
#         else:
#             loses += 1

#         print(result)  # 显示结果
#         show_score(wins, loses, ties)  # 显示比分

#         # 询问是否再玩一次
#         if input('再来一次？输入no退出，回车继续').strip().lower() == 'no':
#             break

# # 转换函数，将 r、p、s 转换为 石头、布、剪刀
# def action_to_text(action):
#     return {'r': '石头', 'p': '布', 's': '剪刀'}.get(action, '未知')

# # 启动游戏
# main()
    
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
 
# t = Test()
# t.prt()

# def a():
#     print(b)

# b = 1
# a()
# print(b)

# import time, sys
# indent = 0  #  How  many  spaces to indent. 


# indentIncreasing = True # Whether the indentation is increasing or not. 



# # try: 


# while True: # The main program loop. 
#     print('  ' *  indent,  end='') 
#     print('********') 


#     time.sleep(0.1) # Pause for 1/10 of a second. 



#     if indentIncreasing: 


#         #  Increase  the  number  of  spaces: 
#         indent  =  indent  +  1
#         if indent  ==  20: 


#             #  Change  direction: 
#             indentIncreasing = False
#     else: 


#         # Decrease the number of spaces: 
#         indent  =  indent - 1
#         if indent == 0: 


#             # Change  direction:
#             indentIncreasing = True
# # except KeyboardInterrupt: 
# #     sys.exit()

# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     else:
#         return 3 * number + 1


# def main():
#     num = int(input())
#     while num != 1:
#         num = collatz(num)
#         print(num)

# main()

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

# if name in birthdays:
#     print(birthdays[name] + ' is the birthday of ' + name)
# else:
#     print('I do not have birthday information for ' + name)
#     print('What is their birthday?')
#     bday = input()
#     birthdays[name] = bday
#     print('Birthday database updated.')
#     print(birthdays)

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'

# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
    
#     move = input()



#     if move not in theBoard:
#         print("Invalid move. Please try again.")
#         continue
    
#     if theBoard[move] != ' ':
#         print("This space is already taken. Please try again.")
#         continue
    
#     theBoard[move] = turn
#     if turn == 'X':


#         turn = 'O'


#     else:


#         turn = 'X'


# printBoard(theBoard)

