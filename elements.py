from pygame import *

class Prompt():
    def __init__(self, key, isOn=True):
        self.key = key
        self.isOn = isOn
        self.x = self.getX()
        self.y = self.getY()
        self.keys = {
            'space' : image.load('assets/images/elements/prompt_space_100x20.jpg'),}

    def draw(self, window):
        if self.isOn:
            window.blit(self.keys.get(self.key), (self.x, self.y))
        return

    def getX(self):
        winX = display.Info().current_w
        return winX * 0.03

    def getY(self):
        winY = display.Info().current_h
        return winY * 0.93