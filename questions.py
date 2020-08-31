# gets questions from json file

import json
import question


def get_questions():
    Questions = []

    # opens, reads and loads data from json file (includes line 14)
    with open('questions.json', 'r') as myfile:
        data = myfile.read()

    questionsfile = json.loads(data)

    # loops questions from json file, 
    for jsonQuestion in questionsfile['questions']:

        # create an instance of the question class
        thisquestion = question.Question()

        # set the data for this question
        thisquestion.questionText = jsonQuestion["question"]
        thisquestion.answers = jsonQuestion["answers"]
        thisquestion.correctAnswer = jsonQuestion["correctanswer"]

        # adds thisquestion to the end of Questions
        Questions.append(thisquestion)

    return Questions
