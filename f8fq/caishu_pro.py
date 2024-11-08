import random
import tkinter as tk
from PIL import Image,ImageTk
from playsound import playsound
import threading

def guess_number_game():
    secret_number = random.randint(1, 100)
    # secret_number = 13
    max_attempts = 5
    attempts_left = max_attempts
    
    while attempts_left > 0:
        try:
            guess = int(input("请输入一个1到100之间的整数："))
            
            if guess == secret_number:
                print("恭喜你猜对了！")
                print('奖励你入飞门')
                show_image('f8fq.jpg','wa_ao.mp3')
                break
            elif guess < secret_number and 1 <= guess <= 100:
                print("太小了，请再试一次。")
            elif guess > secret_number and 1 <= guess <= 100:
                print("太大了，请再试一次。")
            else:
                print('麻辣隔壁叫你输一到一百看不懂啊')
            
            attempts_left -= 1
            print(f"剩余猜测次数：{attempts_left}")
            
        except ValueError:
            print("输入错误，请输入一个整数。")
    
    else:
        print(f"游戏结束，正确答案是{secret_number}。")
        print('哇奥')
        show_image("gun_mu.jpg",'wa_ao.mp3')
    
    play_again = input("是否继续游戏？(输入 'y' 继续，其他键退出)：")
    if play_again.lower() == 'y':
        guess_number_game()
    else:
        print("谢谢参与，游戏结束。")

def play_audio(audio_path):
    # 播放音频
    playsound(audio_path)

def show_image(image_path,audio_path):
    # 创建主窗口
    
    root = tk.Tk()
    root.title("哇奥")

    # 打开并调整图片
    img = Image.open(image_path)
    img = img.resize((400, 400))  # 可根据需要调整尺寸
    img_tk = ImageTk.PhotoImage(img)

    # 创建标签以显示图片
    label = tk.Label(root, image=img_tk)
    label.image = img_tk  # 保持引用
    label.pack()

    audio_thread = threading.Thread(target=play_audio, args=(audio_path,))
    audio_thread.start()

    # 运行窗口循环
    root.mainloop()
    



guess_number_game()