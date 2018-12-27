from pygame import *


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 48
        self.velocity = 5
        self.isWalking = False
        self.isLookingUp = False
        self.isLookingDown = True
        self.isLookingLeft = False
        self.isLookingRight = False
        self.frameDelay = 10
        self.frameCount = 0
        self.tile = 0
        self.upTiles = [
            image.load('assets/images/characters/01/1 - U1.png'),
            image.load('assets/images/characters/01/1 - U2.png'),
            image.load('assets/images/characters/01/1 - U3.png')]
        self.downTiles = [
            image.load('assets/images/characters/01/1 - D1.png'),
            image.load('assets/images/characters/01/1 - D2.png'),
            image.load('assets/images/characters/01/1 - D3.png')]
        self.leftTiles = [
            image.load('assets/images/characters/01/1 - L1.png'),
            image.load('assets/images/characters/01/1 - L2.png'),
            image.load('assets/images/characters/01/1 - L3.png')]
        self.rightTiles = [
            image.load('assets/images/characters/01/1 - R1.png'),
            image.load('assets/images/characters/01/1 - R2.png'),
            image.load('assets/images/characters/01/1 - R3.png')]

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

    def move(self, keys, isColliding):
        width = display.Info().current_w
        height = display.Info().current_h

        if not isColliding:
            if keys[K_UP] or keys[K_w]:
                self.isWalking = True
                self.isLookingUp = True
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = False
                self.y -= self.velocity
            elif keys[K_DOWN] or keys[K_s]:
                self.isWalking = True
                self.isLookingUp = False
                self.isLookingDown = True
                self.isLookingLeft = False
                self.isLookingRight = False
                self.y += self.velocity
            elif keys[K_LEFT] or keys[K_a]:
                self.isWalking = True
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = True
                self.isLookingRight = False
                self.x -= self.velocity
            elif keys[K_RIGHT] or keys[K_d]:
                self.isWalking = True
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = True
                self.x += self.velocity
            else:
                self.isWalking = False
        else:
            pass
        return


class NPC():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 48
        self.velocity = 5
        self.isWalking = False
        self.isLookingUp = False
        self.isLookingDown = False
        self.isLookingLeft = True
        self.isLookingRight = False
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

    def set_facing(self, player):
        windowWidth = display.Info().current_w
        windowHeight = display.Info().current_h
        playerCenterX = player.x + player.width / 2
        playerCenterY = player.y + player.height / 2
        selfCenterX = self.x + player.width / 2
        selfCenterY = self.y + player.height / 2

        distanceX = abs(selfCenterX - playerCenterX)
        distanceY = abs(selfCenterY - playerCenterY)

        if distanceX < windowWidth / 4 and distanceY < windowHeight / 4:
            if selfCenterX < playerCenterX and distanceX > distanceY:
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = True
            elif selfCenterX > playerCenterX and distanceX > distanceY:
                self.isLookingUp = False
                self.isLookingDown = False
                self.isLookingLeft = True
                self.isLookingRight = False
            elif selfCenterY < playerCenterY and distanceX < distanceY:
                self.isLookingUp = False
                self.isLookingDown = True
                self.isLookingLeft = False
                self.isLookingRight = False
            elif selfCenterY > playerCenterY and distanceX < distanceY:
                self.isLookingUp = True
                self.isLookingDown = False
                self.isLookingLeft = False
                self.isLookingRight = False
        return

    def detect_collision(self, player):
        playerCenterX = player.x + player.width / 2
        playerCenterY = player.y + player.height / 2
        playerRangeX = player.width / 2 + player.velocity
        playerRangeY = player.height / 2 + player.velocity
        selfCenterX = self.x + self.width / 2
        selfCenterY = self.y + self.height / 2
        selfRangeX = self.width / 2 + self.velocity
        selfRangeY = self.height / 2 + self.velocity

        distanceX = abs(selfCenterX - playerCenterX)
        distanceY = abs(selfCenterY - playerCenterY)

        if distanceX < selfRangeX + playerRangeX:
            if distanceY < selfRangeY + playerRangeY:
                return True
        return False
