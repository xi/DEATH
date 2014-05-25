#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matrix import Map
from death import Death
import win
import abk

"complete games"


def test(rows=15, cols=15, n=2):
	map = Map(rows, cols)
	alive = []
	born = []
	kill = []
	for id in range(n):
		alive.append(abk.conway[0])
		born.append(abk.conway[1])
		kill.append(abk.conway[2])
	death = Death(map, n, alive, born, kill, win.economy)
	return death
