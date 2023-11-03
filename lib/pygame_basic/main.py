import pygame
import sys

# Initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_size = 50  # Size of the character, used for both width and height for simplicity (making it a square)

player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]  
# Initial position of the character:
# WIDTH // 2 places the character horizontally in the middle of the screen.
# HEIGHT - 2 * player_size places the character on the ground assuming the screen height is 600 and the character is 50px tall.

player_velocity = [0, 0]  
# The character's velocity in x and y directions:
# Initially set to [0, 0] because the character is not moving.

gravity = 0.5  
# The gravity value will be added to the y velocity each frame to simulate gravity pulling the character down.

jump_height = -10  
# The initial velocity in the y direction when a jump occurs.
# It's negative because in Pygame, the y coordinates increase going down the screen,
# so a negative value moves the character up.

# Laser setup
lasers = []  # List to keep track of all lasers
laser_velocity = 10  # Speed at which the laser will move

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    # Movement handling
    # Check for key presses
    if keys[pygame.K_LEFT]:
        # If the left arrow key is pressed, set the horizontal velocity to -5
        # This will move the character to the left on the screen since we're subtracting from the x-coordinate
        player_velocity[0] = -5
    elif keys[pygame.K_RIGHT]:
        # If the right arrow key is pressed, set the horizontal velocity to 5
        # This will move the character to the right on the screen since we're adding to the x-coordinate
        player_velocity[0] = 5
    else:
        # If neither left nor right keys are pressed, set the horizontal velocity to 0 (no horizontal movement)
        player_velocity[0] = 0

    # Shooting handling
    if keys[pygame.K_r]:  # Check if 'R' key is pressed
        lasers.append([player_pos[0] + player_size // 2 - 2, player_pos[1]])  # Center the laser on the player



    # Check for the jump key press
    if keys[pygame.K_SPACE]:
        # If the space key is pressed, set the vertical velocity to jump_height
        # jump_height is negative, which moves the character up on the screen since we're subtracting from the y-coordinate
        player_velocity[1] = jump_height

    # Update the position of each laser
    lasers = [[laser[0], laser[1] - laser_velocity] for laser in lasers if laser[1] > 0]

    # Apply gravity to the vertical velocity
    # Regardless of whether we're jumping or not, gravity constantly pulls the character down
    player_velocity[1] += gravity

    # Update the character's position based on its velocity
    player_pos[0] += player_velocity[0]  # Update the x-coordinate based on the horizontal velocity
    player_pos[1] += player_velocity[1]  # Update the y-coordinate based on the vertical velocity

    # Check for collision with the ground
    if player_pos[1] > HEIGHT - 2 * player_size:
        # If the character has moved below the ground level (due to gravity),
        # reset its position to the ground level to prevent it from falling further
        player_pos[1] = HEIGHT - 2 * player_size
        # Set the vertical velocity to 0 as the character is now on the ground and should not fall further
        player_velocity[1] = 0
    
    # Render
    screen.fill((0, 0, 0))
    pygame.draw.rect(
        screen,  # The surface to draw on (in this case, our game window)
        (255, 0, 0),  # The color of the rectangle, which is red in RGB format
        (player_pos[0], player_pos[1], player_size, player_size)  # The rectangle dimensions:
        # player_pos[0] is the x-coordinate of the rectangle (left position)
        # player_pos[1] is the y-coordinate of the rectangle (top position)
        # player_size is the width of the rectangle
        # player_size is also the height of the rectangle
        # This creates a square shape based on the size defined for the player
    )    


    # Draw all lasers
    for laser in lasers:
        # For each laser in the 'lasers' list, we draw a rectangle on the screen.
        # This loop goes through all the laser positions we've stored and creates a visual representation for each.

        # The 'pygame.draw.rect' function is used to draw the rectangle.
        # It takes several arguments:
        # 1. The 'screen' argument specifies which surface to draw on.
        #    We draw on the main game window surface, referred to as 'screen'.
        # 2. The color argument specifies the color of the rectangle.
        #    The color is given in RGB (red, green, blue) format, and (255, 255, 0) represents yellow.
        # 3. The position and size argument is a tuple containing:
        #    - laser[0]: The x-coordinate of the laser's position.
        #    - laser[1]: The y-coordinate of the laser's position.
        #    - The width of the laser rectangle, which we've set to 5 pixels.
        #    - The height of the laser rectangle, which we've set to 10 pixels.
        #    This places the rectangle at the laser's current position with the specified size.
        
        # When this line is executed, Pygame draws a small yellow rectangle at the coordinates specified by
        # the position of the laser, effectively rendering the laser on the screen for the player to see.
        pygame.draw.rect(screen, (255, 255, 0), (laser[0], laser[1], 5, 10))


    # Update the display
    pygame.display.flip()
    # This command is necessary to make any changes visible on the screen. 
    # When you draw something on the 'screen' surface, it does not become visible immediately. 
    # Instead, you need to call this function to update the entire surface of the window to reflect the changes.
    # It's like flipping to the next frame in an animation, hence the name 'flip'.

    # Control the frame rate
    clock.tick(30)
    # This line tells Pygame to wait enough to ensure the game does not run at more than 30 frames per second (FPS).
    # This is called 'frame rate capping'. By calling 'clock.tick(30)', we are making sure that at most 30 frames
    # are processed per second. If the game loop is running faster than this, 'tick' will make the program sleep
    # for a short time to slow down.
    # This is important to keep the game running at a consistent speed on all machines, regardless of how fast the
    # hardware is. Without this, the game might run too fast on some computers and too slow on others.
    # The number 30 can be adjusted to make the game run smoother (higher number) or to require less processing power (lower number).

pygame.quit()
sys.exit()
