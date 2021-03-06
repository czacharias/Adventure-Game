from Player import *



class Melee_Weapon:
	def __init__(self):
		self.name = ""
		
	def __eq__(self, other):
		if not isinstance(other, Melee_Weapon):
			return False
		return self.name == other.name

    
	def __str__(self):
		return self.name


class Wood_Sword(Melee_Weapon):
	def __init__(self):
		self.name = 'Wood Sword'
		self.damage_increase = 5

	def __str__(self):
		return self.name

class Stone_Sword(Melee_Weapon):
	def __init__(self):
		self.name = 'Stone Sword'
		self.damage_increase = 10

	def __str__(self):
		return self.name

class Stick:
	def __init__(self):
		self.name = 'Stick'
		self.damage_increase = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

	def attacks_(self):
		print('Are you sure you want to use the stick on the enemy')
		answer = ''
		while answer != 'yes' and answer != 'no':
			answer = input('> ').lower()
		if answer == 'yes':
			return True
		if answer == 'no':
			return False
	

class Ranged_Weapon:
	def __init__(self):
		self.name = ''
	
	def __eq__(self, other):
		if not isinstance(other, Ranged_Weapon):
			return False
		return self.name == other.name


class Bow(Ranged_Weapon):
	def __init__(self):
		self.name = 'Bow'
		self.damage_increase = 3
		self.ammo = 12
	
	def __str__(self):
		return self.name

class Gun(Ranged_Weapon):
	def __init__(self):
		self.name = 'Gun'
		self.damage_increase = 12
		self.ammo = 30

	def __str__(self):
		return self.name 