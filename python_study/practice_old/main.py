# import information

# message = information.welcome()

# print (message)

from pathlib import Path

path = Path('daiban.txt')
contents = path.read_text()
print(contents)