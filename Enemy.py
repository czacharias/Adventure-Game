import random
from Player import *

class Enemy:
  """
  Parent class for all types of opponents, has basic attack and take damage functions
    Has a name, hp, attack, and defence
  """
  def __init__(self, name, hp, attack, melee_defence, magic_defence):
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.attack = attack
    self.melee_defence = melee_defence
    self.magic_defence = magic_defence

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

  def take_damage(self, damage, damage_type):
    """
    For when the enemy had damage dealt to them, run in the player attack_ function
    """
    
    if damage_type == 'melee':
      damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
      damage_taken = (damage -(damage * self.melee_defence)-(damage_dropoff//100))
      self.hp -= damage_taken
      print('You hit the ', self.name, ' for ', damage_taken, ' damage!')

    elif damage_type == 'magic':
      damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
      damage_taken = (damage -(damage * self.magic_defence)-(damage_dropoff//100))
      self.hp -= damage_taken
      print('You hit the ', self.name, ' for ', damage_taken, ' damage!')



    




class Zombie(Enemy):
  """
  Subclass of enemy, no new functions
  """
  def __init__(self):
    super().__init__("Zombie", 50, 5 , 0.25, 0)


    

class Wizard(Enemy):
  """
  Subclass of enemy, has healing abilties and different attacks
  """
  def __init__(self):
    super().__init__('Wizard', 75, 15, 0.05, 0.2)

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
      self.take_damage(atk_dmg, 'magic')
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
    super().__init__('Aspid', 125, 10, 0.1, 0.1)
  
  def attack_(self, player: Player) -> None:
    damage_dropoff = random.uniform(self.attack * 0.1, self.attack * 0.5)
    luck = random.randint(1, 100)

    if luck <= 75:
      print('The Aspid charges towards you and hits you dead center')
      player.take_damage(self.attack - (damage_dropoff//100), 'melee')
    if 75 < luck <= 100:
      print('The Aspid shoots acid at you, which does double damage')
      player.take_damage((self.attack - (damage_dropoff//100))*2, 'melee') 