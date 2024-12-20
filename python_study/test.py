while True:
    s = input()  # 读取用户输入的一行字符串
    s = s.replace("你", "我")  # 将字符串中的 "你" 替换为 "我"
    s = s.replace("吗", "")  # 将字符串中的 "吗" 删除
    s = s.replace("？", "！")  # 将字符串中的 "？" 替换为 "！"
    print(s)