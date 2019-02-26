from pygame import *


class Pete():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 48
        self.velocity = 5
        self.isWalking = False
        self.isLookingUp = True
        self.isLookingDown = False
        self.isLookingLeft = False
        self.isLookingRight = False
        self.isTracking = False
        self.isTalkative = False
        self.focused = None
        self.frameDelay = 10
        self.frameCount = 0
        self.tile = 0
        self.upTiles = [
            image.load('assets/images/characters/02/2 - U1.png'),
            image.load('assets/images/characters/02/2 - U2.png'),
            image.load('assets/images/characters/02/2 - U3.png')]
        self.downTiles = [
            image.load('assets/images/characters/02/2 - D1.png'),
            image.load('assets/images/characters/02/2 - D2.png'),
            image.load('assets/images/characters/02/2 - D3.png')]
        self.leftTiles = [
            image.load('assets/images/characters/02/2 - L1.png'),
            image.load('assets/images/characters/02/2 - L2.png'),
            image.load('assets/images/characters/02/2 - L3.png')]
        self.rightTiles = [
            image.load('assets/images/characters/02/2 - R1.png'),
            image.load('assets/images/characters/02/2 - R2.png'),
            image.load('assets/images/characters/02/2 - R3.png')]

    def draw(self, window):
        if self.isWalking:
            if self.isLookingUp:
                window.blit(self.upTiles[self.tile], (self.x, self.y))
            elif self.isLookingDown:
                window.blit(self.downTiles[self.tile], (self.x, self.y))
            elif self.isLookingLeft:
                window.blit(self.leftTiles[self.tile], (self.x, self.y))
            else:
                window.blit(self.rightTiles[self.tile], (self.x, self.y))
            self.frameCount += 1
            if self.frameCount % self.frameDelay == 1:
                self.tile += 1
                if self.tile > 2:
                    self.tile = 0
            return
        else:
            if self.isTracking:
                self.track_character(self.focused)
            if self.isLookingUp:
                window.blit(self.upTiles[0], (self.x, self.y))
            elif self.isLookingDown:
                window.blit(self.downTiles[0], (self.x, self.y))
            elif self.isLookingLeft:
                window.blit(self.leftTiles[0], (self.x, self.y))
            else:
                window.blit(self.rightTiles[0], (self.x, self.y))
            self.frameCount = 0
            self.tile = 0
            return

    def track_character(self, other):

        windowWidth = display.Info().current_w
        windowHeight = display.Info().current_h
        otherCenterX = other.x + other.width / 2
        otherCenterY = other.y + other.height / 2
        selfCenterX = self.x + other.width / 2
        selfCenterY = self.y + other.height / 2
        distanceX = abs(selfCenterX - otherCenterX)
        distanceY = abs(selfCenterY - otherCenterY)

        if distanceX < windowWidth / 4 and distanceY < windowHeight / 4:
            if selfCenterX < otherCenterX and distanceX > distanceY:
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = True
            elif selfCenterX > otherCenterX and distanceX > distanceY:
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = True
                self.isLookingRight = False
            elif selfCenterY < otherCenterY and distanceX < distanceY:
                self.isLookingUp = False
                self.isLookingDown = True
                self.isLookingLeft = False
                self.isLookingRight = False
            elif selfCenterY > otherCenterY and distanceX < distanceY:
                self.isLookingUp = True
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = False
        return
