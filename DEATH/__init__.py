from . import rules

try:
	from ncurses import curses
except ImportError:
	import curses


class Screen:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.keypad(1)
		curses.curs_set(0)
		curses.noecho()

	def __enter__(self):
		return self.screen

	def __exit__(self, *args):
		curses.endwin()


class Grid:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = []
		for y in range(rows):
			self.data.append([])
			for x in range(cols):
				self.data[y].append(None)

	def set(self, y, x, value):
		self.data[y][x] = value

	def get(self, y, x):
		if y < 0 or x < 0:
			raise IndexError
		return self.data[y][x]

	def apply(self, f):
		result = Grid(self.rows, self.cols)
		for y in range(self.rows):
			for x in range(self.cols):
				result.set(y, x, f(self, y, x))
		self.data = result.data

	def count(self, value):
		count = 0
		for row in self.data:
			for cell in row:
				if cell == value:
					count += 1
		return count

	def count_neighbors(self, y, x, value, diagonal=True):
		coods = [
			(y + 1, x),
			(y, x + 1),
			(y - 1, x),
			(y, x - 1),
		]
		if diagonal:
			coods += [
				(y + 1, x + 1),
				(y + 1, x - 1),
				(y - 1, x + 1),
				(y - 1, x - 1),
			]

		count = 0
		for yy, xx in coods:
			if yy in range(self.rows) and xx in range(self.cols):
				if self.get(yy, xx) == value:
					count += 1
		return count


class Game:
	def __init__(self, rows, cols, players, rules, screen):
		self.grid = Grid(rows, cols)
		self.players = players
		self.player = 0
		self.rules = rules
		self.screen = screen
		self.cursor_y = 0
		self.cursor_x = 0

	def draw(self):
		for y in range(self.grid.rows):
			for x in range(self.grid.cols):
				value = self.grid.get(y, x)
				if value is None:
					ch = ' '
				else:
					ch = str(value)
				attr = curses.A_NORMAL
				if y == self.cursor_y and x == self.cursor_x:
					attr |= curses.A_REVERSE
				if value == self.player:
					attr |= curses.A_BOLD
				self.screen.addch(y, x, ch, attr)

	def step(self):
		def f(grid, y, x):
			neighbors = grid.count_neighbors(
				y, x, self.player, diagonal=self.rules.diagonal)
			value = grid.get(y, x)

			if value is None:
				if neighbors in self.rules.born:
					return self.player
			elif value == self.player:
				if neighbors not in self.rules.alive:
					return None
			else:
				if neighbors in self.rules.kill:
					return None
			return value

		self.grid.apply(f)

	def next_player(self):
		self.player = (self.player + 1) % self.players

	def run(self):
		self.draw()
		while True:
			key = self.screen.getch()
			if key == curses.KEY_DOWN:
				if self.cursor_y + 1 < self.grid.rows:
					self.cursor_y += 1
			elif key == curses.KEY_UP:
				if self.cursor_y > 0:
					self.cursor_y -= 1
			elif key == curses.KEY_RIGHT:
				if self.cursor_x + 1 < self.grid.cols:
					self.cursor_x += 1
			elif key == curses.KEY_LEFT:
				if self.cursor_x > 0:
					self.cursor_x -= 1
			elif key == ord(' '):
				value = self.grid.get(self.cursor_y, self.cursor_x)
				if value is None:
					self.grid.set(self.cursor_y, self.cursor_x, self.player)
				elif value == self.player:
					self.grid.set(self.cursor_y, self.cursor_x, None)
				self.next_player()
			elif key == ord('\n'):
				self.step()
				self.next_player()
			elif key == ord('q'):
				return
			self.draw()


def main():
	with Screen() as screen:
		game = Game(20, 20, 2, rules.Conway, screen)
		game.run()
