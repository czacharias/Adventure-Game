import random

class Player:

  """
  Creates a player with String name and hp value int, exp int , inventory list/dictonary
  Attack stat (for damage), level
  """ 


  def __init__(self, name: str) -> None:
    self.name = name
    self.hp = 100
    self.max_hp = 100
    self.melee_defence = 0.25
    self.magic_defence = 0.25
    self.mana = 30
    self.max_mana = 30
    self.xp = 0
    self.level = 0
    self.items = {
      
      #item name:[item description, amount]
      
      'apple':["heals 10% hp", 0], 
      'health potion': ['heals 50% hp', 1], 
      'bandages':['heals 25% hp', 0], 
      'mana regen':['gives 10 mana', 0], 
      'stick':['takes away 10% hp', 0], 
      'random potion':['gives a random effect', 5]

      }
    self.attack = 10
    self.attacks = {

      #attack name:[damage type, damage, mana cost, threshold for hitting, element]

      'fireball':['magic', 25, 10, 75, 'fire'],
      'light attack':['melee', self.attack, 0, 95, 'earth'],
      'heavy attack':['melee', (self.attack*2), 0, 75, 'earth']

      }
    self.coins = 99999

  
  def move(self, opponent) -> None:
    """
    Every turn, this function runs, allows the player to choose an action
    """
    turn_move = ''
    while turn_move not in ['attack', 'use item', 'guard']:
      turn_move = input('What do you want to do?\n|Attack|  |Use Item|  |Guard|\n').lower()
    else:
      if turn_move == 'attack':
        self.attack_(opponent)
      elif turn_move == "use item":
        self.item_use(opponent)
      elif turn_move == 'guard':
        if self.melee_defence >= 0.9:
          print('Defence is maxed out, try another action\n')
          self.move(opponent)
        else:
          self.melee_defence += 0.1
      else:
        print("Invalid input")

  def attack_(self, opponent) -> None:
    """
    Player picks between attacks and damages their opponent
    """

    self._print_attacks()

    attack_choice = ""
    while attack_choice not in self.attacks.keys():
      attack_choice = input('What attack do you want to use?\n').lower()
      if attack_choice == 'back':
        self.move(opponent)
    x = random.randint(0, 100)

    if self.mana > self.attacks[attack_choice][2]:
      if x < self.attacks[attack_choice][3]:
        
        opponent.take_damage(self.attacks[attack_choice][1], self.attacks[attack_choice][0])
        self.mana -= self.attacks[attack_choice][2]
      else:
        print('You missed your attack!')
    else:
      print('Not enough mana, pick another attack')

    #if attack_choice == 'heavy attack':
    #  x = random.randint(0, 100)
    #  if x < 75:
    #    opponent.take_damage(self.attack * 2)
    #  else: 
    #    print('You missed your attack')
    #if attack_choice == 'light attack':
    #  y = random.randint(0, 100)
    #  if y < 90:
    #    opponent.take_damage(self.attack)
    #  else:
    #    print('You missed your attack!')
        
  def _print_attacks(self) -> None:
    attacks_available = []
    for x in self.attacks.keys():
      attacks_available.append(x)
    print(attacks_available)

  def _print_items(self) -> None:
    items_available = []
    for x in self.items:
      if self.items[x][1] >= 1:
        items_available.append(x)
    print(items_available)
    

  def item_use(self, enemy):
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
        return self.move(enemy)
    
    item_confirm = ""


    while item_confirm != 'yes' and item_confirm != 'no':
      item_confirm = input(self.items[item][0] + "\nAre you sure you want to use this item? ").lower()
      if item_confirm == 'yes':
        
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
      
        elif item_confirm == 'no':
          self.item_use(enemy)




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
      damage_taken = (damage -(damage * self.melee_defence)-(damage_dropoff//100))
      self.hp -= round(damage_taken, 1)
      print('You were hit for', round(damage_taken, 1), ' damage')
    elif damage_type == 'magic':
      damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
      damage_taken = (damage -(damage * self.magic_defence)-(damage_dropoff//100))
      self.hp -= round(damage_taken, 1)
      print('You were hit for', round(damage_taken, 1), ' damage')

    

  def end_fight(self, exp_gained):
    """
    At the end of the fight, this function changes xp to levels and gives upgrades
    """
    self.xp += exp_gained
    self.mele_defence = 0.25
    if self.xp >= 100:
      self.level += 1
      self.xp = 0
      bonus_choice = ""
      

      while bonus_choice not in ['health', 'attack damage', 'defence']:
        bonus_choice = input('Do you want to upgrade your health, your attack damage, or your defence?').lower
      else:
        if bonus_choice == 'health':
          self.hp += self.level * 10
          print('Your hp has increased to ', self.hp)
        elif bonus_choice == 'attack damage':
          self.attack += self.level * 1.5
          print('Your hp has increased to ', self.attack)
        elif bonus_choice == "defence":
          self.defence += self.level