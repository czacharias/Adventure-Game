import random
from Player import *
from Shop import *


class Tavern:
  def __init__(self):
    self.games = [
      'roulette',
      'slots'
      ]
    self.slot_1 = [
      1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
    ]
    self.slot_2 = [
      1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
    ]
    self.slot_3 = [
      1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
    ]
    self.shop = Shop()

  
  
  def gamble(self, player):
    print('\n', self.games)
    game = ''
    while game not in self.games:
      game = input('What game do you want to play? ').lower()
    if game == 'roulette':
      self.roulette(player)
    if game == 'slots':
      self.slots(player)

  def roulette(self, player):
    bet = ''
    while bet == '':
      bet = int(input('\nHow much do you want to bet? '))
      if bet > player.coins:
        print('You dont have enough coins to bet that')
        bet = ''
      
    p_number = -1

    
    while True:
      p_number = input('Pick a number between 0 and 36, or choose odds or evens: ').lower()
      if p_number == 'odds' or p_number == 'evens':
        break
      elif int(p_number) in range(0, 37):
        break

    if type(p_number) == int:
      x = random.randint(0, 36)
      if p_number == x:
        winnings = bet*10
        print('The wheel landed on ', p_number, ' you win!\nYou won ', winnings)
        player.coins += winnings
      else:
        print(x)
        retry = ''
        while retry != 'yes' and retry != 'no':
          retry = input('You lost, try again? ').lower()
        if retry == 'yes':
          self.roulette(player)
        elif retry == 'no':
          self.gamble(player)
    elif type(p_number) == str:
      x = random.randint(0, 36)
      if p_number == 'evens' and x%2 == 0 or p_number == 'odds' and x%2 != 0:
        winnings = bet*10
        print('The wheel landed on ', p_number, ' you win!\nYou won ', winnings)
        player.coins += winnings
      else:
        print(x)
        retry = ''
        while retry != 'yes' and retry != 'no':
          print('You have ', player.coins(), ' coins')
          retry = input('You lost, try again? ').lower()
        if retry == 'yes':
          self.roulette(player)
        elif retry == 'no':
          self.gamble(player)
      

  def slots(self, player):
    bet = ''
    while bet == '':
      bet = int(input('\nHow much d you want to bet? '))
      if bet > player.coins:
        print('You dont have enough coins to bet that')
        bet = ''
    roll_1 = self.slot_1[random.randint(0, len(self.slot_1)-1)]
    roll_2 = self.slot_2[random.randint(0, len(self.slot_2)-1)]
    roll_3 = self.slot_3[random.randint(0, len(self.slot_3)-1)]
    print('\n|', roll_1, '|', roll_2, '|', roll_3, '|')
    if roll_1 == roll_2 == roll_3:
      print('You won ', bet*roll_1, ' coins')
      player.coins += bet*roll_1
    elif roll_1 == 1 and roll_2 == 2 and roll_3 == 3:
      print('You won ', bet, ' coins')
      player.coins += bet*roll_1
    else:
      print('You lost ', bet, ' coins')
      player.coins -= bet
    retry = ''
    while retry != 'yes' and retry != 'no':
      print('You have ', player.coins(), ' coins')
      retry = input('\nBet again? ').lower()
    if retry == 'yes':
      self.slots(player)
    elif retry == 'no':
      self.gamble(player)
  
    




    

