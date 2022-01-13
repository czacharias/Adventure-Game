import random
from Items import *
from Weapons import *

class Player:

	"""
	Creates a player with String name and hp value int, exp int , inventory list/dictonary
	Attack stat (for damage), level
	""" 
	#wood_sword = Wood_Sword()

	def __init__(self, name) -> None:
		self.name = name
		self.hp = 100
		self.max_hp = 100
		self.max_melee_defence = 0.25
		self.melee_defence = 0.25
		self.max_magic_defence = 0.25
		self.magic_defence = 0.25
		self.mana = 30
		self.max_mana = 30
		self.xp = 0
		self.level = 1
		self.items = Items()
		self.weapons = [Wood_Sword(), Stone_Sword()]
		self.current_weapon = self.weapons[0]
		self.attack = 10
		self.attacks = {

			#attack name:[damage type, damage, mana cost, threshold for hitting, element]

			'fireball':['magic', 25, 10, 75, 'fire'],
			'light attack':['melee', self.attack, 0, 95, 'null'],
			'heavy attack':['melee', (self.attack*2), 0, 75, 'null']

			}
		self.coins = 100
	

	def move(self, opponent) -> None:
		"""
		Every turn, this function runs, allows the player to choose an action
		"""
		turn_move = ''
		while turn_move not in ['attack', 'use item', 'guard', 'change weapon']:
			turn_move = input('What do you want to do?\n|Attack|  |Use Item|  |Guard| |Change Weapon|\n').lower()
		else:
			if turn_move == 'attack':
				self.attack_(opponent)
				return
			elif turn_move == "use item":
				self.items.item_use(self, opponent)
				return
			elif turn_move == 'guard':
				if self.melee_defence >= 0.9:
					print('Defence is maxed out, try another action\n')
					self.move(opponent)
					return
				else:
					self.melee_defence += 0.1
					self.magic_defence += 1
					print('Your guard increased by one\n')
				return
			else:
				weapons_names = []
				weapons_ = []
				for i in self.weapons:
					weapons_names.append(i.name)
					weapons_.append(i)
				print("Current Weapon: ", self.current_weapon)
				self.print_weapons()
				print(weapons_names)
				weapon_name = ''
				while weapon_name not in weapons_names:
					weapon_name = input('\nWhat weapon do you want to use? ')
				weapon_choice = weapons_[weapons_names.index(weapon_name)]
				self.current_weapon = weapon_choice
				self.move(opponent)
				return

	def print_opponents(self, opponent):
		for enemy in opponent:
			print(enemy, end=' ')

	def print_weapons(self):
		weapon_lst = []
		for name in self.weapons:
			weapon_lst.append(name.name)
		print(weapon_lst)

	def attack_(self, opponent) -> None:
		"""
		Player picks between attacks and damages their opponent
		"""			

		if len(opponent) > 1:
			self.print_opponents(opponent)
			opponent_choice = 9999
			while opponent_choice > (len(opponent)-1):
				opponent_choice = int(input('\nWhat is the number of the opponent you want to attack? '))
		else:
			opponent_choice = 0

		self._print_attacks()

		attack_choice = ""
		while attack_choice not in self.attacks.keys():
			attack_choice = input('What attack do you want to use?\n').lower()
			if attack_choice == 'back':
				self.move(opponent)
		x = random.randint(0, 100)

		if self.mana > self.attacks[attack_choice][2]: # check if they have enough mana
			if x < self.attacks[attack_choice][3]: # check to see if attack hits
				
				if isinstance(self.current_weapon, Ranged_Weapon): # if weapon is ranged
					opponent[opponent_choice].take_damage((self.attacks[attack_choice][1] + self.current_weapon.damage_increase), self.attacks[attack_choice][0], self.attacks[attack_choice][4])
					self.mana -= self.attacks[attack_choice][2]
					self.current_weapon.ammo -= 1
				if self.current_weapon.name == "Stick" and attack_choice != 'fireball':
					returned = self.current_weapon.attacks_()
					if returned:
						opponent[opponent_choice].take_damage((self.attacks[attack_choice][1] + self.current_weapon.damage_increase), self.attacks[attack_choice][0], self.attacks[attack_choice][4])
						self.mana -= self.attacks[attack_choice][2]
						self.move(opponent)
				else:
					opponent[opponent_choice].take_damage((self.attacks[attack_choice][1] + self.current_weapon.damage_increase), self.attacks[attack_choice][0], self.attacks[attack_choice][4])
					self.mana -= self.attacks[attack_choice][2]	
					
			else:
				print('You missed your attack!')
		else:
			print('Not enough mana, pick another attack')

			
	def _print_attacks(self) -> None:
		attacks_available = []
		for x in self.attacks.keys():
			attacks_available.append(x)
		print('\n', attacks_available)



	def heal(self, percentage):
		"""    
		When player uses healing item, this function heals them and gives information about the heal
		"""
	
		healing = self.max_hp * percentage
		self.hp += healing
		if self.hp > self.max_hp:
			self.hp = self.max_hp
		print("You have healed for {} and are now at {}/{}\n".format(healing, self.hp, self.max_hp))
	
	def take_damage(self, damage, damage_type):
		"""
		When the player gets damaged by their opponent, the opponent runs this function in their attack_ function
		"""
		if damage_type == 'melee':
			damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
			damage_taken = (damage -(damage * self.melee_defence) - damage_dropoff)
			if damage_taken <= 0:
				damage_taken = random.uniform(1, 2)
			self.hp -= round(damage_taken, 1)
			print('You were hit for', round(damage_taken, 1), ' damage')
		elif damage_type == 'magic':
			damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
			damage_taken = (damage -(damage * self.magic_defence) - damage_dropoff)
			if damage_taken <= 0:
				damage_taken = random.uniform(1, 2)
			self.hp -= round(damage_taken, 1)
			print('You were hit for', round(damage_taken, 1), ' damage')

    

	def end_fight(self, exp_gained):
		"""
		At the end of the fight, this function changes xp to levels and gives upgrades
		"""
		
		if self.xp >= 100:
			self.level += 1
			self.xp = 0
			bonus_choice = ""
		

		while bonus_choice not in ['health', 'attack damage', 'defence', 'mana']:
			bonus_choice = input('Do you want to upgrade your health, your attack damage, or your defence?').lower
		else:
			if bonus_choice == 'health':
				self.max_hp += self.level * 10
				print('Your hp has increased to ', self.hp)
			elif bonus_choice == 'attack damage':
				self.attack += self.level * 1.5
				print('Your hp has increased to ', self.attack)
			elif bonus_choice == "defence": 
				self.max_melee_defence += self.level
				self.max_magic_defence += self.level
			elif bonus_choice == 'mana':
				self.max_mana += self.level * 5

		self.xp += exp_gained
		self.melee_defence = self.max_melee_defence
		self.magic_defence = self.max_magic_defence
		self.coins += 100