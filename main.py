import pygame

pygame.init()
# * main things that screen and caption of the window and the tick speed
# clock for controlling the frame rate with delta time
clock = pygame.time.Clock()
delta_time = 0.1

# * configs of the window
pygame.display.set_caption("Flappy bird")
width_screen = 800
height_screen = 600
screen_tuple = (width_screen, height_screen)
screen = pygame.display.set_mode(screen_tuple)

# * ground scroll variable
ground_scroll = 0
scroll_speed = 4

# * loading images
background = pygame.image.load("assets/background.png").convert_alpha()
background = pygame.transform.scale(background, (width_screen, height_screen - 100))

ground = pygame.image.load("assets/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (width_screen, 100))

# * main loop
running = True
while running:
    for event in pygame.event.get(): # used to close the window
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(background, (0, 0))  # Draw the background image
    screen.blit(ground, (ground_scroll, height_screen - 100))  # Draw the ground image
    
    # * above this is the main things i would not change other than the background
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 75:  # Reset ground scroll to create a looping effect
        ground_scroll = 0

    # * this is the update line and the fps line no need to tinker with this, that much
    pygame.display.flip()  # Update the display
    
    clock.tick(60)  # Set the frame rate to 60 FPS

pygame.quit()