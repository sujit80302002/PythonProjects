import random

from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#funcion to check the user's number with the actual answer
def check_answer(guess, answer, turns):
  """Checks the answer against guess. Returns the number of guesses remaining."""
  if guess > answer:
    print("Too High")
    return turns -1
  elif guess < answer:
    print("Too Low")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}.")
 #Make functiion to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    

def game():
  print("Welcome to the Number Guessing Game!")
  #Choosing a number between 1 and 100.
  print("I'm thinking of a number between 1 and 100.")
  answer =  random.randint(1,100)
  
  turns = set_difficulty()
  guess = 0
  #Repeat the functionality if they get it wrong
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
  #Let the user guess a number
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, You lose.")
      return 
    elif guess != answer:
      print("Guess again")
game()
#Track the user's attemps and reduce the number by 1 if user gueses wrong 

  
