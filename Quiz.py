# main program file, run this for quiz

# imports questions.py
import questions

RightAnswers = 0
WrongAnswers = 0 

# checks if the answer from the keyboard contains the right answer 
def check_answer(question, keyboard):
    return question.correctAnswer.lower() in keyboard.lower()

# displays the question to the user, takes the answer from the user and checks if it is right
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

# shows the questions 
for question in questions.get_questions():
    show_question(question)

# prints how many you got wrong and right
print("You got %d correct and got %d wrong" % (RightAnswers, WrongAnswers))
if RightAnswers == 0:
    print("Dismal.")
if WrongAnswers == 0:
    print("Woo, I guess.")

# prints how much you got in a percentage 
if WrongAnswers == 0:
    print("You got 100%")
if RightAnswers == 0:
    print("You got 0%")
if RightAnswers > 0 and WrongAnswers > 0:
    Percentage = 100 * float(RightAnswers) / float(RightAnswers + WrongAnswers)
    print("You got %d%%" % (Percentage))

