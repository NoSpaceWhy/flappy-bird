import pygame

pygame.init()
# * main things that screen and caption of the window

pygame.display.set_caption("flappy bird")
width_screen = 800
height_screen = 600
screen_tuple = (width_screen, height_screen)
screen = pygame.display.set_mode(screen_tuple)

# * down this is the player things
player_sprite = pygame.image.load('bird.png').convert_alpha() # Load the player image

player_hight = 50
player_width = 50
player_sprite = pygame.transform.scale(player_sprite, (player_width, player_hight))  # Scale the player image

# player positions
player_x = 100
player_y = 50
player_tuple = (player_x, player_y)

# * main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))  # background color
    # * above this is the main things i would not change other than the background
    
    screen.blit(player_sprite, player_tuple)
    
    pygame.display.flip()  # Update the display
pygame.quit()
exit()