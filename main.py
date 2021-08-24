import random
from Player import *
from Enemy import *
from Shop import *
from Tavern import *


player = Player('player_name')
tavern = Tavern()
  

def fight(player, opponent):
  """
  Decides who's turn it is in a fight, and has them take turns as needed
  """
  turn = 1
  while player.hp > 0 and opponent.hp > 0:
    if turn == 1:
      player.move(opponent)
      turn = 0
    if turn == 0:
      opponent.turn_(player)
      turn = 1

    if player.hp < 0:
      player.hp = 0
    if opponent.hp < 0:
      opponent.hp = 0
    print('\nYour health: ', round(player.hp, 1), "/", player.max_hp, "\nYour opponents health: ", round(opponent.hp, 1), '/', opponent.max_hp, "\n")
  else:
    if player.hp <= 0:
      print('You died! Game Over.')
      return
    elif opponent.hp <= 0:
      print('You killed ', opponent)
      return

def opponent_creator(opponent):
  if opponent == 'Zombie':
    return Zombie()
  if opponent == 'Wizard':
    return Wizard()



player_name = ' '
print(r"""  __  .__                             .__                                                             
_/  |_|  |__   ___________  ____      |__| ______      ____   ____        ____ _____    _____   ____  
\   __|  |  \_/ __ \_  __ _/ __ \     |  |/  ___/     /    \ /  _ \      /    \\__  \  /     \_/ __ \ 
 |  | |   Y  \  ___/|  | \\  ___/     |  |\___ \     |   |  (  <_> )    |   |  \/ __ \|  Y Y  \  ___/ 
 |__| |___|  /\___ /|__|   \___|      |__/____  >    |___|  /\____/     |___|  (____  |__|_|  /\___  >
           \/                                 \/          \/                 \/     \/      \/     \/ """)
print('v0.8\n\n\n')

shop = Shop()
#hello there

opponents = ["Zombie", "Wizard"]

room = 1
print('You stumble into a cave')
tavern.gamble(player)

while player.hp > 0:
  if room == 0:
    print('How did you get here?')
    player.hp == 0  

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


        
  if room == 2:
    room_opponent_choice = opponents[random.randint(0, (len(opponents)-1))]
    room_opponent = opponent_creator(room_opponent_choice)
    print('\nYou encountered a', room_opponent, "\n")
    fight(player, room_opponent)
    print('fight done')
    room = 3

  if room == 3:
    print('\nYou enter the stone door and find an abandoned tresure chest lying on the ground')
    r3c = ''
    while r3c != 'a' and r3c != 'b':
      r3c = input('\nDo you\n|A| Open the chest\n|B| Leave the chest and move on\n').lower()
    else:
      if r3c == 'a':
        random_item = random.choice(list(player.items.keys()))
        print('\nYou open the chest to find a ', random_item)
        player.items[random_item][1] += 1
        print('This item', player.items[random_item][0], "\n")
      if r3c == 'b':
        print('\nYou walk away from the chest, never knowing what was inside.\n')
      room = 4
    
  if room == 4:
    print("\nYou encounter your first boss\n")
    aspid = Aspid()
    fight(player, aspid)
    print('\nAfter killing the boss, you find a pile of coins on the ground\n')
    player.coins += 150
    print('Beyond the coins, there is two tunnels, leading left and right')
    r4c = input('Which tunnel do you choose\n|A|Left\n|B|Right\n').lower()
    if r4c == 'a':
      room = 5
    if r4c == 'b':
      room = 6
  
  if room == 5:
    """
    shop room
    """
    print('Welcome to the shop')
    shop.sell(player)
    print('Goodbye')
    room = 4

  if room == 6:
    pass


