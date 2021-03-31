import pygame
import Colors
from classes import Block
from classes import Ball
import random
import math
pygame.init()

#game variables
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Brick Ball")
block_size = 20
no_of_block = 75
fps = 500
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def game_loop():
    block_arr = []
    rect_arr = []
    welcome()
    #loop variables
    exit_game = False
    game_start = False
    game_over = False
    ball_thrown = False
    platform = pygame.Rect(screen_width/2 , screen_height/2+200 , 100,10)
    ball = Ball([screen_width/2+30 , screen_height/2 + 200-7] , 7 , 1.5 ,  [math.cos(math.pi/4) , math.sin(math.pi/4)])
    score = 0
    lifes = 1


    #make list of blocks
    for _ in range(no_of_block):
        temp = Block([random.randint(100,800) , random.randint(50,300) , block_size , block_size] , Colors.rand_col() , 40)
        rect_arr.append(pygame.Rect(temp.list_info[0] , temp.list_info[1] , block_size , block_size))
        block_arr.append(temp)

    #game loop
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                elif event.key == pygame.K_ESCAPE:
                    game_start = False
                    ball_thrown = False
                    platform = pygame.Rect(screen_width / 2, screen_height / 2 + 200, 100, 10)
                    ball = Ball([screen_width / 2 + 30, screen_height / 2 + 200 - 7], 7, 1.5 ,[math.cos(math.pi/4) , math.sin(math.pi/4)])

            if event.type == pygame.MOUSEBUTTONDOWN and game_start:
                ball_thrown = True


        gameWindow.fill(Colors.white)
        if game_over:
            temp_color = Colors.rand_col()
            while not exit_game:
                gameWindow.fill(temp_color)
                text_screen("press x to restart", Colors.black, 350, 300)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            game_loop()
        pygame.draw.rect(gameWindow , Colors.black , platform) #draw platform
        tr = pygame.draw.circle(gameWindow , Colors.black ,ball.center , ball.radius) #draw circle
        for i in range(len(block_arr)):
            if block_arr[i].color == (0,0,0):
                if(random.randint(1,5) == 1):
                    temp = Block([random.randint(100, 800), random.randint(50, 300), block_size, block_size],Colors.rand_col(), 40)
                    rect_arr[i] = pygame.Rect(temp.list_info[0] , temp.list_info[1] , block_size , block_size)
                    block_arr[i] = temp
            else:
                pygame.draw.rect(gameWindow, block_arr[i].color, block_arr[i].list_info)
        text_screen(f"Score {score}", Colors.red, 330, 525)
        text_screen(f"Lifes {lifes}", Colors.red, 530, 525)

        pygame.display.update()

        #move platform
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if game_start == True:
            try:
                platform.left = platform.left + 8*(x-platform.left)/((x-platform.left)*(x-platform.left) + (y-platform.top)*(y-platform.top) )**0.5
            except:
                pass
        
        #move ball
        if ball_thrown == False:
            ball.center = [platform.left+platform.width/2 , platform.top-7]
        else:
            temp_x = ball.center[0]
            temp_y = ball.center[1]
            ball.center = [temp_x + ball.direction[0]*ball.magnitude , temp_y - ball.direction[1]*ball.magnitude]
            if (ball.center[0] >= 893 and ball.direction[0] >0) or (ball.center[0] <= 0 and ball.direction[0]<0):
                ball.direction[0] = -1*ball.direction[0]
            if  ball.center[1] <= 0:
                if (ball.center[0] >= 893 and ball.direction[0] >0) or (ball.center[0] <= 0 and ball.direction[0]<0):
                    ball.direction = [math.cos(math.pi/4) , math.sin(math.pi/4)]
                else:
                    ball.direction[1] = -1*ball.direction[1]
            if pygame.Rect.colliderect(tr , platform) and ball.direction[1] <0:
                ball.direction[1] = -1*ball.direction[1]
            if ball.direction[0] == 0:
                ball.direction[0]= 1.5
            if ball.direction[1] == 0:
                ball.direction = 1.5

        #collision with block
        for i in range(no_of_block):
            if pygame.Rect.colliderect(tr , rect_arr[i]) and block_arr[i].color != (0,0,0):
                if abs(tr.left - rect_arr[i].right) <= 3:
                    ball.direction[0] = -1*ball.direction[0]
                elif abs(tr.right - rect_arr[i].left) <= 3:
                    ball.direction[0] = -1*ball.direction[0]
                elif abs(tr.top - rect_arr[i].bottom) <= 3:
                    ball.direction[1] = -1*ball.direction[1]
                elif abs(tr.bottom - rect_arr[i].top) <= 3:
                    ball.direction[1] = -1*ball.direction[1]
                temp0 = block_arr[i].color[0]
                temp1 = block_arr[i].color[1]
                temp2 = block_arr[i].color[2]
                block_arr[i].color = (int(temp0/1.2) , int(temp1/1.2) , int(temp2/1.2))
                if(random.randint(1,20) == 1):
                    score+=1

        #ball falls down
        if ball.center[1]>= 600:
            game_start = False
            ball_thrown = False
            lifes-=1
            if lifes == 0:
                game_over = True
            platform = pygame.Rect(screen_width / 2, screen_height / 2 + 200, 100, 10)
            ball = Ball([screen_width / 2 + 30, screen_height / 2 + 200 - 7], 7, 1.5,[math.cos(math.pi / 4), math.sin(math.pi / 4)])
        clock.tick(fps)


def welcome():
    exit_game = False
    temp_color = Colors.rand_col()
    while not exit_game:
        gameWindow.fill(temp_color)
        text_screen("Press space to start" , Colors.black , 350 , 300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 0

def you_lost():
    exit_game = False
    temp_color = Colors.rand_col()
    while not exit_game:
        gameWindow.fill(temp_color)
        text_screen("press x to restart" , Colors.black , 350 , 300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_loop()
game_loop()