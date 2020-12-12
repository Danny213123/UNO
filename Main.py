import random as rand
import time
log = open("errorlog.txt", "w")
unocards = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10", "CG", "CG", "CG", "CG", "P4", "P4"]
rand.shuffle(unocards)
class game():
  def __init__ (self, players, playerhand, startcards, deck):
    self.players = players
    self.startcards = startcards
    self.deck = deck
    self.hand = [""] * self.players
    self.playerhand = playerhand
  def hannd(self):
    for x in range (len(self.hand)):
      self.hand[x] = [""] * self.startcards
  def distribute (self):
    deck = self.deck
    for x in range (self.players):
      for y in range (self.startcards):
        q = rand.randint(0, len(deck) - 1)
        log.write(str(x)),log.write(", "),log.write(str(y)),log.write(", "),log.write(deck[q]),log.write(", ")
        self.hand[x][y] = deck[q]
        self.deck.remove(deck[q])
  def main (self):
    unogame = True
    card = []
    card.append(self.deck[rand.randint(0, len(self.deck))])
    turn = rand.randint(0, self.players - 1)
    print (self.hand)
    print (card[0])
    print (len(self.hand[turn]))
    while unogame == True:
      if (turn != self.playerhand):
        for x in range (len(self.hand[turn])):
          if (self.hand[turn][x][0] == card[-1][0]):
            turn += 1
            break
      unogame = False

Game = game(2, 1, 6, unocards)
Game.hannd()
Game.distribute()
Game.main()
log.close()

