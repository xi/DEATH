#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
win-functions
* take a Map and number of players and
* return the id of the winnig player or None
"""


def death_match(_map, n):
	"""destroy every foe unit"""
	winner = None
	for player in range(n):
		if _map.count(player) > 0:
			if winner:
				return None
			else:
				winner = player
	return winner


def capturetheflag(_map, n):
	"""capture the four corners"""
	flag1 = _map.getitem(0, 0)
	flag2 = _map.getitem(0, _map.cols - 1)
	flag3 = _map.getitem(_map.rows - 1, _map.cols - 1)
	flag4 = _map.getitem(_map.rows - 1, 0)
	if flag1 == flag2 and flag2 == flag3 and flag3 == flag4:
		return flag1 - 1
	else:
		return None


def economy(_map, n):
	"""be first to capture a given fraction of the map"""
	k = int(_map.rows * _map.cols / n * 0.2)  # TODO?
	for player in range(n):
		if _map.count(player) >= k:
			return player
	return None
