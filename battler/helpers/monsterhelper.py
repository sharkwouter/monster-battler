import json

def createMonster(number):
	with open('battler/data/monsters.json','r') as f:
		data = json.load(f)
	if data:
		return data["monsters"][str(number)] 
	else:
		return None

def listMonsters():
	with open('battler/data/monsters.json','r') as f:
		data = json.load(f)
	if data:
		return data["monsters"]
	else:
		return None
