from book import Survey

question = 'how old are you'
age_survey = Survey(question)

age_survey.show_question()
print('enter q to quit\n')
while True:
    response = input('age:')
    if response == 'q':
        break
    age_survey.store_response(response)

print('\nthanks')
age_survey.show_results()