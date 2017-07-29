''' Shreya's Spelling Bee words game for Spelling Practice
read original list of words
ask for length of a word. ex 3 letter words
get a random word from the words list
save the generated word to a temporary list
ask for confirmation to continue
when negative confirmation save the temporary list to a file based on timestamp and exit

author : nirajkvinit@yahoo.co.in
'''
from __future__ import print_function
import random
import datetime
import csv
import os
import sys
import platform
import colorama


def clear_screen():
	''' Clears the screen '''
	command = "-cls" if platform.system().lower() == "windows" else "clear"
	os.system(command)


def get_words_list(words_file=None):
	''' get words list from a file containing words '''
	# File containing words
	words_list_file = 'wordslist.csv'
	# Words List to be returned
	words_list = None
	# if words_file is not provided then use the default one
	if words_file is None:
		words_file = words_list_file
	# read words file to a words list
	try:
		with open(words_file, 'r') as csv_file:
			# get the first item from the resulting list as it contains the list of words as list
			words_list = list(csv.reader(csv_file))[0]
	except FileNotFoundError:
		print('Dictionary File not found!')
	except IOError:
		print('Error reading the dictionary file.')
	return words_list


def get_random_word(words_list=None, begins_with=None, word_length=None):
	''' core function which extracts random words from words list '''
	found_word = None
	if words_list is not None:
		# get the length of the words_list after getting the words from the file to this list
		words_list_length = len(words_list)
		# Generate a random number between 1 and the number of total words in the words list
		random_number = random.randint(1, (words_list_length - 1))
		# get a random word from the list
		found_word = words_list[random_number]
	if found_word is not None:
		if begins_with is not None:
			found_word = found_word if found_word.startswith(begins_with) else None
	if found_word is not None:
		if word_length is not None:
			found_word = found_word if len(found_word) == int(word_length) else None
	return found_word


def shreya_words_game(words_list):
	''' Entry point of shreya's word game.'''
	if words_list is None:
		print('Error! Words list not available! Exiting the game!')
		sys.exit()
	while True:
		clear_screen()
		print(colorama.Fore.WHITE + colorama.Back.GREEN + 'Welcome to Shreya\'s Words Game!')
		print(colorama.Style.RESET_ALL)
		print('Please select your Game: \n')
		# Random Words
		print('1. Random words.')
		# Random words where the word begins with a desired letter
		print('2. Random words of desired first alphabet.')
		# Random words of desired length
		print('3. Random words of desired word length.')
		# Random words of desired length and alphabet
		print('4. Random words of desired word length and alphabet. \n')
		print(colorama.Fore.WHITE + colorama.Back.RED + 'Press \'q\' to exit the game.')
		print(colorama.Style.RESET_ALL)
		game_choice = str(input('Please input your choice: ')).strip().lower()
		if game_choice == 'q':		# Quit
			break
		elif game_choice == '1':		# 1. Random words - Any.
			random_word_any(words_list)
		elif game_choice == '2':		# 2. Random words of desired first letter.
			random_word_by_letter(words_list)
		elif game_choice == '3':		# 3. Random words of desired word length.
			random_word_by_length(words_list)
		elif game_choice == '4':		# 3. Random words of desired word length.
			random_word_by_length_letter(words_list)
		else:
			input('Your input was incorrect! Press \'Enter\' key to try again!')
	clear_screen()
	goodbye_message = 'Thank you for playing Shreya\'s Game! Goodbye!'
	print(colorama.Fore.WHITE + colorama.Back.MAGENTA + goodbye_message)
	print(colorama.Style.RESET_ALL)


def random_word_by_length(words_list):
	''' Get random words by desired word length '''
	exercise_list = get_exercise_list()
	found_word = None
	while True:
		try:
			clear_screen()
			print('\n'*3)
			desired_word_length = int(input('Please input a number between 1 and 14: '))
			# We are only going to generate words of minimum 1 and 14 letters
			if desired_word_length in range(1, 15):
				break
			else:
				input("You must input a number between 1 and 14. Hit Enter to try again.")
		# In exception We will just ask the user to input correct number again
		except ValueError:
			print('Please enter a number.')
	while True:
		# Loop should not run indefinitely.
		word_not_found_loop_count = 0
		while True:
			# Increase the counter if a word is not found
			word_not_found_loop_count += 1
			# get a random word
			found_word = get_random_word(words_list=words_list, word_length=desired_word_length)
			if found_word is not None:
				# Since word has been found. Reset the counter
				word_not_found_loop_count = 0
				# append the found word to exercise list
				get_exercise_list(exercise_list, found_word)
				break
			# Break the loop and exit the program if a word is not found after 1000 iteration
			if word_not_found_loop_count > 1000:
				str_message = 'Sorry! Words of ' + str(desired_word_length)
				str_message += ' characters long are not available. Press Enter to continue.'
				input(str_message)
				found_word = None
				break
		if found_word is not None:
			# Print Found word!
			print_found_word(found_word)
		if word_not_found_loop_count > 1000:
			break
		str_message = colorama.Fore.WHITE + colorama.Back.RED
		str_message += "Press 'Enter' to continue or 'q' to exit the game: "
		game_choice = str(input(str_message)).lower()
		print(colorama.Style.RESET_ALL)

		if game_choice == 'q':
			break

	save_exercise_list(exercise_list)
	return None


def random_word_by_letter(words_list):
	''' Get random word by desired alphabet '''
	exercise_list = get_exercise_list()
	found_word = None
	while True:
		clear_screen()
		print('\n'*3)
		desirable_alphabet = str(input('Please input an alphabet: '))
		# We are only going to generate words of minimum 1 and 14 letters
		if len(desirable_alphabet) == 1 and desirable_alphabet.isalpha():
			desirable_alphabet = desirable_alphabet.lower()
			break
		else:
			input("You must input an alphabet. Hit Enter to try again.")
	while True:
		# Loop should not run indefinitely.
		word_not_found_loop_count = 0
		while True:
			# Increase the counter if a word is not found
			word_not_found_loop_count += 1
			# get a random word
			found_word = get_random_word(words_list=words_list, begins_with=desirable_alphabet)
			if found_word is not None:
				# Since word has been found. Reset the counter
				word_not_found_loop_count = 0
				# append the found word to exercise list
				get_exercise_list(exercise_list, found_word)
				break
			# Break the loop and exit the program if a word is not found after 1000 iteration
			if word_not_found_loop_count > 1000:
				str_message = 'Sorry! Words of ' + str(desirable_alphabet)
				str_message += ' characters are not available. Press Enter to continue.'
				input(str_message)
				found_word = None
				break
		# Clear screen
		if found_word is not None:
			# Print Found word!
			print_found_word(found_word)
		if word_not_found_loop_count > 1000:
			break
		str_message = colorama.Fore.WHITE + colorama.Back.RED
		str_message += "Press 'Enter' to continue or 'q' to exit the game: "
		game_choice = str(input(str_message)).lower()
		print(colorama.Style.RESET_ALL)
		if game_choice == 'q':
			break
	save_exercise_list(exercise_list)
	return None


def random_word_by_length_letter(words_list):
	''' Get random word by desired alphabet and desired length of a word '''
	# pylint: disable=too-many-branches
	exercise_list = get_exercise_list()
	found_word = None
	desired_word_length = 0
	# Get desired Alphabet
	while True:
		clear_screen()
		print('\n'*3)
		desirable_alphabet = str(input('Please input an alphabet: '))
		# We are only going to generate words of minimum 1 and 14 letters
		if len(desirable_alphabet) == 1 and desirable_alphabet.isalpha():
			desirable_alphabet = desirable_alphabet.lower()
			break
		else:
			input("You must input an alphabet. Hit Enter to try again.")
	# Get desired word length
	while True:
		try:
			clear_screen()
			print('\n'*3)
			desired_word_length = int(input('Please input a number between 1 and 14: '))
			# We are only going to generate words of minimum 1 and 14 letters
			if desired_word_length in range(1, 15):
				break
			else:
				input("You must input a number between 1 and 14. Hit Enter to try again.")
		# In exception We will just ask the user to input correct number again
		except ValueError:
			print('Please enter a number.')
	while True:
		# Loop should not run indefinitely.
		word_not_found_loop_count = 0
		while True:
			# Increase the counter if a word is not found
			word_not_found_loop_count += 1
			# get a random word
			found_word = get_random_word(words_list, desirable_alphabet, desired_word_length)
			if found_word is not None:
				# Since word has been found. Reset the counter
				word_not_found_loop_count = 0
				# append the found word to exercise list
				get_exercise_list(exercise_list, found_word)
				break
			# Break the loop and exit the program if a word is not found after 1000 iteration
			if word_not_found_loop_count > 1000:
				str_message = 'Sorry! Words of ' + str(desirable_alphabet)
				str_message += ' characters are not available. Press Enter to continue.'
				input(str_message)
				found_word = None
				break
		# Clear screen
		if found_word is not None:
			# Print Found word!
			print_found_word(found_word)
		if word_not_found_loop_count > 1000:
			break
		str_message = colorama.Fore.WHITE + colorama.Back.RED
		str_message += "Press 'Enter' to continue or 'q' to exit the game: "
		game_choice = str(input(str_message)).lower()
		print(colorama.Style.RESET_ALL)

		if game_choice == 'q':
			break

	save_exercise_list(exercise_list)
	return None


def random_word_any(words_list):
	''' get any random word '''
	exercise_list = get_exercise_list()
	while True:
		# get a random word
		found_word = get_random_word(words_list)
		# append the found word to exercise list
		get_exercise_list(exercise_list, found_word)
		# Print Found word!
		print_found_word(found_word)
		str_message = colorama.Fore.WHITE + colorama.Back.RED
		str_message += "Press 'Enter' to continue or 'q' to exit the game: "
		game_choice = str(input(str_message)).lower()
		print(colorama.Style.RESET_ALL)
		if game_choice == 'q':
			break
	save_exercise_list(exercise_list)
	return None


def print_found_word(found_word):
	''' Print found word in colorful format '''
	clear_screen()
	print(colorama.Fore.WHITE + colorama.Back.CYAN + 'Random Words Game!')
	print(colorama.Style.RESET_ALL)
	print('\n' * 3)
	print('{0: ^20}'.format(found_word))
	print('\n' * 3)


def get_exercise_list(exercise_list=None, found_word=None):
	''' Get current game's exercise list or add word to the exercise list '''
	if exercise_list is None:
		return []
	elif found_word is None:
		return exercise_list
	else:
		if found_word not in exercise_list:
			exercise_list.append(found_word)
		return exercise_list


def save_exercise_list(exercisewords_list):
	''' Save current game's exercise list in a timestamped file '''
	exercise_words_list_length = len(exercisewords_list)
	if exercise_words_list_length > 0:
		try:
			# Get dir path where this file is residing
			current_dir = str(os.path.dirname(os.path.abspath(__file__)))
			# timestamped exercise file
			new_file_name = current_dir + '/exercises/'+str(datetime.datetime.now()) + '.txt'
			# if exercises directory is not available then create
			if not os.path.exists(os.path.dirname(new_file_name)):
				os.makedirs(os.path.dirname(new_file_name))
			# Save all the found words in the exercise file
			with open(new_file_name, 'w') as exercise_file:
				csv_writer = csv.writer(exercise_file)
				csv_writer.writerow(exercisewords_list)
		except OSError as ose:
			print('Exercise File could not be created.' + str(ose))

# Start the main game loop
shreya_words_game(get_words_list())
