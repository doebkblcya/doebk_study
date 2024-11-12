# f = 'song'
# l = 'qiheng'
# fl = f'{f} {l}'
# print(fl.title())

# print('\tpython')

# sb = 'py '
# print(f'{sb.rstrip()}')

# ai = [1,2,3,4]
# # del ai[1]

# # p_ai = ai.pop(2)
# # print(ai)
# # print(p_ai)
# for a in ai:
#     print(a)

# for a in range(6):
#     print(a + 1)

# numbers = list(range(5))
# print(numbers)

# squares = []
# for value in range(1,11):
#     # square = value ** 2
#     squares.append(value ** 2)
# print(squares)

# squares = [value ** 2 for value in range(5)]
# print(squares)

# squares = [value ** 2 for value in range(4)]
# print(squares)

# players = [1,2,3,4]
# print(players[:2])

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color':'green','point':5,'speed':'slow'}
#     aliens.append(new_alien)



# # print(f'total number of aliens:{len(aliens)}')
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:5]:
#     print(alien)
# print('...')

# favorite_language = {
#     'jen':['python','rust'],
#     'sarah':['c'],
#     'edward':['rust','go'],
#     'phil':['python','haskell'],
# }

# for name, languages in favorite_language.items():
#     if len(languages) == 1:
        
#         print(f"\n{name}'s favorite language is {}")
#     else:
#         print(f"\n{name}'s favorite languages are:")
#         for language in languages:
#             print(f'\t{language}')

# user = {
#     'ab':{
#        'first':'a',
#        'last':'b',
#        'location':'china' 
#     },
#     'cd':{
#         'first':'c',
#         'last':'d',
#         'location':'japan' 
#     }
# }

# for user_name,user_info in user.items():
#     print(f'\nusername:{user_name}')
#     full_name = f'{user_info['first']}{user_info['last']}'
#     location = user_info['location']

#     print(f'\tfullname:{full_name}')
#     print(f'\tlocation:{location.title()}')

# current_number = 0

# while current_number <= 6:
#     print(current_number)
#     current_number += 1

# prompt = '\nnishushenmewohuishenme'
# prompt += '\nshuruquitlikai'

# message = ''

# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# unconfirmed_users = ['a','b','c']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f'verifying user:{current_user}')

#     confirmed_users.append(current_user)

# print('\nthe following user have been confirmed')
# for confirmed_user in confirmed_users:
#     print(f'\t{confirmed_user}')

# responses = {}

# polling_active = True

# while polling_active:
#     name = input('\nwhat is your name?')
#     response = input('which mountain would you like to climb someday?')

#     responses[name] = response

#     repeat = input('again?')
#     if repeat == 'no':
#         polling_active = False

# print('\n=== Poll Result ===')
# for name,response in responses.items():
#     print(f'{name} would like to climb {response}')

# print(responses)

# def build(first,second,age=None):
#     person = {'1st':first,'2nd':second}
#     if age:
#         person['age'] = age
#     return person

# mu = build('song','qiheng',age=21)
# print(mu)

# def get_name(first_name,second_name):
#     full_name = f'{first_name}{second_name}'
#     return full_name.title()

# while True:
#     print('\nplz enter your name')
#     print('enter q to quit')

#     f_name = input('first name is:')
#     if f_name == 'q':
#         break
#     s_name = input('second name is:')
#     if s_name == 'q':
#         break

#     name = get_name(f_name,s_name)
#     print(f'\nhello,{name}!')

# def greet_users(names):
#     for name in names:
#         msg = f'\nhello,{name.title()}!'
#         print(msg)

# usernames = ['jack','rose','sqh']
# greet_users(usernames)

# un = ['1','2','3']
# done = []

# while un:
#     cu = un.pop()
#     print(f'printing:{cu}')
#     done.append(cu)

# print('\nthe following has been printed:')
# for do in done:
#     print(do)

# def printing(uns,dones):
#     while uns:
#         cu = uns.pop()
#         print(f'printing:{cu}')
#         dones.append(cu)

# def show(dones):
#     print('\nthe following has been printed:')
#     for done in dones:
#         print(done)

# uns = ['1','2','3']
# dones = []

# printing(uns[:],dones)
# show(dones)

# print(uns)

# def a(*b):
#     print('1111111:')
#     for c in b:
#         print(f'{c}')

# a('1','2')

# def build_profile(first,last,**user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('s','q',)

# class Dog:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(f'{self.name} is now sitting')
    
#     def roll_over(self):
#         print(f'{self.name} rolled over')

# my_dog = Dog('sqq',6)
# your_dog = Dog('qqs',3)

# # print(f'my dog is called {my_dog.name}')
# # print(f'my dog is {my_dog.age} years old')

# # my_dog.sit()
# # my_dog.roll_over()

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_d_name(self):
#         long_name = f'{self.make} {self.model} {self.year}'
#         return long_name
    
#     def read_o(self):
#         print(f'this car has {self.odometer_reading} miles on it')

# my_new_car = Car('audi','a4',2024)
# print(my_new_car.get_d_name())
# my_new_car.read_o()


# path = Path('daiban.txt')
# contents = path.read_text()
# print(contents)
from pathlib import Path

class Survey:
    def __init__(self,question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self,new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print('survey result:')
        for response in self.responses:
            print(f'- {response}')

