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

player_gravity = 5  # Gravity effect on the player
player_jump_height = 10  # Height of the player's jump

# player sprite loading and scaling
player_sprite = pygame.image.load('assets/bird.png').convert_alpha() # Load the player image
player_hight = 50
player_width = 50
player_sprite = pygame.transform.scale(player_sprite, (player_width, player_hight))  # Scale the player image

# player positions
player_x = 200
player_y = 50

player_rect= player_sprite.get_rect(topleft=(player_x, player_y))  # Create a rectangle for the player sprite

box = pygame.Rect(200, 400, 100, 50)

# * main loop
running = True
while running:
    for event in pygame.event.get(): # used to close the window
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))  # background color
    # * above this is the main things i would not change other than the background


    # * player controls
    keys = pygame.key.get_pressed()  # Get the state of all keys
    
    if keys[pygame.K_SPACE]:  # If the space key is pressed
        player_y -= player_jump_height  # Move the player up by the jump height
    
    
    # * this the gravity and the collision detection
    player_y += player_gravity # this is the gravity
    
    player_rect.topleft = (player_x, player_y) # updates te player position
    
    if box.colliderect(player_rect): # Check for collision with the box
        print("Collision detected!")
        player_y = box.top - player_hight # Reset player position to the top of the box
        color = (255, 0, 0) # for debugging purposes
    else:
        color = (0, 255, 0)
    
    # * drawing the player and the other drawings
    screen.blit(player_sprite, player_rect)  # Draw the player sprite at the position in the tuple
    pygame.draw.rect(screen, color, box)  # Draw the box at the specified position
    
    
    # * this is the update line and the fps line no need to tinker with this, that much
    pygame.display.flip()  # Update the display
    
    clock.tick(60)  # Set the frame rate to 60 FPS

pygame.quit()