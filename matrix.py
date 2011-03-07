#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Matrix:
  def __init__(self, rows, cols, value=0):
    self.rows = rows
    self.cols = cols
    self.value = value
    self.data=[]
    for i in range(rows):
      self.data.append([])
      for j in range(cols):
        self.data[i].append(value)

  def setitem(self, row, col, value):
    self.data[row][col] = value

  def getitem(self, row, col):
    if row<0 or col<0:
      raise IndexError
    return self.data[row][col]

  def draw(self):
    for row in self.data:
      print row        

  def apply_f(self, f):
    for i in range(self.rows):
      for j in range(self.cols):
        self.setitem(i, j, f(self.getitem(i,j)))
    
  def join(self, mats):
    for mat in mats:
      if mat.rows != self.rows or mat.cols != self.cols:
        raise Exception
    for i in range(self.rows):
      for j in range(self.cols):
        self.setitem(i, j, [mat.getitem(i,j) for mat in mats])

  def count(self, _item):
    c = 0
    for row in rows:
      for item in row:
        if item == _item:
          c += 1
    return c

  def save(filename, seperator=';'):
    pass # TODO

  def load(filename, seperator=';'):
    pass # TODO

class Map(Matrix):
  def __init__(self, rows=5, cols=5, diagonal=True, value=0):
    Matrix.__init__(self,rows, cols, value)
    self.diagonal = diagonal

  def neighbors(self, id, reverse=False):
    try: 0 in id
    except: id = [id]
    if reverse: id.append(self.value)
    result = Map(self.rows, self.cols, self.diagonal)
    for i in range(self.rows):
      for j in range(self.cols):
        a = 0
        for cood in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
          try:
            if reverse:
              if self.getitem(cood[0], cood[1]) not in id: a += 1
            else:
              if self.getitem(cood[0], cood[1]) in id: a += 1
          except: pass
        if self.diagonal:
          for cood in [(i+1,j+1), (i+1,j-1), (i-1,j+1), (i-1,j-1)]:
            try:
              if reverse:
                if self.getitem(cood[0], cood[1]) not in id: a += 1
              else:
                if self.getitem(cood[0], cood[1]) in id: a += 1
            except: pass
        result.setitem(i,j,a)
    return result

  def clone(self):
    result = Map(self.rows, self.cols, self.diagonal, self.value)
    for i in range(self.rows):
      for j in range(self.cols):
        result.setitem(i, j, self.getitem(i,j))
    return result

