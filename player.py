from pygame import *


class Penny():

    """Create an object containing all attributes and methods of the main character"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 48
        self.velocity = 4
        self.currentTile = 0
        self.currentFocus = None
        self.isAdvancingDialogue = False
        self.walkTimer = 10
        self.talkTimer = 10
        self.walkFrames = 0
        self.talkFrames = 0
        self.isWalking = False
        self.isTalking = False
        self.isTalkative = False
        self.isFacingUp = True
        self.isFacingDown = False
        self.isFacingLeft = False
        self.isFacingRight = False
        self.isBlockedUp = False
        self.isBlockedDown = False
        self.isBlockedLeft = False
        self.isBlockedRight = False
        self.exitMapUp = False
        self.exitMapDown = False
        self.exitMapLeft = False
        self.exitMapRight = False
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
        """Draw sprite at the current x and y position"""
        if self.isWalking:
            # select a walking sprite frame
            if self.isFacingUp:
                window.blit(self.upTiles[self.currentTile], (self.x, self.y))
            elif self.isFacingDown:
                window.blit(self.downTiles[self.currentTile], (self.x, self.y))
            elif self.isFacingLeft:
                window.blit(self.leftTiles[self.currentTile], (self.x, self.y))
            else:
                window.blit(self.rightTiles[self.currentTile], (self.x, self.y))

            # advance the sprite animation
            self.walkFrames += 1
            if self.walkFrames % self.walkTimer == 1:
                self.currentTile += 1
                if self.currentTile > 2:
                    self.currentTile = 1
        else:
            # select a standing sprite frame
            if self.isFacingUp:
                window.blit(self.upTiles[0], (self.x, self.y))
            elif self.isFacingDown:
                window.blit(self.downTiles[0], (self.x, self.y))
            elif self.isFacingLeft:
                window.blit(self.leftTiles[0], (self.x, self.y))
            else:
                window.blit(self.rightTiles[0], (self.x, self.y))

            # reset the sprite animation
            self.walkFrames = 0
            self.currentTile = 0
        return

    def move(self, keys):
        """ Change the position of the player given the currently pressed keys"""
        # get current window dimensions
        windowWidth = display.Info().current_w
        windowHeight = display.Info().current_h

        # handle off-screen movement
        self.switch_sides(windowWidth, windowHeight)

        # move the player
        if keys[K_UP] or keys[K_w]:
            self.set_facing(up=True)
            if not self.isBlockedUp:
                self.isWalking = True
                self.y -= self.velocity
            else:
                self.isWalking = False
        elif keys[K_DOWN] or keys[K_s]:
            self.set_facing(down=True)
            if not self.isBlockedDown:
                self.isWalking = True
                self.y += self.velocity
            else:
                self.isWalking = False
        elif keys[K_LEFT] or keys[K_a]:
            self.set_facing(left=True)
            if not self.isBlockedLeft:
                self.isWalking = True
                self.x -= self.velocity
            else:
                self.isWalking = False
        elif keys[K_RIGHT] or keys[K_d]:
            self.set_facing(right=True)
            if not self.isBlockedRight:
                self.isWalking = True
                self.x += self.velocity
            else:
                self.isWalking = False
        else:
            self.isWalking = False
        return

    def handle_collision(self, others):
        """
        Determine which directions are obstructing the player and set the corresponding attribute(s)
        """
        # reset blocking attributes
        self.set_blocking(reset=True)
        self.isTalkative = False
        self.currentFocus = None

        for other in others:
            dx, dy = self.get_distance(other)

            if self.find_collision(other):
                # assign closest talkative npc as currentFocus
                self.handle_focus(other)

                # assign blocking attributes
                self.handle_blocking(other)
        return

    def get_distance(self, other):
        myX = self.x + self.width / 2
        myY = self.y + self.height / 2
        otherX = other.x + other.width / 2
        otherY = other.y + other.height / 2

        x = abs(myX - otherX)
        y = abs(myY - otherY)
        return x, y

    def get_center(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2
        return x, y

    def find_collision(self, other):
        dx, dy = self.get_distance(other)
        rx = (self.width / 2) + (other.width / 2)
        ry = (self.height / 2) + (other.height / 2)

        if dx < rx and dy < ry:
            return True
        return False

    def handle_blocking(self, other):
        ox = other.x
        oy = other.y
        mx, my = self.get_center()
        dx, dy = self.get_distance(other)

        if dx < dy:
            if my > oy:
                self.isBlockedUp = True
            else:
                self.isBlockedDown = True
        if dx > dy:
            if mx > ox:
                self.isBlockedLeft = True
            else:
                self.isBlockedRight = True
        return

    def set_blocking(self, up=True, down=True, left=True, right=True, reset=False):
        if reset:
            up = False
            down = False
            left = False
            right = False
        self.isBlockedUp = up
        self.isBlockedDown = down
        self.isBlockedLeft = left
        self.isBlockedRight = right
        return

    def set_facing(self, up=False, down=False, left=False, right=False):
        self.isFacingUp = up
        self.isFacingDown = down
        self.isFacingLeft = left
        self.isFacingRight = right
        return

    def handle_focus(self, npc):
        if npc.isTalkative:
            self.isTalkative = True
            self.currentFocus = npc
        return

    def talk(self, keys):
        self.isAdvancingDialogue = False
        if self.isTalking:
            if self.isWalking:
                self.isTalking = False
                self.talkFrames = 0
            elif keys[K_SPACE]:
                if self.talkFrames >= self.talkTimer:
                    self.isAdvancingDialogue = True
                    self.talkFrames = 0
            else:
                self.talkFrames += 1
        elif self.isTalkative:
            if keys[K_SPACE]:
                self.isTalking = True
                self.isAdvancingDialogue = True
        return

    def switch_sides(self, width, height):
        """Swap which side the player is on when leaving the map"""
        # reset map exit values
        self.exitMapUp = False
        self.exitMapDown = False
        self.exitMapLeft = False
        self.exitMapRight = False

        # move player to bottom
        if self.y < 0 - self.height:
            self.exitMapUp = True
            self.y = height

        # move player to top
        elif self.y > height:
            self.exitMapDown = True
            self.y = 0 - self.height

        # move player to left
        elif self.x > width:
            self.exitMapRight = True
            self.x = 0 - self.width

        # move player to right
        elif self.x < 0 - self.width:
            self.exitMapLeft = True
            self.x = width
        return

    def debug(self, mode=0):
        """Display attributes of the player for debugging"""
        if mode:
            print('xy =', self.x, self.y,
            #'\tvelocity =', self.velocity,
            #'\tisWalking =', self.isWalking,
            #'\ttile =', self.currentTile,
            #'\tframeCount =', self.walkFrames, ' ',
            #'\tcanGoUpDownLeftRight = ', self.isBlockedUp, self.isBlockedDown, self.isBlockedLeft, self.isBlockedRight,
            '\tisTalkative =', self.isTalkative,
            '\tisTalking =', self.isTalking,
            '\tfocus =', self.currentFocus)
        return