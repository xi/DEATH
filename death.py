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

class Death:
  def __init__(self, _map=Map(), n=1, alive=[[2,3]], born=[[3]], kill=[[]], win=lambda _map,n: None):
  # the defaults make death the standart life 
    self.n = n
    self.alive = alive
    self.born = born
    self.kill = kill
    self.map = _map
    self.id = 0
    self._win = win

  def step_one(self,id):
    def f(x): 
      if x[0] == 0:
        if x[1] in self.born[id]:
          return id+1
        else:
          return x[0]
      elif x[0] == id+1: 
        if x[1] in self.alive[id]:
          return x[0]
        else:
          return 0
      else:
        if x[1] in self.kill[id]:
          return 0
        else:
          return x[0]
    self.map.join([self.map, self.map.neighbors([id+1])])
    self.map.apply_f(f)

  def step(self):
    for id in range(self.n):
      self.step_one(id)

  def next(self):
    self.id += 1
    if self.id == self.n:
      self.id = 0

  def count(self):
    c = []
    for id in range(self.n):
      c.append(self.map.count(id+1))
    return c

  def win(self):
    return self._win(self.map, self.n)
