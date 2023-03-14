import pygame
import random
import time

pygame.init()

snake_speed = 15
white   = (255, 255, 255)
black   = (0, 0, 0)
red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)
light_dark = (0, 200, 0)

# Initialising pygame
pygame.init()
 
# Initialise game window
window_x = 600
window_y = 400
icon = pygame.image.load("snake.png")
pygame.display.set_caption('Python Snakie')
pygame.display.set_icon(icon)
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

snake_position = [window_x/2, window_y/2] # also the head

snake_body = [[window_x/2, window_y/2]]

#food
food_position = [random.randrange(1, (window_x//10))*10,
                random.randrange(1, (window_y//10))*10]

food_spawn = True

direction = 'right'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    font = pygame.font.SysFont('consolas', 20)
    score_dis = font.render('Score : ' + str(score), True, white)
    score_rect = score_dis.get_rect()
    game_window.blit(score_dis, score_rect)

# Game over
def game_over():
    font = pygame.font.SysFont('consolas', 50)
    game_over_dis = font.render('Score : ' + str(score), True, white)
    # create a retangular object for the text
    game_over_rect = game_over_dis.get_rect()
    # setting position of the text
    game_over_rect.midtop = (window_x/2, 3*window_y/4)
    game_window.blit(game_over_dis, game_over_rect)
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()
    #quit()


#Main function
while True:
    # key event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
    	direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
    	direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
    	direction = 'RIGHT'
    
    # now move the snake
    if direction == 'UP':
    	snake_position[1] -= 10
    if direction == 'DOWN':
    	snake_position[1] += 10
    if direction == 'LEFT':
    	snake_position[0] -= 10
    if direction == 'RIGHT':
    	snake_position[0] += 10

    # snake grow
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        score += snake_speed
        if score > snake_speed*10:
            snake_speed += 2
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_position = [random.randrange(1, (window_x//10))*10,
                        random.randrange(1, (window_y//10))*10]
    
    food_spawn = True
    game_window.fill(black)

    #draw the snake
    k = True
    for block in snake_body:
        if block != snake_position: 
            if k:
                pygame.draw.rect(game_window, green, pygame.Rect(block[0], block[1], 10, 10))
                k = False
            else:
                pygame.draw.rect(game_window, light_dark, pygame.Rect(block[0], block[1], 10, 10))
                k = True
        else:
            pygame.draw.rect(game_window, red, pygame.Rect(block[0], block[1], 10, 10))
        #pygame.draw.rect(game_window, green, pygame.rect(block[0], block[1], 10, 10))
    
    pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x:
        if snake_position[0] < 0:
            snake_position[0] = window_x
        else:
            snake_position[0] = 0
    if snake_position[1] < 0 or snake_position[1] > window_y:
        if snake_position[1] < 0:
            snake_position[1] = window_y
        else:
            snake_position[1] = 0
    #game over
    #print(snake_position, " + ", snake_body)
    for block in snake_body[1:]:
        #print(block)
        if block == snake_position:
            game_over()
    

    show_score(1, white, 'consolas', 20)
    # refresh game screen
    pygame.display.update()

    fps.tick(snake_speed)

#pygame.display.update()