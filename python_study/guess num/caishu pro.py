import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts_left = max_attempts
    
    while attempts_left > 0:
        try:
            guess = int(input("请输入一个1到100之间的整数："))
            
            if guess == secret_number:
                print("恭喜你猜对了！")
                break
            elif guess < secret_number:
                print("太小了，请再试一次。")
            else:
                print("太大了，请再试一次。")
            
            attempts_left -= 1
            print(f"剩余猜测次数：{attempts_left}")
            
        except ValueError:
            print("输入错误，请输入一个整数。")
    
    else:
        print(f"游戏结束，正确答案是{secret_number}。")
    
    play_again = input("是否继续游戏？(输入 'y' 继续，其他键退出)：")
    if play_again.lower() == 'y':
        guess_number_game()
    else:
        print("谢谢参与，游戏结束。")

# 启动猜数游戏
guess_number_game()