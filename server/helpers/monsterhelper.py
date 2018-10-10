import json

def createMonster(number):
	with open('server/data/monsters.json','r') as f:
		data = json.load(f)
	if data:
		return data["monsters"][str(number)] 
	else:
		return None

def listMonsters():
	with open('server/data/monsters.json','r') as f:
		data = json.load(f)
	if data:
		return data["monsters"]
	else:
		return None
