import random
import math


class Warrior:

    def __init__(self, name="warior", health=0, maxAttack=0, maxBlock=0):
        self.name = name
        self.health = health
        self.maxAttack = maxAttack
        self.maxBlock = maxBlock

    def attack(self):
        attackAmt = self.maxAttack * (random.random() + .5)
        return attackAmt

    def block(self):
        blockAmt = self.maxBlock * (random.random() + .5)
        return blockAmt


class Battle:
    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAattackAmt = warriorA.attack()
        warriorBblockAmt = warriorB.block()
        print(warriorAattackAmt)
        print(warriorBblockAmt)

        fightResult = math.ceil(warriorAattackAmt - warriorBblockAmt)
        warriorB.health = warriorB.health - fightResult

        print("warrior {} attacks {} and has deal {} damage ".format(warriorA.name, warriorB.name,fightResult) )

        if warriorB.health <= 0:
            print("{} has died and {} has victorious ".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():

    maximun = Warrior("Maximun", 50, 10, 15)
    galaxon = Warrior("Galaxon", 50, 10, 10)

    battle = Battle()

    battle.startFight(maximun, galaxon)

main()