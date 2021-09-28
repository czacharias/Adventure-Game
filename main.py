import random
from Player import *
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

	def fight(self, player, opponents):
		"""
		Decides who's turn it is in a fight, and has them take turns as needed
		"""
		if len(opponents) == 1:
			for opponent in opponents:

				turn = 1
				while player.hp > 0 and opponent.hp > 0:
					if turn == 1:
						player.move([opponent])
						turn = 0
					if turn == 0:
						opponent.turn_(player)
						turn = 1
		else:
			player.move(opponents)
			for opponent in opponents:
				opponent.turn_(player)

		print('\nYour health: ', round(player.hp, 1), "/", player.max_hp) 
		for opponent in opponents:
			print(opponent.name, "health: ", round(opponent.hp, 1), '/', opponent.max_hp)
		if player.hp < 0:
				player.hp = 0
		if opponent.hp < 0:
				opponent.hp = 0
		else:
			if player.hp <= 0:
				print('You died! Game Over.')
				return
			elif opponent.hp <= 0:
				print('You killed ', opponent)
				opponent.item_drop(player)
				return

	def opponent_creator(self, opponent):
		if opponent == 'Zombie':
			return Zombie()
		if opponent == 'Wizard':
			return Wizard()


	def run_game(self):
		print(r"""___________.__                               .__                                                               
\__    ___/|  |__   ___________   ____       |__| ______       ____   ____         ____ _____    _____   ____  
  |    |   |  |  \_/ __ \_  __ \_/ __ \      |  |/  ___/      /    \ /  _ \       /    \\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/|  | \/\  ___/      |  |\___ \      |   |  (  <_> )     |   |  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  >__|    \___  >     |__/____  >     |___|  /\____/      |___|  (____  /__|_|  /\___  >
                \/     \/            \/              \/           \/                  \/     \/      \/     \/ """)







		room = 6

		print('You stumble into a cave')
		self.tavern.gamble(self.player)

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
				self.aspid = Aspid()
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

			elif room == 7:
				rm7_enemies = []
				fly_name = 'fly-'
				for i in range(13):
					fly_name = fly_name + str(i)
					rm7_enemies.append(fly_swarm(fly_name))
					fly_name = 'fly-'
				self.fight(self.player, rm7_enemies)
					

  



game = Main()
game.run_game()