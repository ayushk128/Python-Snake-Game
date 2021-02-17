import pygame
x = pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Ayush")
quit_game = False
while not quit_game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            print("Quit")
            quit_game = True
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                print("Right Key pressed")
            if events.key == pygame.K_UP:
                print("Up key pressed")
