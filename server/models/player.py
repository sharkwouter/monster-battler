#!/usr/bin/env python3
class Player:
	def __init__(self, name):
		self.name = name
		self.current_team = []

	def getName(self):
		return self.name

	def addToTeam(self, monster):
		self.current_team.append(monster)        
		return type(monster)
