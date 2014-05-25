#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
mulitplayer life

in life you define the rules by giving two lists if ints
alive [2,3] - numbers of neighbors for an item to survive
born   [3]  - numbers of neighbors for an item to be born

in multiplayer this gets more complicated.
here's what i thought of:
alive - number of friendly neighbors for a frinedly item to survive
born  - number of friendly neighbors for a friendly item to be born
kill  - number of friendly neighbors for a foe item to be killed
this happens in turns
"""

from matrix import Map


class Death(object):
	def __init__(self, _map=Map(), n=1, alive=[[2, 3]], born=[[3]], kill=[[]],
			win=lambda _map, n: None):
		# the defaults make death the standart life
		self.n = n
		self.alive = alive
		self.born = born
		self.kill = kill
		self.map = _map
		self.player = 0
		self._win = win

	def step_one(self, player):
		# main logic of the game
		def f(x):
			if x[0] < 0:
				if x[1] in self.born[player]:
					return player
				else:
					return x[0]
			elif x[0] == player:
				if x[1] in self.alive[player]:
					return x[0]
				else:
					return -1
			else:
				if x[1] in self.kill[player]:
					return -1
				else:
					return x[0]
		self.map.join([self.map, self.map.neighbors([player])])
		self.map.apply_f(f)

	def step(self):
		for player in range(self.n):
			self.step_one(player)

	def next(self):
		self.player = (self.player + 1) % self.n

	def count(self):
		c = []
		for player in range(self.n):
			c.append(self.map.count(player))
		return c

	def win(self):
		return self._win(self.map, self.n)
