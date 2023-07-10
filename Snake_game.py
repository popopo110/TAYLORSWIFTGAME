import pygame
import random
import math

# initialize Pygame
pygame.init()

# set up window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# set up clock
clock = pygame.time.Clock()

# set up font
font = pygame.font.SysFont(None, 25)

# set up starting position and direction for snake
x = 250
y = 250
size = 10
vel = 10
direction = "right"

# set up starting position for tetris cube
cube_x = random.randint(0, width - size)
cube_y = -10

# set up snake body
body = []
body_length = 3

# set up score
score = 0

# set up timer for tetris cube and asteroid drops
cube_timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(cube_timer_event, 4000)



# create function to draw snake, tetris cube, and asteroid
def draw_snake_cube_and_asteroid():
    # clear screen
    window.fill(white)

    # draw snake body
    for part in body:
        pygame.draw.rect(window, black, [part[0], part[1], size, size])

    # draw tetris cube
    pygame.draw.rect(window, red, [cube_x, cube_y, size, size])

# create game loop
run = True
while run:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
        elif event.type == cube_timer_event:
            cube_x = random.randint(0, width - size)
            cube_y = -10

    # move snake
    if direction == "up":
        y -= vel
    elif direction == "down":
        y += vel
    elif direction == "left":
        x -= vel
    elif direction == "right":
        x += vel

    # check for collision with tetris cube
    if cube_y + size > y and cube_x < x + size and cube_x + size > x:
        score += 1
        body_length += 1
        cube_x = random.randint(0, width - size)
        cube_y = -10

    # check for collision with asteroid
    if asteroid_y + size > y and asteroid_x < x + size and asteroid_x + size > x:
        run = False

    # check for collision with walls
    if x < 0 or x > width - size or y < 0 or y > height - size:
        run = False

    # update snake body
    body.insert(0, (x, y))
    if len(body) > body_length:
        body.pop()

    # draw everything
    draw_snake_cube_and_asteroid()

    # display score
    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (10, 10))

    # update display and tick clock
    pygame.display.update()
    clock.tick(30)

# quit Pygame
pygame.quit()
