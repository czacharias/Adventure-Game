import random
from Player import *

class Enemy:
	"""
	Parent class for all types of opponents, has basic attack and take damage functions
	Has a name, hp, attack, and defence
	"""
	def __init__(self, name, hp, attack, melee_defence, magic_defence, element):
		self.name = name
		self.hp = hp
		self.max_hp = hp
		self.attack = attack
		self.melee_defence = melee_defence
		self.magic_defence = magic_defence
		self.element = element

	def __str__(self):
		"""
		Returns the class name as a string when called
		"""
		return self.name 

	def attack_(self, player):
		"""
		For when an enemy deals damage to the player
		"""

		luck = random.randint(1, 150)
		if luck < 100:
			player.take_damage(self.attack,'melee')
		elif 100 < luck < 125:
			player.take_damage((self.attack * 1.25), 'melee')

		else:
			print(self, 'missed')

	def turn_(self, player):
		self.attack_(player)

	def take_damage(self, damage, damage_type, element):
		"""
		For when the enemy had damage dealt to them, run in the player attack_ function
		"""

		if self.element == element:
			print('Damage doubled for element alignment!')

			if damage_type == 'melee':
				damage_dropoff = random.uniform(damage * 0.1, damage * 0.5)
				damage_taken = ((damage -(damage * self.melee_defence)- damage_dropoff)*2)
				self.hp -= damage_taken
				print('You hit the ', self.name, ' for ', round(damage_taken, 1), ' damage!')
			elif damage_type == 'magic':
				damage_dropoff = random.uniform(damage * 0.1, damage * 0.5)
				damage_taken = ((damage -(damage * self.magic_defence)- damage_dropoff)*2)
				self.hp -= round(damage_taken, 1)
				print('You hit the ', self.name, ' for ', round(damage_taken, 1), ' damage!')
		else:
			if damage_type == 'melee':
				damage_dropoff = random.uniform(damage * 0.1, damage * 0.5)
				damage_taken = (damage -(damage * self.melee_defence)- damage_dropoff)
				self.hp -= damage_taken
				print('You hit the ', self.name, ' for ', round(damage_taken, 1), ' damage!')
			elif damage_type == 'magic':
				damage_dropoff = random.uniform(damage * 0.1, damage * 0.5)
				damage_taken = (damage -(damage * self.magic_defence)- damage_dropoff)
				self.hp -= damage_taken
				print('You hit the ', self.name, ' for ', round(damage_taken, 1), ' damage!')

	def item_drop(self, Player):
		'''
		End of fight, enemy might drop weapon
		'''
		weapons = [Wood_Sword(), Stone_Sword(), Bow(), Gun()]
		for i in weapons:
			for j in Player.weapons:
				if i == j:
					weapons.remove(i)
					
		weapon_drop_chance = random.randint(1, 2)
		if weapon_drop_chance == 2:
			weapon_drop = weapons[random.randint(0, len(weapons) - 1)]
			Player.weapons.append(weapon_drop)
			print(Player.weapons)
			print('You found a ', weapon_drop)





    




class Zombie(Enemy):
  """
  Subclass of enemy, no new functions
  """
  def __init__(self):
    super().__init__("Zombie", 0, 15 , 0.25, 0, 'earth')


    

class Wizard(Enemy):
	"""
	Subclass of enemy, has healing abilties and different attacks
	"""
	def __init__(self):
		super().__init__('Wizard', 75, 20, 0.05, 0.2, 'water')

	def turn_(self, player):
		turn = random.randint(0, 1)
		if turn == 0:
			self.attack_(player)
		if turn == 1:
			self.heal()

	def attack_(self, player):
		damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
		luck = random.randint(1, 150)

		if luck <= 100:
			atk_dmg = self.attack - (damage_dropoff//100)
			print('The wizard cast a basic damage spell')
			player.take_damage(atk_dmg, 'magic')
		if 100 < luck <= 125:
			atk_dmg = self.attack - (damage_dropoff//100)
			print("The wizard's spell backfired\n")
			self.take_damage(atk_dmg, 'magic', 'water')
		if 125 < luck <= 150:
			print("The wizard's spell worked better than expected, there was no damage dropoff\n")
			player.take_damage(self.attack, 'magic')

	def heal(self):
		hp_increase = random.randint(5, 15)
		print('The wizard healed for ', hp_increase, ' hp!')
		self.hp += hp_increase

class Aspid(Enemy):
  '''
  Subclass of enemy, custom attacks
  '''

  def __init__(self):
    super().__init__('Aspid', 125, 10, 0.1, 0.1, 'air')
  
  def attack_(self, player) -> None:
    damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
    luck = random.randint(1, 100)

    if luck <= 75:
      print('The Aspid charges towards you and hits you dead center')
      player.take_damage(self.attack - (damage_dropoff//100), 'melee')
    if 75 < luck <= 100:
      print('The Aspid shoots acid at you, which does double damage')
      player.take_damage((self.attack - (damage_dropoff//100))*2, 'melee') 


class fly_swarm(Enemy):
	'''
	Subclass of enemy
	'''

	def __init__(self, name):
		self.name = name
		self.hp = 10 
		self.max_hp = 10
		self.attack = 1
		self.melee_defence = 0
		self.magic_defence = 0
		self.element = 'air'
	
	def __str__(self):
		return self.name
	
class You():
	'''
	Subclass of enemy, custom attacks, final boss, has same moveset as player
	'''

	def __init__(self, opponent):
		self.name = 'Dark ' + opponent.name 
		self.hp = 1
		self.max_hp = 100
		self.max_melee_defence = 0.25
		self.melee_defence = 0.25
		self.max_magic_defence = 0.25
		self.magic_defence = 0.25
		self.mana = 30
		self.max_mana = 30
		self.items = {
		
		#item name:[item description, amount]
		
		'apple':["heals 10% hp", 10], 
		'health potion': ['heals 50% hp', 10], 
		'bandages':['heals 25% hp', 10], 
		'mana regen':['gives 10 mana', 10], 
		'stick':['takes away 10% hp', 10], 
		'random potion':['gives a random effect', 15]

		}
		self.attack = 10
		self.attacks = {

		#attack name:[damage type, damage, mana cost, threshold for hitting, element]

		'fireball':['magic', 25, 10, 75, 'fire'],
		'light attack':['melee', self.attack, 0, 95, 'null'],
		'heavy attack':['melee', (self.attack*2), 0, 75, 'null']

		}
		self.coins = 100

	def __str__(self):
		"""
		Returns the class name as a string when called
		"""
		return self.name
	
	def turn_(self, opponent) -> None:
		"""
		Every turn, this function runs, allows the player to choose an action
		"""
		
		if self.hp == self.hp/2 or self.mana <= 10:
			turn_move = 1
		else:
			turn_move = random.randint(0, 2)

		if turn_move == 0:
			self.attack_(opponent)
		elif turn_move == 1:
			self.item_use(opponent)
		elif turn_move == 2 and self.melee_defence <= 0.9:
			print(self.name, 'increased their guard')
			self.melee_defence += 0.1
		else:
			self.turn_

	def attack_(self, opponent) -> None:
		"""
		Player picks between attacks and damages their opponent
		"""


		attack_choice = random.choice(list(self.attacks.keys()))

		x = random.randint(0, 100)

		if self.mana > self.attacks[attack_choice][2]:
			if x < self.attacks[attack_choice][3]:
				opponent.take_damage(self.attacks[attack_choice][1], self.attacks[attack_choice][0])
				self.mana -= self.attacks[attack_choice][2]
			else:
				print('Dark you missed your attack on yourself!')
		else:
			print('You had no mana for an attack')

	def item_use(self, enemy):
		"""
		Possible items and each items effect:
		Bandages: 25%
		Health potion: 50%
		Random potion # Uhh this will be interesting
		Apple: 10%
		Stick: - 10%

		"""


		if self.hp == self.hp/2:
			if self.items['health potion'][1] >= 1:
				item = 'health potion'
			elif self.items['bandages'][1] >= 1:
				item = 'bandages'
			else:
				item = random.choice(list(self.items.keys()))
		elif self.mana <= 10:
			if self.items['mana regen'][1] >= 1:
				item = 'mana regen' 
			else:
				item = random.choice(list(self.items.keys()))
		else:
			item = random.choice(list(self.items.keys()))

		
		if item == 'bandages':
			self.items[item][1] -= 1 
			self.heal(0.25)
		
		elif item == 'health potion':
			self.items[item][1] -= 1 
			self.heal(0.5)
			
		elif item == 'apple':
			self.items[item][1] -= 1 
			self.heal(0.1)

		elif item == 'stick':
			self.items[item][1] -= 1 
			self.heal(-0.1)

		elif item == 'random potion':
			self.items[item][1] -= 1 
			effect = random.randint(0, 100)
			if effect == 0:
				self.take_damage(999)
			elif effect >= 1 and effect <= 50:
				self.heal(0.5)
			elif effect >= 51 and effect <= 98:
				self.heal(0.25)
			elif effect == 99:
				self.hp = self.max_hp
			elif effect == 100:
				enemy.take_damage(999)

		elif item == 'mana regen':
			self.items[item][1] -= 1 
			self.mana += 10


	def take_damage(self, damage, damage_type, element):
		"""
		When the player gets damaged by their opponent, the opponent runs this function in their attack_ function
		"""
		if damage_type == 'melee':
			damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
			damage_taken = (damage -(damage * self.melee_defence)- damage_dropoff)
			self.hp -= round(damage_taken, 1)
			print(self.name, 'was hit for', round(damage_taken, 1), ' damage')
		elif damage_type == 'magic':
			damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
			damage_taken = (damage -(damage * self.magic_defence)- damage_dropoff)
			self.hp -= round(damage_taken, 1)
			print(self.name, 'was hit for', round(damage_taken, 1), ' damage')

	def heal(self, percentage):
		"""    
		When player uses healing item, this function heals them and gives information about the heal
		"""

		print('heal')

		healing = self.max_hp * percentage
		self.hp += healing
		if self.hp > self.max_hp:
			self.hp = self.max_hp
		print("You healed for {} and are now at {}/{}\n".format(healing, self.hp, self.max_hp))



