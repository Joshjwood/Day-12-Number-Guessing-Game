from art import logo
from random import randrange
from replit import clear

def pickanumber():
  return(randrange(1, 100))

lowest_score = 10

def play_game():
  global lowest_score
  print(logo)

  print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")

  difficulty = 0
  difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty_choice == "easy":
    difficulty = 10
  elif difficulty_choice == "hard":
    difficulty = 5

  print(f"On {difficulty_choice} mode, you have {difficulty} attempts.\n")

  secret_number = pickanumber()
  #print(f"Secret number debug: {secret_number}")


  while difficulty > 0:
    guess = int(input("Make a guess: "))
    print(f"Debug: Difficulty is {difficulty}, lowest score is {lowest_score}")
    if guess > secret_number:
      print("Too high")
      difficulty -= 1
    elif guess < secret_number: 
      print("Too low")
      difficulty -= 1
    elif guess == secret_number:
      print("You got it!")
      winning_pick = difficulty
      difficulty = 0

  #print("You made it out of the loop.")
  if guess == secret_number:
    print(f"You guessed {guess}, the secret number was {secret_number}. You win this round.")
    if difficulty < lowest_score:
      lowest_score = winning_pick + 1
      print(f"Your lowest score so far is {lowest_score} guesses.")
  elif guess != secret_number:
    print(f"You're out of lives, you lose.\nThe secret number was {secret_number}\n")

while input(f"Do you want to play The Number Guessing Game? 'y' or 'n': ") == "y":
  clear()
  play_game()