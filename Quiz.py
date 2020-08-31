# main program file, run this for quiz

import questions

RightAnswers = 0
WrongAnswers = 0

def check_answer(question, keyboard):
    return question.correctAnswer.lower() in keyboard.lower()

def show_question(question):
    global RightAnswers
    global WrongAnswers
    print(question.questionText)
    print("")
    for answer in question.answers:
        print(answer)
        print()
    keyboard = input("Give me ur answer pls: " ) 
    print()

    if check_answer(question, keyboard):
        RightAnswers = RightAnswers + 1
    else:
        WrongAnswers = WrongAnswers + 1

for question in questions.get_questions():
    show_question(question)


print("You got %d correct but got %d wrong" % (RightAnswers, WrongAnswers))
if RightAnswers == 0:
    print("Dismal.")
if WrongAnswers == 0:
    print("Woo, I guess.")

Percentage = 100 * float(RightAnswers) / float(RightAnswers + WrongAnswers)
if WrongAnswers == 0:
    print("You got 100%")
if RightAnswers == 0:
    print("You got 0%")
if RightAnswers >0:
    print("You got %d%%" % (Percentage))

