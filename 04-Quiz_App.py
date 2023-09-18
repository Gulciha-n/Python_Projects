class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def CheckAnswer(self,answer):
        return self.answer == answer
        
    
q1 = Question('What is the most important programming language?', ['Java','Python','Javascript','C#'], 'Python')
q2 = Question('What is the best programming language?', ['Python','Javascript','Java','C#'], 'Python')
q3 = Question('What is your favorite programming language?', ['Java','Javascript','C#','Python',], 'Python')
q4 = Question('What is the most populer programming language?', ['Javascript','Java','Python','C#'], 'Python')

print(q1.CheckAnswer('Python'))
print(q2.CheckAnswer('java'))

class Quiz():
    def __init__ (self,questions):
        self.questions = questions
        self.score = 0
        
    














