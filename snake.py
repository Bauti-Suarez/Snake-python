# snakegame
import pygame, time, random
from pygame import font
#init
pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (210, 50, 80)
gray = (128, 128, 128)

#dim
dis_width = 500
dis_height = 500
#setDim
dis = pygame.display.set_mode((dis_height, dis_width))
pygame.display.set_caption("SnakeGame by Bauti")
#initClock
clock = pygame.time.Clock()
#dimSnake
snake_block = 10
#frame
snake_speed = 15
#font
font_style = pygame.font.SysFont("bahnschrift", 25)
font_score = pygame.font.SysFont("comicsansms", 35)

#score
def you_score(score):
    value = font_score.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

#bodySnake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

#Message game
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#game
def gameLoop():
    #cond
    game_over = False
    game_close = False
    #spaw
    x1 = dis_width / 2
    y1 = dis_height / 2
    #change
    x1_change = 0
    y1_change = 0
    #bodysnake
    snake_list = []
    length_of_snake = 1
    #random food
    foodX = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foodY = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    #buclegame
    while not game_over:
        #control
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q_Quit or C", red)
            you_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #keys and for
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        #gameover
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #changecontrol
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        #foodPosi
        pygame.draw.rect(dis, gray, [foodX, foodY, snake_block, snake_block])
        #snakeBody
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        our_snake(snake_block, snake_list)
        you_score(length_of_snake - 1)

        pygame.display.update()
        #snakebody
        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodY = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
