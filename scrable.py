# Scrable Word Calculator 

# This program takes a word and calculates its point value based on official Scrabble scoring rules.
# Please note: This program does not consider bonus squares on the board.


# These are variables containing letters corresponding to specified points 
one_point_letters = "aeioulnrst"
two_point_letters = "dg"
three_point_letters = "bcmp"
four_point_letters = "fhvwy"
five_point_letters = "k"
eight_point_letters = "jx"
ten_point_letters = "qz"

# This function calculates the number of points for a given word:
def word_calc(word):
  """
  This function calculates the Scrabble word score for a given word.

  """
  points = 0
  for letter in word:
    if letter in one_point_letters:
      points += 1
    elif letter in two_point_letters:
      points += 2
    elif letter in three_point_letters:
      points += 3
    elif letter in four_point_letters:
      points += 4
    elif letter in five_point_letters:
      points += 5
    elif letter in eight_point_letters:
      points += 8
    elif letter in ten_point_letters:
      points += 10
    else:
      raise ValueError(f"Invalid letter found in word: {letter}")
  return points


print("\nHi! Welcome to Scrable Word Calculator.")

# This loop asks for input and continues until a valid word or 'q' is entered .
while True:
    word = input("\nPlease enter a word you want to calculate points for or tyle 'q' to exit program: ").lower().strip()
    # If 'q' is entered, prints goodbye message and exits the program
    if word == 'q':
      print ("\nThank you! Goodbye!\n")
      exit()
    # If a valid word is entered, breaks out of the loop.
    elif word.isalpha():
        break
    # If the input is not alphabetic, it prompts for a valid word
    else:
      print("\nInvalid input. Please enter only alphabetic characters.")

# Calling function to lalculate nymber of points
num_of_points = word_calc(word)

print(f"\nWord: {word}, Points: {num_of_points}\n")