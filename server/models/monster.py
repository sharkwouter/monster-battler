#!/usr/bin/env python3
class Monster:
    def __init__(self, name):
        self.name = name
        self.moves = [None] * 4

    def getName(self):
        return self.name

    def getMoves(self):
        return self.moves

    def addMove(self, move):
        self.moves.remove(self.move.last())
        self.moves.append(move)
