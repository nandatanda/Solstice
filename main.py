import pygame
import characters
pygame.init()

viewport = 800, 600
window = pygame.display.set_mode((viewport))    # set up the window
pygame.display.set_caption('Work In Progress')  # name the window

player = characters.Player(0, 0)                # instance all characters here
pete = characters.NPC(200,200)
bob = characters.NPC(500,100)

npcList = [pete]                                # list all onscreen npcs

run = True
while run:                                      # begin game loop
    pygame.time.delay(30)                       # control the framerate

    for event in pygame.event.get():            # quit the game if necessary
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()             # get a list of all pressed keys
    player.detect_collision(npcList)            # control boundaries for player
    player.move(keys)
    for npc in npcList:
        npc.set_facing(player)                  # turn npc when player approaches

    player.debug_mode(1)                        # print the values of various player attributes

    window.fill((0, 0, 0))                      # redraw all elements here
    for npc in npcList:
        npc.draw(window)
    player.draw(window)
    pygame.display.update()