import pygame

pygame.init()

pygame.display.set_caption("flappy bird")
screen = pygame.display.set_mode((800, 600))
running = True

player = pygame.image.load('').convert_alpha() 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    
    pygame.display.flip()  # Update the display
pygame.quit()
exit()