class Question:
    question = None
    correctanswer = None
    answers = []

    def PrintQuestion(self):
        print(self.question)


TestQuestion1 = Question()
TestQuestion1.question = "what instance is mr bean in starwars battlefront 2"

TestQuestion2 = Question()
TestQuestion2.question = "if 4 + 4 is 9, then when will Esa not ask a question"

TestQuestion3 = Question()
TestQuestion3.question = "The Moorheads are simple folk. They enjoy screaming by the fire and rage over Donkey Kong Batlle Mania 6"

TestQuestion1.PrintQuestion() 
TestQuestion2.PrintQuestion()
TestQuestion3.PrintQuestion()