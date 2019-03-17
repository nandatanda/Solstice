import pygame
import scenes
pygame.init()

viewport = 800, 600
window = pygame.display.set_mode((viewport))
pygame.display.set_caption('Work In Progress')          # name the window

scene = scenes.Intro()                                  # set up scene's properties
player = scene.player                                   # instance main character
npcList = scene.npcs                                    # list all onscreen npcs

run = True
while run:                                              # begin game loop
    pygame.time.delay(30)                               # control the framerate

    for event in pygame.event.get():                    # quit the game if window is closed
        if event.type == pygame.QUIT:
            run = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:       # quit the game if escape key is pressed
        run = False

    keys = pygame.key.get_pressed()                     # get a list of all pressed keys
    player.handle_collision(npcList)                    # control boundaries for player
    player.move(keys)
    player.talk(keys)

    scene.handle_events(player, npcList, keys)          # control player interactions

    player.debug(0)                                     # print the values of various player attributes

    window.fill((0, 0, 0))                              # redraw all elements here
    for npc in npcList:
        npc.draw(window)
    player.draw(window)
    pygame.display.update()