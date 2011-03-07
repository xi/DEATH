#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import death_cli
from death import Death
from matrix import Map

"""
title
number of players
map size
advanced - diagonal, numbers
win
start
"""

class Crs:
  def __init__(self, screen=curses.initscr()):
    self.screen = screen
    self.screen.clear()
    curses.curs_set(0)
    self.screen.keypad(1)
    curses.start_color()
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_BLACK)
    while self.main(): pass

  def main(self):
    x0 = (self.screen.getmaxyx()[1]-20)/2
    y0 = (self.screen.getmaxyx()[0]-2)/2
    # n
    self.screen.clear()
    n = 1
    while 1:
      self.screen.addstr(y0, x0, 'number of players: %s' % n, curses.color_pair(2))
      key = self.screen.getch()
      if key == curses.KEY_UP:
        n += 1
      elif key == curses.KEY_DOWN:
        if n > 1:
          n -= 1
      elif key == ord('\n'):
        break
      elif key == 27:
        return False
    # map size
    self.screen.clear()
    rows = 5
    while 1:
      self.screen.addstr(y0, x0, 'number of rows: %s' % rows, curses.color_pair(2))
      key = self.screen.getch()
      if key == curses.KEY_UP:
        rows += 1
      elif key == curses.KEY_DOWN:
        if rows > 1:
          rows -= 1
      elif key == ord('\n'):
        break
      elif key == 27:
        return False
    cols = 5
    while 1:
      self.screen.addstr(y0, x0, 'number of clumns: %s' % cols, curses.color_pair(2))
      key = self.screen.getch()
      if key == curses.KEY_UP:
        cols += 1
      elif key == curses.KEY_DOWN:
        if cols > 1:
          cols -= 1
      elif key == ord('\n'):
        break
      elif key == 27:
        return False
    # alive born kill
    self.screen.clear()
    alive = []
    born = []
    kill = []
    for id in range(n):
      alive.append([1,3,5,7])
      born.append([1,3,5,7])
      kill.append([])
#      alive.append([2,3])
#      born.append([3])
#      kill.append([2,3,4])
    
    _map = Map(rows, cols)
    d = Death(_map, n, alive, born, kill)
    death_cli.Crs(d, self.screen)
    return True

if __name__ == '__main__':
  try: Crs()
  except: pass
  curses.endwin()

