# f = open('C:/Users/songqiheng/Desktop/lets_do_it.txt', encoding='utf-8')
# contents = f.read()
# print(contents)
# f.close()

# from pathlib import Path

# path = Path(
#     'C:/Users/songqiheng/Desktop/123.txt'
# )

# contents = path.read_text()
# print(contents)

# lines = contents.splitlines()
# # for line in lines:
# #     print(line)
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

# from pathlib import Path

# try:
#     path = Path('C:/Users/songqiheng/Desktop/lets_do_it.txt')
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print('sorry')
# else:
#     print(contents)

from pathlib import Path
import json

# numbers = [2,3,5,7,11,13]

# contents = json.dumps(numbers)
# path.write_text(contents)

# path = Path('number.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)

# username = input('what is your name')

# contents = json.dumps(username)
# path.write_text(contents)

# print(f'we will remember you when you come back again,{username}')

# contents = path.read_text()
# username = json.loads(contents)

# print(f'welcome back,{username}')


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input('123')
    contents = json.dumps(username)
    path.write_text(contents)
    return username
    

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        print(f'hello,{username}')
    else:
        username = get_new_username(path)
        print(f'new {username}')

greet_user()

