class Rules:
	diagonal = True
	alive = []
	born = []
	kill = []

	def winner(self, grid):
		raise NotImplementedError


class UserDefinedRules(Rules):
	def __init__(self, alive, born, kill):
		self.alive = alive
		self.born = born
		self.kill = kill


class Conway(Rules):
	alive = [2, 3]
	born = [3]

	def winner(self, grid):
		return None


class DeathMatch(UserDefinedRules):
	def winner(self, grid):
		values = []
		for y in range(grid.rows):
			for x in range(grid.cols):
				value = grid.get(y, x)
				if value is None:
					pass
				elif len(values) == 0:
					values.append(value)
				else:
					return None
		return values[0]


class CaptureTheFlag(UserDefinedRules):
	def winner(self, grid):
		flag1 = grid.get(0, 0)
		flag2 = grid.get(0, grid.cols - 1)
		flag3 = grid.get(grid.rows - 1, 0)
		flag4 = grid.get(grid.rows - 1, grid.cols - 1)

		if flag1 == flag2 and flag2 == flag3 and flag3 == flag4:
			return flag1


class Economy(UserDefinedRules):
	fraction = 0.2

	def winner(self, grid):
		counts = {}
		for y in range(grid.rows):
			for x in range(grid.cols):
				value = grid.get(y, x)
				if value not in counts:
					counts[value] = 0
				counts[value] += 1

		best = max(counts, key=lambda key: counts[key])
		required = int(grid.rows * grid.cols * self.fraction)
		if best > required:
			return best
