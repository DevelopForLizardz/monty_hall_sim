#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulate the Monty Hall problem to prove that it's always best to switch.

-- BEGIN LICENSE --

MIT License

Copyright (c) 2016 Ryan Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-- END LICENSE --
"""

import sys
import random
import argparse


def simulate_problem(switch):
	"""
	Plays the game and returns True if a prize was won.
	:param switch: If True, the opportunity to switch doors
				   will be taken.
	"""
	
	# doors are numbered 0 through 2
	prize_door = random.randint(0, 2)
	players_door = random.randint(0, 2)
	# will contain at least one goat
	leftover_doors = range(3)
	leftover_doors.remove(prize_door)
	try:
		leftover_doors.remove(players_door)
	except ValueError:
		pass  # means that players_door and prize_door are the same

	if switch:  # don't need to do this bit if not switching
		# choose a random leftover door to open
		opened_door = random.choice(leftover_doors)
		leftover_doors.remove(opened_door)
		switch_door = prize_door if len(leftover_doors) == 0 else leftover_doors[0]
		players_door = switch_door

	return players_door == prize_door


def simulate_games(num_games, switch):
	"""
	Runs the simulate_problem function num_games times, returning
	total win and loss.
	:param num_games: Number of times to play the game
	:param switch: If True, the opportunity to switch doors will be taken
	:return: (total won, total lost)
	"""
	
	won = 0
	lost = 0

	for x in range(num_games):
		if simulate_problem(switch) is True:
			won += 1
		else:
			lost += 1

	return won, lost


def main():
	parser = argparse.ArgumentParser(description='Monty Hall problem simulater.')
	parser.add_argument('num_games', type=int, help='Number of times to simulate the game')
	parser.add_argument('-s', '--switch', action='store_true', help="If passed, then while " \
						"playing the game the 'switch doors' opportunity will always be taken.")
	args = parser.parse_args()
	if args.num_games < 0:
		raise ValueError("Number of games to simulate must be greater than zero")

	results = simulate_games(args.num_games, args.switch)
	print "Total tests ran: {}\nTest type: {}\nNumber of prizes won: {}\nNumber of goats: {}".format(
		args.num_games, "Switch doors" if args.switch else "Keep choice", results[0], results[1])


if __name__ == '__main__':
	main()
