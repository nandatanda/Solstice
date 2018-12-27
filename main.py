import pygame
import characters
pygame.init()

viewport = 800, 600
window = pygame.display.set_mode((viewport))
pygame.display.set_caption('Work In Progress')

player = characters.Player(0, 0)
npc = characters.NPC(200,200)

npcList = [npc]                         # list all onscreen npcs

run = True
while run:
    pygame.time.delay(30)               # control the framerate

    for event in pygame.event.get():    # quit the game if necessary
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()     # get a list of all pressed keys
    player.detect_collision(npcList)    # control boundaries for player
    player.move(keys)
    npc.set_facing(player)              # turn npc when player approaches

    player.debug_data(1)

    window.fill((0, 0, 0))
    npc.draw(window)
    player.draw(window)
    pygame.display.update()