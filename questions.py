def get_questions():
    Questions = []

    Question1 = {}
    Question1["QuestionText"] = "Where does a fish live?."
    Question1["Answers"] = ["Water.io", "H2O", "A compound of nutrients supported in a nuclei-based water mixture * You can just put compound if that's your answer*"]
    Question1["CorrectAnswer"] = "compound"
    
    Questions.append(Question1)
    
    Question2 = {}
    Question2["QuestionText"] = "What is a dog."
    Question2["Answers"] = ["A dog", "A dog", "A dog"]
    Question2["CorrectAnswer"] = "dog" 
    
    Questions.append(Question2)

    Question3 = {}
    Question3["QuestionText"] = "Animals are..."
    Question3["Answers"] = ["Annoying", "Cute", "Not humans"]
    Question3["CorrectAnswer"] = "Not"
    
    Questions.append(Question3)

    return Questions

