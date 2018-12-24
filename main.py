import pygame
import characters
pygame.init()

viewport = 800, 600
window = pygame.display.set_mode((viewport))
pygame.display.set_caption('Work In Progress')

player = characters.Player(0, 0)

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.move(keys)
 
    window.fill((0, 0, 0))
    player.draw(window)
    pygame.display.update()