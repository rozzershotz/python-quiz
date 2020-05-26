import json
import question


def get_questions():
    Questions = []

    with open('questions.json', 'r') as myfile:
        data = myfile.read()

    questionsfile = json.loads(data)

    for jsonQuestion in questionsfile['questions']:

        qquestion = question.Question()

        qquestion.questionText = jsonQuestion["question"]
        qquestion.answers = jsonQuestion["answers"]
        qquestion.correctAnswer = jsonQuestion["correctanswer"]

        Questions.append(qquestion)

    return Questions
