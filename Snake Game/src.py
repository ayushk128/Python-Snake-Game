import pygame

# pygame.init()  
# screen = pygame.display.set_mode((400,500))  
# done = False  
# while not done:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             done = True  
#     pygame.display.flip()

x = pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
close = False
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
    pygame.display.flip()
