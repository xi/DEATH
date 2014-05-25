#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Matrix:
	def __init__(self, rows, cols, value=-1):
		self.rows = rows
		self.cols = cols
		self.value = value
		self.data = []
		for i in range(rows):
			self.data.append([])
			for j in range(cols):
				self.data[i].append(value)

	def setitem(self, row, col, value):
		self.data[row][col] = value

	def getitem(self, row, col):
		if row < 0 or col < 0:
			raise IndexError
		return self.data[row][col]

	def draw(self):
		for row in self.data:
			print(row)

	def apply_f(self, f):
		for i in range(self.rows):
			for j in range(self.cols):
				self.setitem(i, j, f(self.getitem(i, j)))

	def join(self, mats):
		for mat in mats:
			if mat.rows != self.rows or mat.cols != self.cols:
				raise Exception
		for i in range(self.rows):
			for j in range(self.cols):
				self.setitem(i, j, [mat.getitem(i, j) for mat in mats])

	def count(self, _item):
		c = 0
		for row in self.data:
			for item in row:
				if item == _item:
					c += 1
		return c

	def save(filename, seperator=';'):
		f = open(filename, 'w')
		f.write('bla')
		pass  # TODO
		f.close()

	def load(filename, seperator=';'):
		f = open(filename, 'r')
		pass  # TODO
		f.close()


class Map(Matrix):
	def __init__(self, rows=15, cols=15, diagonal=True, value=-1):
		Matrix.__init__(self, rows, cols, value)
		self.diagonal = diagonal

	def clear(self, i, j):
		self.setitem(i, j, -1)

	def field_neighbors(self, i, j, players):
		coods = [
			(i + 1, j),
			(i, j + 1),
			(i - 1, j),
			(i, j - 1),
		]
		if self.diagonal:
			coods += [
				(i + 1, j + 1),
				(i + 1, j - 1),
				(i - 1, j + 1),
				(i - 1, j - 1),
			]

		a = 0
		for _row, _col in coods:
			if _row in range(self.rows) and _col in range(self.cols):
				if self.getitem(_row, _col) in players:
					a += 1
		return a

	def neighbors(self, players):
		result = Matrix(self.rows, self.cols)
		for i in range(self.rows):
			for j in range(self.cols):
				result.setitem(i, j, self.field_neighbors(i, j,  players))
		return result

	def clone(self):
		result = Map(self.rows, self.cols, self.diagonal, self.value)
		for i in range(self.rows):
			for j in range(self.cols):
				result.setitem(i, j, self.getitem(i, j))
		return result
