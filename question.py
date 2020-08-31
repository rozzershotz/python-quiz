# represents a single quiz question

class Question:
    questionText = None
    correctAnswer = None
    answers = []

    def PrintQuestion(self):
        print(self.question)
