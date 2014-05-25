#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import death_extra

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
             after that it is the next players' turn
backspace  - clear field value
return     - perform a full step (one for every player)
tab        - perform a single step (only for the active player)
             after that it is the next players' turn
h          - display this help screen
escape     - return to menu

return with any key
"""


class DeathCli:
	global help

	def __init__(self, death=death_extra.test(15, 15, 2), title='',
			screen=curses.initscr()):
		self.screen = screen
		self.death = death
		self.title = title
		self.screen.clear()
		curses.curs_set(0)
		self.screen.keypad(1)
		curses.start_color()
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
		curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
		self.row = 0
		self.col = 0
		self.draw()
		while self.mainloop():
			winner = self.death.win()
			if winner:
				print('Player %s wins!' % (winner + 1))
				self.screen.getch()
				break

	def draw(self):
		w = 2 * self.death.map.cols - 1
		h = self.death.map.rows
		x0 = (self.screen.getmaxyx()[1] - w) / 2
		y0 = (self.screen.getmaxyx()[0] - h) / 2
		# margin
		for x in range(w):
			self.screen.addstr(y0 - 1, x0 + x, '-', curses.color_pair(2))
			self.screen.addstr(y0 + h, x0 + x, '-', curses.color_pair(2))
		for y in range(h):
			self.screen.addstr(y0 + y, x0 - 1, '|', curses.color_pair(2))
			self.screen.addstr(y0 + y, x0 + w, '|', curses.color_pair(2))
		self.screen.addstr(y0 + h, x0 + w, str(self.death.id + 1),
			curses.color_pair(2))
		# count
		self.screen.addstr(y0 - 1, x0 + 2,
			'|'.join([str(a) for a in self.death.count()]),
			curses.color_pair(2))
		# title
		self.screen.addstr(y0 - 1, x0 + w - len(self.title), self.title,
			curses.color_pair(2))
		# map
		for i in range(self.death.map.rows):
			for j in range(self.death.map.cols):
				field = self.death.map.getitem(i, j)
				if field < 0:
					s = ' '
				else:
					s = str(field + 1)
				if i == self.row and j == self.col:
					self.screen.addstr(y0 + i, x0 + 2*j, s, curses.color_pair(1))
				else:
					self.screen.addstr(y0 + i, x0 + 2*j, s, curses.color_pair(2))

	def mainloop(self):
		key = self.screen.getch()
		if key == curses.KEY_DOWN:
			if self.row < self.death.map.rows - 1:
				self.row += 1
		elif key == curses.KEY_UP:
			if self.row > 0:
				self.row -= 1
		elif key == curses.KEY_RIGHT:
			if self.col < self.death.map.cols - 1:
				self.col += 1
		elif key == curses.KEY_LEFT:
			if self.col > 0:
				self.col -= 1
		elif key == ord(' '):
			self.death.map.setitem(self.row, self.col, self.death.id)
			self.death.next()
		elif key == curses.KEY_BACKSPACE:
			self.death.map.clear(self.row, self.col)
		elif key == ord('\n'):
			self.death.step()
		elif key == ord('\t'):
			self.death.step_one(self.death.id)
			self.death.next()
		elif key == ord('h'):
			self.screen.clear()
			self.screen.addstr(0, 0, help, curses.color_pair(2))
			self.screen.getch()
			self.screen.clear()
			self.draw()
		elif key == 27:
			self.screen.clear()
			return False
		self.draw()
		return True


if __name__ == '__main__':
	try:
		DeathCli()
	except Exception as ex:
		print(ex)
	curses.endwin()
