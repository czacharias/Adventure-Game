import random
from Player import *

class Shop:
  def __init__(self):
    self.inventory = {
    'apple':["heals 10% hp", 15, random.randint(0, 1)], 
    'health potion': ['heals 50% hp', 65, random.randint(0, 1)], 
    'bandages':['heals 25% hp', 35, random.randint(0, 1)], 
    'stick':['takes away 10% hp', 5, random.randint(0, 1)], 
    'random potion':['gives a random effect', 100, random.randint(0, 1)], 
    'attack buff':['increases attack by 2', 75, random.randint(0, 1)], 
    'hp buff':['increases health by 10', 75, random.randint(0, 1)],
    'mana regen':['gives 10 mana', 100, random.randint(0, 1)]
    }
    

  def sell(self, player):
    self._print_items()
    item = ''
    while item not in self.inventory.keys() and item != 'exit':
      item = input('\nWhat would you like to buy?\nType "exit" at anytime to leave the shop\n')
    if item == 'exit':
      self.stock()
      return
    elif self.inventory[item][2] > 0:
      selected = self.inventory[item]
      print('this item', selected[0], '\nthis item costs', selected[1], '')
      if player.coins >= selected[1]:
        confirm = ''
        while not(confirm == 'yes') and not(confirm == 'no'):
          confirm = input('\nAre you sure you want to buy this item:\n').lower()
        if confirm == 'yes':
          print('You bought', item,)
          self.inventory[item][2] -= 1
          player.coins -= selected[1]
          if item == 'attack buff':
              player.attack += 2
          if item == 'hp buff':
            player.hp += 10
        else:
          pass
        self.sell(player)
        
    else:
      print('\nThat item is out of stock, sorry\n')
      self.sell(player)
  
  def stock(self):
    for x in self.inventory.keys():
      self.inventory[x][2] = 10
    
  
  def _print_items(self) -> None:
    items_available = []
    for x in self.inventory:
      if self.inventory[x][2] >= 1:
        items_available.append(x)
    print(items_available)

