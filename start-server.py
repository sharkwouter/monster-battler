#!/usr/bin/env python3
from flask import request
from flask_api import FlaskAPI, status, exceptions

#import models
from server.models import Player, Monster

#import helper
from server.helpers import listMonsters, createMonster

#Lists and other variables
players = []

def findPlayer(name):
	for player in players:
		if player.getName() == name:
			return player
	return None

app = FlaskAPI(__name__)

@app.route('/monsters/', methods=['GET'])
def monsters():
	return listMonsters()

@app.route('/register/', methods=['GET',"POST"])
def register():
	name = str(request.data.get('name', '')) 
	if name == '':
		return "missing name",status.HTTP_400_BAD_REQUEST
	
	players.append(Player(name))
	return "success"

app.run()
