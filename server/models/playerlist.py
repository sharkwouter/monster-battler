#!/usr/bin/env python3
class PlayerList:
	def __init__(self):
		self.list = []

	def addPlayer(self, player):
		self.list.append(player)

	def findPlayer(self, name):
		found = None
		for player in self.list:
			if player.getName == name:
				found = player
				break
		return found
