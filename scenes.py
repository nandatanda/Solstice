import pygame
import player
import characters
import elements


class Intro():
    def __init__(self):
        self.playerIsPresent = True
        self.player = player.Penny(300, 500)
        self.pete = characters.Pete(300,100)
        self.npcs = [self.pete]

        self.pete.isLookingUp = False
        self.pete.isLookingDown = True
        self.pete.isTracking = True
        self.pete.isTalkative = True
        self.pete.focused = self.player

        self.exitingMapUp = False
        self.exitingMapDown = False
        self.exitingMapLeft = False
        self.exitingMapRight = False

        self.dialogueCounter = 1
        self.dialogueDict = {
            1 : "Hi, I'm Pete. Pleased to meet you.",
            2 : "I don't say much as of yet, but I'll be more helpful soon..",
            3 : "Enjoy your stay in this bleak horrorscape!"}

    def handle_events(self, player, npcs, keys):
        if player.isTalking:
            #print('istalking')
            if player.isAdvancingDialogue:
                #print('spacepressed')
                if player.currentFocus == npcs[0]:
                    if self.dialogueCounter in self.dialogueDict:
                        print(self.dialogueDict.get(self.dialogueCounter))
                        self.dialogueCounter += 1
        return