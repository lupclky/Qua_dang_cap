# Import pygame library
import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen size and create a window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Define the snake class
class Snake:
    # Initialize the snake with a position, a direction and a body
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.body = []
        self.length = 3

    # Draw the snake on the screen
    def draw(self):
        # Draw the head of the snake
        pygame.draw.rect(screen, GREEN, [self.x, self.y, 10, 10])
        # Draw the body of the snake
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], 10, 10])

    # Update the snake's position and body
    def update(self):
        # Add a new segment to the body with the current head position
        self.body.append([self.x, self.y])
        # Remove the last segment of the body if the body is too long
        if len(self.body) > self.length:
            del self.body[0]
        # Move the head of the snake by the direction vector
        self.x += self.dx
        self.y += self.dy

    # Handle keyboard input to change the direction of the snake
    def handle_input(self):
        # Get the events from pygame
        events = pygame.event.get()
        # Loop through the events
        for event in events:
            # If the user presses a key
            if event.type == pygame.KEYDOWN:
                # If the key is an arrow key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # Set the direction vector accordingly
                    if event.key == pygame.K_LEFT:
                        self.dx = -10
                        self.dy = 0
                    elif event.key == pygame.K_RIGHT:
                        self.dx = 10
                        self.dy = 0
                    elif event.key == pygame.K_UP:
                        self.dx = 0
                        self.dy = -10
                    elif event.key == pygame.K_DOWN:
                        self.dx = 0
                        self.dy = 10

    # Check if the snake is out of bounds or collides with itself
    def check_collision(self):
        # If the snake goes beyond the left or right edge of the screen
        if self.x < 0 or self.x > SCREEN_WIDTH - 10:
            # Return True to indicate a collision
            return True
        # If the snake goes beyond the top or bottom edge of the screen
        if self.y < 0 or self.y > SCREEN_HEIGHT - 10:
            # Return True to indicate a collision
            return True
        # Loop through the segments of the body (except the head)
        for segment in self.body[:-1]:
            # If the head position is equal to a body segment position
            if self.x == segment[0] and self.y == segment[1]:
                # Return True to indicate a collision
                return True
        # If no collision is detected, return False
        return False

# Define the food class
class Food:
    # Initialize the food with a random position
    def __init__(self):
        self.x = random.randrange(0, SCREEN_WIDTH, 10)
        self.y = random.randrange(0, SCREEN_HEIGHT, 10)

    # Draw the food on the screen
    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, 10, 10])

    # Generate a new position for the food
    def generate(self):
        self.x = random.randrange(0, SCREEN_WIDTH, 10)
        self.y = random.randrange(0, SCREEN_HEIGHT, 10)

# Create a snake object and a food object
snake = Snake(300, 200)
food = Food()

# Create a clock to control the game loop
clock = pygame.time.Clock()

# Create a variable to store the game state
running = True

# Game loop
while running:
    # Handle the keyboard input
    snake.handle_input()

    # Update the snake and the food
    snake.update()

    # Check if the snake eats the food
    if snake.x == food.x and snake.y == food.y:
        # Increase the length of the snake
        snake.length += 1
        # Generate a new position for the food
        food.generate()

    # Check if the snake collides with itself or the edges of the screen
    if snake.check_collision():
        # End the game loop
        running = False

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the snake and the food on the screen
    snake.draw()
    food.draw()

    # Update the display
    pygame.display.flip()

    # Set the frame rate to 15 frames per second
    clock.tick(15)

# Quit pygame

