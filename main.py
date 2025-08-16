import pygame

pygame.init()
# * main things that screen and caption of the window and the tick speed
# clock for controlling the frame rate with delta time
clock = pygame.time.Clock()
delta_time = 0.1

# configs of the window
pygame.display.set_caption("flappy bird")
width_screen = 800
height_screen = 600
screen_tuple = (width_screen, height_screen)
screen = pygame.display.set_mode(screen_tuple)

# * down this is the player things

player_gravity = 10  # Gravity effect on the player
player_jump_height = 10  # Height of the player's jump

# player sprite loading and scaling
player_sprite = pygame.image.load('bird.png').convert_alpha() # Load the player image
player_hight = 50
player_width = 50
player_sprite = pygame.transform.scale(player_sprite, (player_width, player_hight))  # Scale the player image

# player positions
player_x = 200
player_y = 50

# * main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))  # background color
    # * above this is the main things i would not change other than the background
    
    player_y = player_y + player_gravity
    print(player_y)
    
    
    screen.blit(player_sprite, (player_x, player_y))  # Draw the player sprite at the position in the tuple
    
    # * this is the update line and the fps line no need to tinker with this that much
    pygame.display.flip()  # Update the display
    
    clock.tick(60)  # Set the frame rate to 60 FPS

pygame.quit()