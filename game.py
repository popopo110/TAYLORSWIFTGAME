import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set block dimensions
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20

# Set snake speed
SNAKE_SPEED = 20

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.dx = SNAKE_SPEED
        self.dy = 0
        self.body = [Block(x, y)]

        if len(self.body) >= 3:
            self.body.pop()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, Block(self.x, self.y))

    def grow(self):
        if len(self.body) >= 3:
            self.body.pop()
        self.body.insert(0, Block(self.x, self.y))

    def draw(self, screen):
        for block in self.body:
            block.draw(screen)

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.color = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def main():
    # Initialize Pygame
    pygame.init()

    # Set font
    font = pygame.font.SysFont(None, 25)

    # Set screen dimensions
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Set caption
    pygame.display.set_caption("Snatris Game")

    # Create clock object
    clock = pygame.time.Clock()

    # Set starting position for snake
    snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set starting position for block
    block = Block(random.randrange(0, SCREEN_WIDTH - BLOCK_WIDTH), random.randrange(0, SCREEN_HEIGHT - BLOCK_HEIGHT))

    # Set score
    score = 0

    # Set thrown block
    thrown_block = None

    # Main game loop
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dx = -SNAKE_SPEED
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.dx = SNAKE_SPEED
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -SNAKE_SPEED
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = SNAKE_SPEED
                elif event.key == pygame.K_SPACE and thrown_block is None:
                    # Throw a block if the spacebar is pressed and there's no thrown block
                    thrown_block = Block(snake.x, snake.y)
                    thrown_block.color = RED

        # Move snake
        snake.move()

        # Check for collision with block
        if snake.x == block.x and snake.y == block.y:
            # If the snake collides with the block, grow the snake and move the block to a new position
            snake.grow()
            block.x = random.randrange(0, SCREEN_WIDTH - BLOCK_WIDTH)
            block.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_HEIGHT)
            score += 10

            # Check for collision with thrown block
        if thrown_block is not None:
            if snake.x == thrown_block.x and snake.y == thrown_block.y:
                # If the snake collides with the thrown block, reset the thrown block and move the snake to the position of the block
                thrown_block = None
                snake.body = [(block.x, block.y)] + snake.body
                score += 10

                # Add new block to the snake's body
                snake.grow()

            # Move the thrown block
            thrown_block.y += SNAKE_SPEED

            # Check if thrown block goes off screen
            if thrown_block.y > SCREEN_HEIGHT:
                thrown_block = None

            # Check for collision with screen edges
        if snake.x < 0 or snake.x > SCREEN_WIDTH - BLOCK_WIDTH or snake.y < 0 or snake.y > SCREEN_HEIGHT - BLOCK_HEIGHT:
            running = False

            # Check for collision with self
        for block in snake.body[1:]:
            if snake.x == block.x and snake.y == block.y:
                running = False

            # Fill screen with black
        screen.fill(BLACK)

        # Draw snake and block
        snake.draw(screen)
        block.draw(screen)

        # Draw thrown block if it exists
        if thrown_block is not None:
            thrown_block.draw(screen)

        # Draw score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, [10, 10])

        # Update screen
        pygame.display.flip()

        # Set game speed
        clock.tick(10)

        # Quit Pygame
    pygame.quit()

if __name__ == '__main__':main()