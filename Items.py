from Player import *
import random

class Items:
	def __init__(self):
		self.items = {
			
			#item name:[item description, amount]
			
			'apple':["heals 10% hp", 0], 
			'health potion': ['heals 50% hp', 1], 
			'bandages':['heals 25% hp', 0], 
			'mana regen':['gives 10 mana', 0], 
			'stick':['takes away 10% hp', 0], 
			'random potion':['gives a random effect', 5]

			}
			

	def item_use(self, player, enemy):
		"""
		Possible items and each items effect:
		Bandages: 25%
		Health potion: 50%
		Random potion # Uhh this will be interesting
		Apple: 10%
		Stick: - 10%

		"""
		item = ""
		while item not in self.items:
			self._print_items()
			item = input('What item do you want to use? ').lower()
			if item == 'back':
				return player.move(enemy)

		item_confirm = ""


		while item_confirm != 'yes' and item_confirm != 'no':
			item_confirm = input(self.items[item][0] + "\nAre you sure you want to use this item? ").lower()
			if item_confirm == 'yes':
			
				if item == 'bandages':
					self.items[item][1] -= 1 
					player.heal(0.25)
				
				elif item == 'health potion':
					self.items[item][1] -= 1 
					player.heal(0.5)
				
				elif item == 'apple':
					self.items[item][1] -= 1 
					player.heal(0.1)

				elif item == 'stick':
					self.items[item][1] -= 1 
					player.heal(-0.1)

				elif item == 'random potion':
					self.items[item][1] -= 1 
					effect = random.randint(0, 100)
					if effect == 0:
						player.take_damage(999)
					elif effect >= 1 and effect <= 50:
						player.heal(0.5)
					elif effect >= 51 and effect <= 98:
						player.heal(0.25)
					elif effect == 99:
						player.hp = player.max_hp
					elif effect == 100:
						enemy.take_damage(999)

				elif item == 'mana regen':
					self.items[item][1] -= 1

			elif item_confirm == 'no':
				self.item_use(enemy)

	def _print_items(self) -> None:
		items_available = []
		for x in self.items:
			if self.items[x][1] >= 1:
				items_available.append(x)
		print(items_available)
	