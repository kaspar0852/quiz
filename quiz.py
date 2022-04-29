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
 "what is the capital of Chile?: ": "D",
 "What is the highest mountain in the world: ": "B",
 "what is the smallest country in the world?: ": "C",
 "What is the largest country in the world?: ": "A",
 "How many players are there in a rugby team?:": "C",
 "Who won the FIFA  Women's World Cup in 2019?:": "D",
 "What is the fastest memory in a computer?: ": "B",
 "What is the capital of Finland?:": "D",
 "What is the name of the lead singer of Guns and Roses?: ": "A",
 "Alberta is a provvince of which country: ": "A",
}

options = [["A. Rome", "B. Kathmandu", "C. New Delhi", "Santiago"],
          ["A. K2", "B. Everest", "C. Manaslu", "D. Mardi"],
          ["A. Nepal", "India", "C. USA", "Vatican City"],
          ["A. Russia","B. Spain", "C. England", "D. Nepal"],
          ["A. 11","B. 12", "C. 13", "D. 10"],
          ["A. Canada","B. Spain", "C. England", "D. USA"],
          ["A. Cache","B. RAM", "C. HDD", "D. SSD"],
          ["A. Sample","B. Dubai", "C. England", "D. Helsinki"],
          ["A. Axel Rose","B. Gustavo", "C. Arjit Singh", "D. Pramod Kharel"],
          ["A. Canada","B. Spain", "C. England", "D. Nepal"],]


start_quiz()

while play_again():
    start_quiz()
    
print("Have a nice day")