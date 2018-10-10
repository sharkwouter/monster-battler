#!/usr/bin/env python3
from flask import request
from flask_api import FlaskAPI, status, exceptions

#import models
from server.models import Player, Monster, PlayerList

#import helper
from server.helpers import listMonsters, createMonster

#Lists and other variables
players = PlayerList()

app = FlaskAPI(__name__)

@app.route('/monsters/', methods=['GET'])
def monsters():
	return listMonsters()

@app.route('/register/', methods=['GET',"POST"])
def register():
	name = str(request.data.get('name', '')) 
	if name == '':
		return "missing name",status.HTTP_400_BAD_REQUEST
	
	players.addPlayer(Player(name))
	return "success"

app.run()
