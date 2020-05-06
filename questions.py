import json

def get_questions():
    Questions = []

    with open('questions.json', 'r') as myfile:
        data=myfile.read()

    questionsfile = json.loads(data)

    for question in questionsfile['questions']:
        Questions.append(question)

    return Questions