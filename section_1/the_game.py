# Challenge

# The requirements for the number game are:

# Players get 5 chances
# They have to guess a random number
# It has to be a whole number from 1 to 10
# If they guess wrong, tell them whether the chosen number is higher or lower than their guess
# Tell them how many guesses they've made

import random

random_number = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

while len(guessed_nums) < allowed_guesses:
	guess = input("Guess a number between 1 and 10 --> ")
	try:
		user_num = int(guess)
	except: 
		print("That's not a whole number!")
		break
	if not user_num > 0 or not user_num < 11:
		print("That number is not between 1 and 10")
		break
	guessed_nums.append(user_num)
	if user_num == random_number:
		print("You win! My number was {}.".format(random_number))
		print("It took you {} tries".format(len(guessed_nums)))
		break
	else: 
		if user_num > random_number:
			print("Your guess is too high! Guess #{}".format(len(guessed_nums)))
		else:
			print("Your guess is too low Guess #{}".format(len(guessed_nums)))
			continue

if not random_number in guessed_nums:
	print("Sorry my number was {}".format(random_number))





