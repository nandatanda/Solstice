import pygame
import characters
import elements
import scenes
pygame.init()

viewport = 800, 600
window = pygame.display.set_mode((viewport))    # set up the window
pygame.display.set_caption('Work In Progress')  # name the window

scene = scenes.Intro()
player = scene.player                           # instance main character
npcList = scene.npcs                            # list all onscreen npcs

prompt = elements.Prompt('space')

run = True
while run:                                      # begin game loop
    pygame.time.delay(30)                       # control the framerate

    for event in pygame.event.get():            # quit the game if necessary
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()             # get a list of all pressed keys
    player.detect_collision(npcList)            # control boundaries for player
    player.move(keys)

    player.debug_mode(1)                        # print the values of various player attributes

    window.fill((0, 0, 0))                      # redraw all elements here
    for npc in npcList:
        npc.draw(window)
    player.draw(window)
    prompt.draw(window)
    pygame.display.update()