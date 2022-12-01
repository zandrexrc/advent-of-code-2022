#!/usr/bin/python

"""
Solution for Day 1 of Advent of Code 2022
https://adventofcode.com/2022/day/1
"""

import sys
from functools import reduce

class Calorie:
	"""A representation of a Calorie

	Attributes
	----------
	value: int
		The number of calories

	Methods
	-------
	get_value()
		Returns the Calorie's value as an integer
	"""

	def __init__(self, value):
		"""
		@param value (int): The number of calories
		"""
		self.value = value

	def get_value(self):
		"""Get the number of calories
		@returns int: the Calorie's value as an integer
		"""
		return self.value

class CalorieFactory:
	"""A class for generating a new Calorie object

	Methods
	-------
	create(value)
		Creates a Calorie object with the given value
	"""
	def create(value):
		"""Creates a Calorie object with the given value
		@param value (string): The number of calories
		@returns Calorie: The created Calorie object
		"""
		parsed_value = int(value)
		return Calorie(parsed_value)

class CalorieListFactory:
	"""A class for generating a List of Calorie objects
	
	Methods
	-------
	create(calorie_string_block)
		Transforms a calorie string block into a list of Calorie objects
	"""
	def create(calorie_string_block):
		"""Transforms a calorie string block into a list of Calorie objects
		@param calorie_string_block (string): A series of numbers separated by newlines
		@returns Calorie[]: A list of Calorie objects
		"""
		calorie_strings = StringParsingUtils.split_by_newlines(calorie_string_block)
		calorie_list = [CalorieFactory.create(calorie_string) for calorie_string in calorie_strings]
		return list(calorie_list)

class CaloriesFileReader:
	"""A class for reading and parsing a file containing calorie data

	Methods
	-------
	parse_file_to_calorie_lists(filepath)
		Reads a given file and extracts data into a list of Calorie lists
	"""
	def parse_file_to_calorie_lists(filepath):
		"""Reads a given file and extracts data into a list of Calorie lists
		@param filepath (string): Path to a valid file containing calorie data
		@returns Calorie[][]: A list of Calorie lists
		"""
		with open(filepath) as f:
			file_content = f.read()
			calorie_string_blocks = StringParsingUtils.split_by_empty_lines(file_content)
			calorie_lists = [CalorieListFactory.create(calorie_string_block) for calorie_string_block in calorie_string_blocks]
			return list(calorie_lists)

class Elf:
	"""A representation of an Elf

	Attributes
	----------
	calories: Calorie[]
		A list of Calorie objects belonging to the Elf

	Methods
	-------
	get_sum_calories()
		Returns the sum of Calories that the Elf is carrying
	"""
	def __init__(self, calories):
		"""
		@param calories (Calorie[]): A list of Calorie objects
		"""
		self.calories = calories

	def get_sum_calories(self):
		"""Calculates the sum of Calories that the Elf is carrying
		@returns int: The sum of all calories in the list
		"""
		return CalorieUtils.sum_calories(self.calories)

class ElfGroup:
	"""A representation of a group of Elves
	
	Attributes
	----------
	elves: Elf[]
		A list of Elf objects (plural Elves)

	Methods
	-------
	add_elf(elf)
		Adds an Elf to the group
	sort_elves_by_most_calories()
		Sorts the elves in a decreasing order based on the total amount of calories they are carrying
	get_n_elves_carrying_most_calories(number_of_elves)
		Returns a list of Elves who are carrying the highest total calories among the group
	"""
	def __init__(self):
		self.elves = []

	def add_elf(self, elf):
		"""Adds an Elf object to the group
		@param elf (Elf): An Elf object to be added in the group
		"""
		self.elves.append(elf)

	def sort_elves_by_most_calories(self):
		"""Sorts the elves in a decreasing order based on the total amount of calories they are carrying.
		@returns None: Elves are sorted in place
		"""
		self.elves.sort(key=lambda elf: elf.get_sum_calories(), reverse=True)

	def get_n_elves_carrying_most_calories(self, number_of_elves=1):
		"""Get a given number of elves who are carrying the highest total calories among the group
		@param number_of_elves (int): The number of elves included in the returned list
		@returns Elf[]: A list of Elves carrying the most calories
		"""
		self.sort_elves_by_most_calories()
		return self.elves[:number_of_elves]

class StringParsingUtils:
	"""Various utility functions for processing strings
	
	Methods
	-------
	split_by_empty_lines(string)
		Splits a string into a list of substrings with empty lines as separators
	split_by_newlines(string)
		Splits a string into a list of substrings with newlines as separators
	"""
	def split_by_empty_lines(string):
		"""Splits a string into a list of substrings with empty lines as separators
		@param string (string): The string to be processed
		@returns string[]: A list of strings previously separated by empty lines
		"""
		return string.split("\n\n")

	def split_by_newlines(string):
		"""Splits a string into a list of substrings with newlines as separators
		@param string (string): The string to be processed
		@returns string[]: A list of strings previously separated by newlines
		"""
		return string.split("\n")

class CalorieUtils:
	"""Various utility functions for processing Calorie objects

	Methods
	-------
	sum_calories(calorie_list)
		Calculates the sum of values in a given list of Calorie objects
	"""
	def sum_calories(calorie_list):
		"""Calculates the sum of values in a given list of Calorie objects
		@param calorie_list (Calorie[]): A list of Calorie objects
		@returns int: The sum of all Calorie values in the given list
		"""
		return reduce((lambda calorie1, calorie2: calorie1 + calorie2), [calorie.get_value() for calorie in calorie_list])

class Program:
	"""Entrypoint of the solution

	Methods
	-------
	main()
		Runs the main process of the solution
	"""
	def main():
		"""
		Runs the main process of the solution
		"""
		elves = ElfGroup()

		# Parse file
		filepath = len(sys.argv) > 1 and sys.argv[1] or "inputs/day01.txt"
		calorie_lists = CaloriesFileReader.parse_file_to_calorie_lists(filepath)
		for calorie_list in calorie_lists:
			elves.add_elf(Elf(calorie_list))

		elves_carrying_most_calories = elves.get_n_elves_carrying_most_calories(3)

		# Total calories carried by the top elf
		print(elves_carrying_most_calories[0].get_sum_calories())

		# Sum of calories carried by the top three elves
		print(sum([elf.get_sum_calories() for elf in elves_carrying_most_calories]))

if __name__ == "__main__":
	Program.main()
