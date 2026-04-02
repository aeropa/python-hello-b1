def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  if n <= 1:
    return 1
  return n * factorial(n - 1)

import random

def guessing_game():
  number = random.randint(1, 100)
  attempts = 0
  print("Guess the number between 1 and 100!")
  while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Correct! You got it in {attempts} attempts.")
      break

def main():
  print("hello")
  guessing_game()

if __name__ == "__main__":
  main()
