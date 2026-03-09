import random

class MemoryGame:
    def __init__(self):
        self.cards = ['A','A','B','B','C','C','D','D']
        random.shuffle(self.cards)
        self.revealed = ['*'] * len(self.cards)

    def play(self):
        while '*' in self.revealed:
            print("Cards:", self.revealed)

            i = int(input("Select first index: "))
            j = int(input("Select second index: "))

            if self.cards[i] == self.cards[j]:
                self.revealed[i] = self.cards[i]
                self.revealed[j] = self.cards[j]
                print("Match Found!")
            else:
                print("Not a match")

        print("Game Completed!")

game = MemoryGame()
game.play()