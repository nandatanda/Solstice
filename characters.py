from pygame import *


class Player():

    """Create an object containing all attributes and methods of the main character"""

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
        self.canGoUp = True
        self.canGoDown = True
        self.canGoLeft = True
        self.canGoRight = True
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
        """Redraw the player to the screen at its current x and y position"""
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

    def move(self, keys):
        """ Change the position of the player given the currently pressed keys"""
        width = display.Info().current_w
        height = display.Info().current_h
        self.switch_sides(width, height)

        if keys[K_UP] or keys[K_w]:
            self.isLookingUp = True
            self.isLookingDown = False
            self.isLookingLeft = False
            self.isLookingRight = False
            if self.canGoUp:
                self.isWalking = True
                self.y -= self.velocity
            else:
                self.isWalking = False
        elif keys[K_DOWN] or keys[K_s]:
            self.isLookingUp = False
            self.isLookingDown = True
            self.isLookingLeft = False
            self.isLookingRight = False
            if self.canGoDown:
                self.isWalking = True
                self.y += self.velocity
            else:
                self.isWalking = False
        elif keys[K_LEFT] or keys[K_a]:
            self.isLookingUp = False
            self.isLookingDown = False
            self.isLookingLeft = True
            self.isLookingRight = False
            if self.canGoLeft:
                self.isWalking = True
                self.x -= self.velocity
            else:
                self.isWalking = False
        elif keys[K_RIGHT] or keys[K_d]:
            self.isLookingUp = False
            self.isLookingDown = False
            self.isLookingLeft = False
            self.isLookingRight = True
            if self.canGoRight:
                self.isWalking = True
                self.x += self.velocity
            else:
                self.isWalking = False
        else:
            self.isWalking = False
        return

    def detect_collision(self, others):
        """Determine which direction is most immediately obstructing the player and set the corresponding attribute"""
        selfCenterX = self.x + self.width / 2
        selfCenterY = self.y + self.height / 2
        selfRangeX = self.width / 2
        selfRangeY = self.height / 2
        self.canGoUp = True
        self.canGoDown = True
        self.canGoLeft = True
        self.canGoRight = True
        for other in others:
            otherCenterX = other.x + other.width / 2
            otherCenterY = other.y + other.height / 2
            otherRangeX = other.width / 2
            otherRangeY = other.height / 2
            distanceX = abs(selfCenterX - otherCenterX)
            distanceY = abs(selfCenterY - otherCenterY)

            if distanceX < selfRangeX + otherRangeX:
                if distanceY < selfRangeY + otherRangeY:
                    if selfCenterY > otherCenterY and distanceX < distanceY:
                        self.canGoUp = False
                        self.canGoDown = True
                        self.canGoLeft = True
                        self.canGoRight = True
                        return
                    elif selfCenterY < otherCenterY and distanceX < distanceY:
                        self.canGoUp = True
                        self.canGoDown = False
                        self.canGoLeft = True
                        self.canGoRight = True
                        return
                    elif selfCenterX > otherCenterX and distanceX > distanceY:
                        self.canGoUp = True
                        self.canGoDown = True
                        self.canGoLeft = False
                        self.canGoRight = True
                        return
                    elif selfCenterX < otherCenterX and distanceX > distanceY:
                        self.canGoUp = True
                        self.canGoDown = True
                        self.canGoLeft = True
                        self.canGoRight = False
                        return
        return

    def switch_sides(self, width, height):
        """Change the player's position if it has left the current window's dimensions"""
        if self.y < 0 - self.height:
            self.y = height
        elif self.y > height:
            self.y = 0 - self.height
        if self.x < 0 - self.width:
            self.x = width
        elif self.x > width:
            self.x = 0 - self.width
        return

    def debug_mode(self, mode=0):
        if mode:
            print('xy =', self.x, self.y,
            '\tvelocity =', self.velocity,
            '\tisWalking =', self.isWalking,
            '\ttile =', self.tile,
            '\tframeCount =', self.frameCount, ' ',
            '\tcanGoUpDownLeftRight = ', self.canGoUp, self.canGoDown, self.canGoLeft, self.canGoRight)
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
