import pygame
import math
import time

pygame.init()

# Set up the window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey Clock")

# Load the Mickey image and scale it to fit the window
mickey_image = pygame.image.load("mickeyclock.jpg")
mickey_image = pygame.transform.scale(mickey_image, window_size)

# Define the center of the screen as the pivot point for rotation
center = (window_size[0] / 2, window_size[1] / 2)

# Define the length and thickness of the clock hands
minute_hand_length = 100
minute_hand_thickness = 10
second_hand_length = 150
second_hand_thickness = 5

# Set the font and font size for the clock text
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    # Get the current time and convert it to minutes and seconds
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the Mickey image on the screen
    screen.blit(mickey_image, (0, 0))

    # Calculate the angles for the hands based on the current time
    minute_angle = math.radians(-90 + (minutes * 6))
    second_angle = math.radians(-90 + (seconds * 6))

    # Draw the minute hand
    minute_hand_end = (center[0] + minute_hand_length * math.cos(minute_angle),
                       center[1] + minute_hand_length * math.sin(minute_angle))
    pygame.draw.line(screen, (0, 0, 0), center, minute_hand_end, minute_hand_thickness)

    # Draw the second hand
    second_hand_end = (center[0] + second_hand_length * math.cos(second_angle),
                       center[1] + second_hand_length * math.sin(second_angle))
    pygame.draw.line(screen, (255, 0, 0), center, second_hand_end, second_hand_thickness)

    # Draw the current time text on the screen
    time_text = font.render(time.strftime("%M:%S"), True, (0, 0, 0))
    screen.blit(time_text, (center[0] - time_text.get_width() / 2, center[1] + 100))

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()