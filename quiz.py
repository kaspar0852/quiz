def start_quiz():
    guesses = []
    correct_guesses = 0
    question_num =1 
    
    for key in questions:
        print("---------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
            
        guess = input("Enter(A,B,C,D):")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num+= 1
        
    display_score(correct_guesses,guesses)
    inp = input("do you want to add new questions?")
    inp = inp.upper()
    
    if inp == "YES":
        new_ques()
         
    
#----------------------------------------
def check_answer(answer,guess):
    max = 10
    if answer == guess:
         print("correct!") 
         return max
    else:
         print("INCORRET")
         return max-15
     
def display_score(corret_guesses,guesses):
    print("---------------------------------")
    print("Results")
    print("----------------------------------")
    
    print("Answers:", end =" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    
    print("Guesses:", end =" ")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int(corret_guesses)
    print("Your score is : "+str(score))
    
def add_new_questions():
    response = input("do you want to add more questions?")
    response = response.upper()
    
    if response == "YES":
        return 
    
def play_again():
    response = input("do you want to play again?")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False

def new_ques():
        ''' print("current set of question is",questions) '''
        new_q = input("Enter a new question: ")
        new_a =input("enter the new question answer: ")
        new_o_a = input("enter new options A: ")
        new_o_b = input("enter new options B: ")
        new_o_c = input("enter new options C: ")
        new_o_d = input("enter new options D: ")
        
        questions[new_q] = new_a
        
        options.append([new_o_a,new_o_b,new_o_c,new_o_d])
        
        start_quiz()
        
        ''' print("the new question set with its  answer are ", questions) '''
        '''  print("the new options are ",options) '''
    
      
              
    
questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]


start_quiz()

while play_again():
    start_quiz()
    
print("Have a nice day")