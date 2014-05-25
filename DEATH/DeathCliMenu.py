#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
from death_ui import DeathUI
from death import Death
from matrix import Map

help = """
Welcome to DEATH !
DEATH is a variant to Conways game of LIFE.
Every LIFE game can be described by two sets of numbers:
What I added is mulitiplayer support:
* numbers of friendly neighbors for a friendly item to survive
* numbers of friendly neighbors for a friendly item to be born
* numbers of friendly neighbors for a foe item to be killed
the players take turns.

CONTROLS:
arrow-keys - move cursor
space      - toggle field value

backspace  - clear field value
return     - submit


h          - display this help screen
escape     - quit

return with any key
"""


class Crs(object):
	def __init__(self, screen):
		self.screen = screen
		self.screen.clear()
		curses.curs_set(0)
		self.screen.keypad(1)
		curses.start_color()
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
		curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

	def run(self):
		while self.main():
			pass

	def main(self):
		x0 = (self.screen.getmaxyx()[1] - 20) / 2
		y0 = (self.screen.getmaxyx()[0] - 2) / 2
		# n
		self.screen.clear()
		n = 1
		while 1:
			self.screen.addstr(y0, x0, 'number of players: %s' % n,
				curses.color_pair(2))
			key = self.screen.getch()
			if key == curses.KEY_UP:
				n += 1
			elif key == curses.KEY_DOWN:
				if n > 1:
					n -= 1
			elif key == ord('h'):
				self.screen.clear()
				self.screen.addstr(0, 0, help, curses.color_pair(2))
				self.screen.getch()
				self.screen.clear()
			elif key == ord('\n'):
				break
			elif key == 27:
				return False
		# map size
		self.screen.clear()
		rows = 10
		while 1:
			self.screen.addstr(y0, x0, 'number of rows: %s' % rows,
				curses.color_pair(2))
			key = self.screen.getch()
			if key == curses.KEY_UP:
				if rows < self.screen.getmaxyx()[0] - 2:
					rows += 1
			elif key == curses.KEY_DOWN:
				if rows > 1:
					rows -= 1
			elif key == ord('h'):
				self.screen.clear()
				self.screen.addstr(0, 0, help, curses.color_pair(2))
				self.screen.getch()
				self.screen.clear()
			elif key == ord('\n'):
				break
			elif key == 27:
				return False
		cols = 10
		while 1:
			self.screen.addstr(y0, x0, 'number of columns: %s' % cols,
				curses.color_pair(2))
			key = self.screen.getch()
			if key == curses.KEY_UP:
				if cols < self.screen.getmaxyx()[1] / 2 - 1:
					cols += 1
			elif key == curses.KEY_DOWN:
				if cols > 1:
					cols -= 1
			elif key == ord('h'):
				self.screen.clear()
				self.screen.addstr(0, 0, help, curses.color_pair(2))
				self.screen.getch()
				self.screen.clear()
			elif key == ord('\n'):
				break
			elif key == 27:
				return False
		# alive born kill
		"""
			Diplay manu for every user
			and append the results to the three lists afterwards
		"""
		alive = []
		born = []
		kill = []
		for player in range(n):
			abk = [[], [], []]
			_abk = 0
			_i = 0
			while 1:
				self.screen.clear()
				self.screen.addstr(y0 - 1, x0 - 10, 'Player %s' % str(player + 1),
					curses.color_pair(2))
				self.screen.addstr(y0, x0 - 10, 'alive', curses.color_pair(2))
				self.screen.addstr(y0 + 1, x0 - 10, 'born', curses.color_pair(2))
				self.screen.addstr(y0 + 2, x0 - 10, 'kill', curses.color_pair(2))
				for i in range(9):
					self.screen.addstr(y0 - 1, x0 + 2*i, str(i), curses.color_pair(2))
					for __abk in range(3):
						if _abk == __abk and _i == i:
							color = curses.color_pair(1)
						else:
							color = curses.color_pair(2)
						if i in abk[__abk]:
							self.screen.addstr(y0 + __abk, x0 + 2*i, 'X', color)
						else:
							self.screen.addstr(y0 + __abk, x0 + 2*i, ' ', color)

				key = self.screen.getch()
				if key == curses.KEY_UP:
					if _abk > 0:
						_abk -= 1
				elif key == curses.KEY_DOWN:
					if _abk < 2:
						_abk += 1
				if key == curses.KEY_LEFT:
					if _i > 0:
						_i -= 1
				elif key == curses.KEY_RIGHT:
					if _i < 10 - 1:
						_i += 1
				elif key == ord(' '):
					if _i in abk[_abk]:
						abk[_abk] = filter(lambda x: x != _i, abk[_abk])
					else:
						abk[_abk].append(_i)
				elif key == curses.KEY_BACKSPACE:
					abk[_abk] = filter(lambda x: x != _i, abk[_abk])
				elif key == ord('h'):
					self.screen.clear()
					self.screen.addstr(0, 0, help, curses.color_pair(2))
					self.screen.getch()
					self.screen.clear()
				elif key == ord('\n'):
					break
				elif key == 27:
					return False
			alive.append(abk[0])
			born.append(abk[1])
			kill.append(abk[2])

		_map = Map(rows, cols)
		d = Death(_map, n, alive, born, kill)
		DeathUI(self.screen, d, title='default')
		return True


if __name__ == '__main__':
	screen = curses.initscr()
	crs = Crs(screen)
	try:
		crs.run()
	except Exception as ex:
		print(ex)
	curses.endwin()
