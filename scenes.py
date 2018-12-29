import pygame
import characters
import elements


class Intro():
    def __init__(self):
        self.playerIsPresent = True
        self.player = characters.Penny(300, 500)
        self.pete = characters.Pete(400,100)
        self.npcs = [self.pete]

        self.pete.isLookingUp = False
        self.pete.isLookingDown = True
        self.pete.isTracking = True
        self.pete.focused = self.player

        self.exitMapUp = False
        self.exitMapDown = False
        self.exitMapLeft = False
        self.exitMapRight = False

    def do_stuff(self):
        pass