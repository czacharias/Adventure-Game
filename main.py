import random
import ast
from Player import *
from Weapons import *
from Enemy import *
from Shop import *
from Tavern import *

name = input('What is your name? ')

class Main:

	def __init__(self):
		self.player = Player(name)
		self.tavern = Tavern()
		self.shop = Shop()
		self.opponents = ["Zombie", "Wizard"]

	def save_check(self, file):
		with open(file, mode = 'r') as f:
			a = f.read()
			if a != '':
				print("That file already has a save, are you sure you want to overwrite it?")
				b = input('> ').lower()
				if b == "yes":
					return True
				else:
					return False
			return True


	def save_write(self, player, room):
		weapons = []
		for i in player.weapons:
			weapons.append(i.name)
		files = ['1', 'save 1', '2', 'save 2', '3', 'save 3']
		file = ''
		while file not in files:
			file = input("|Choose a save|\nSave 1\nSave 2\nSave 3\n> ").lower()
		if file == "1" or file == "save 1":
			a = self.save_check("save_1")
			if a == True:
				with open('save_1', mode = 'w') as f:
					f.write(player.name) 
					f.write('\n')
					f.write(str(player.hp))
					f.write('\n')
					f.write(str(weapons))
					f.write('\n')
					f.write(str(player.xp))
					f.write('\n')
					f.write(str(player.level))
					f.write('\n')
					f.write(str(player.coins))
					f.write('\n')
					f.write(str(room))
					print("File saved")
			else:
				self.save_write(player, room)
				return
		elif file == "2" or file == "save 2":
			a = self.save_check("save_2")
			if a == True:
				with open('save_2', mode = 'w') as f:
					f.write(player.name) 
					f.write('\n')
					f.write(str(player.hp))
					f.write('\n')
					f.write(str(weapons))
					f.write('\n')
					f.write(str(player.xp))
					f.write('\n')
					f.write(str(player.level))
					f.write('\n')
					f.write(str(player.coins))
					f.write('\n')
					f.write(str(room))
					print("File saved")
			else:
				self.save_write(player, room)
				return
		elif file == "3" or file == "save 3":
			a = self.save_check("save_3")
			if a == True:
				with open('save_3', mode = 'w') as f:
					f.write(player.name) 
					f.write('\n')
					f.write(str(player.hp))
					f.write('\n')
					f.write(str(weapons))
					f.write('\n')
					f.write(str(player.xp))
					f.write('\n')
					f.write(str(player.level))
					f.write('\n')
					f.write(str(player.coins))
					f.write('\n')
					f.write(str(room))
					print("File saved")
			else:
				self.save_write(player, room)
				return
	
# name , hp, weapons, xp, level, coins, room
	def weapon_stringToObj(self, weapons):
		for n, i in enumerate(weapons):
			if i == 'Wood Sword':
				weapons[n] = Wood_Sword()
			elif i == 'Stone Sword':
				weapons[n] = Stone_Sword()
			elif i == 'Stick':
				weapons[n] = Stick()
			elif i == 'Gun':
				weapons[n] = Gun()
			elif i == 'Bow':
				weapons[n] = Bow()


	def save_read(self, player, room):
		files = ['1', 'save 1', '2', 'save 2', '3', 'save 3']
		file = ''
		while file not in files:
			file = input("|Choose a save|\nSave 1\nSave 2\nSave 3\n> ").lower()
		if file in files[0:2]:
			file = 'save_1'
		elif file in files[2:4]:
			file = 'save_2'
		elif file in files[4:]:
			file = 'save_3'
		with open(file, mode = 'r') as f:
			save_file = f.read()
		save_file = save_file.split("\n")
		print(save_file)
		player.name = save_file[0]
		player.hp = int(save_file[1])
		player.weapons.clear()
		player.weapons = ast.literal_eval(save_file[2])
		player.xp = int(save_file[3])
		player.level = int(save_file[4])
		player.coins = int(save_file[5])
		room = int(save_file[6])
		print(player.weapons)
		self.weapon_stringToObj(player.weapons)
		print(player.weapons)

	



	def fight(self, player, opponents):
		"""
		Decides who's turn it is in a fight, and has them take turns as needed
		"""
		if len(opponents) == 1:
			opponent = opponents[0]
			turn = 0
			while self.player.hp >= 0 and opponent.hp >= 0:
				print("Your Hp | ", self.player.hp, "/", self.player.max_hp, '\nOpponent hp | ', opponent.hp, "/", opponent.max_hp, '\n')
				if turn == 0:
					self.player.move([opponent])
					turn = 1
				elif turn == 1:
					opponent.attack_()
					turn = 0
		else:
			opponentsDead = 0
			while opponentsDead >= 0 and self.player.hp > 0:
				opponentsDead = 0
				for opponent in opponents:
					if opponent.hp > 0:
						opponentsDead += 1
					else:
						opponents.remove(opponent)
				if opponentsDead == 0:
					opponentsDead -= 1
				elif opponentsDead > 0:
					for opponent in opponents:
						if opponent.hp > 0:
							opponent.attack_()
						else:
							pass
					self.player.move(opponents)
					print("Your Hp | ", self.player.hp, "/", self.player.max_hp)
					for opponent in opponents:
						print(opponent.name, 'hp | ', opponent.hp, '/', opponent.max_hp)
			



	def opponent_creator(self, opponent):
		if opponent == 'Zombie':
			return Zombie(self.player)
		if opponent == 'Wizard':
			return Wizard(self.player)


	def run_game(self):
		print(r"""___________.__                               .__                                                               
\__    ___/|  |__   ___________   ____       |__| ______       ____   ____         ____ _____    _____   ____  
  |    |   |  |  \_/ __ \_  __ \_/ __ \      |  |/  ___/      /    \ /  _ \       /    \\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/|  | \/\  ___/      |  |\___ \      |   |  (  <_> )     |   |  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  >__|    \___  >     |__/____  >     |___|  /\____/      |___|  (____  /__|_|  /\___  >
                \/     \/            \/              \/           \/                  \/     \/      \/     \/ """)







		room = 0
		self.save_write(self.player, room)
		self.save_read(self.player, room)
		self.tavern.gamble(self.player)
	

		print('You stumble into a cave')

		while self.player.hp > 0:
			if room == 0:
				print('How did you get here?')
				self.player.hp == 0  

			if room == 1:
				#dialog
				print("\nYou see two doors, one on the left, made of wood; and one on the right, made of stone. You can see a faint light coming from the wooden door, but you have a bad feeling about it. The stone door seems to have jammed shut, but with a little strength, you should be able to pull it open.")
				r1c = ''
				#room select
				while r1c not in ['a', 'b']:
					r1c = input("\nDo you choose the \n|A| Wooden Door \n|B| Stone Door\n").lower()
				#room check
				else:
					if r1c == 'a':
						room = 2
					if r1c == 'b':
						room = 3


				
			elif room == 2:
				room_opponent_choice = self.opponents[random.randint(0, (len(self.opponents)-1))]
				room_opponent = self.opponent_creator(room_opponent_choice)
				print('\nYou encountered a', room_opponent, "\n")
				self.fight(self.player, [room_opponent])
				print('fight done')
				room = 3

			elif room == 3:
				print('\nYou enter the stone door and find an abandoned tresure chest lying on the ground')
				r3c = ''
				while r3c != 'a' and r3c != 'b':
					r3c = input('\nDo you\n|A| Open the chest\n|B| Leave the chest and move on\n').lower()
				else:
					if r3c == 'a':
						random_item = random.choice(list(self.player.items.items.keys()))
						print('\nYou open the chest to find a ', random_item)
						self.player.items.items[random_item][1] += 1
						print('This item', self.player.items.items[random_item][0], "\n")
						room = 4
					if r3c == 'b':
						print('\nYou walk away from the chest, never knowing what was inside.\n')
						room = 4

			elif room == 4:
				print("\nYou encounter your first boss\n")
				self.aspid = Aspid(self.player)
				self.fight(self.player, [self.aspid])
				print('\nAfter killing the boss, you find a pile of coins on the ground\n')
				self.player.coins += 150
				print('Beyond the coins, there is two tunnels, leading left and right')
				r4c = input('Which tunnel do you choose\n|A|Left\n|B|Right\n').lower()
				if r4c == 'a':
					room = 5
				if r4c == 'b':
					room = 6

			elif room == 5:
				"""
				shop room
				"""
				print('Welcome to the shop')
				self.shop.sell(self.player)
				print('Goodbye')
				room = 4

			elif room == 6:
				print('You walk into a room to find your dead body laying on the floor in a pool of blood')  
				self.you = You(self.player)
				print('Your dead body stands up')  
				self.fight(self.player, [self.you])
				room == 5

			elif room == 7:
				rm7_enemies = []
				fly_name = 'fly-'
				for i in range(5):
					fly_name = fly_name + str(i)
					rm7_enemies.append(fly_swarm(fly_name, self.player))
					fly_name = 'fly-'
				self.fight(self.player, rm7_enemies)
				room = 8
			
			elif room == 8:
				trader = Trader(self.player)
				sales_pitch = trader.bargian(self.player)
				if not sales_pitch:
					self.fight(self.player, [trader])
				room = random.randint(0, 7)
			
			elif room == 9:
				gold_brick = Gold_Brick(self.player)
				print('You find a gold brick lying on the ground')
				self.fight(self.player, [gold_brick])
				room = 10
			
			else:
				print("this game is nowhere close to being done, this room doesnt exist yet, sorry\n")
				room = random.randint(0, 9)

				
				


					

  



game = Main()
game.run_game()