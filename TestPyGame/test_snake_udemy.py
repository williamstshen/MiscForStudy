import pygame, sys, random, time

check_errors = pygame.init()

# sington : global used const parameter
class PARAM:
    WIN_X = 960
    WIN_Y = 720
    HEADER_Y = int(WIN_Y/8)
    GRID = 10
    MAX_X = int(WIN_X/GRID)
    MAX_Y = int(WIN_Y/GRID)

# specify window size (main user surface)
# single parameter with tuple
playSurface = pygame.display.set_mode((PARAM.WIN_X, PARAM.WIN_Y))
pygame.display.set_caption('Test for Snake Game!')

# Colors 
# red: GameOver text
# cyan: snake
# black: background
# white: score text
# brown: food
red_color = pygame.Color(199, 0, 0)
cyan_color = pygame.Color(0, 250, 250)
black_color = pygame.Color(0, 0, 0)
white_color = pygame.Color(255, 255, 255)
brown_color = pygame.Color(165, 42, 42)

# FPS 
fpsCtrl = pygame.time.Clock()

# snake shape
# snakeBody format : head , body, body, ..., tail
snakePos = [int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)]
snakeBody = [[int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)], 
             [int(PARAM.WIN_X/2) - PARAM.GRID*1, snakePos[1]],
             [int(PARAM.WIN_X/2) - PARAM.GRID*2, snakePos[1]]
            ]


# Food generation : avoid hitting snake
foodSpawn = False

def generateFood(snakeBody):
    isGenerate = False
    foodPos = []
    while isGenerate == False:
        foodPos = [int(random.randrange(1, PARAM.MAX_X)*PARAM.GRID),
                   int(random.randrange(1, PARAM.MAX_Y)*PARAM.GRID)]
        isGenerate = True
        for snake_body_p in snakeBody:
            if snake_body_p == foodPos:
                isGenerate = False
    return foodPos

foodPos = generateFood(snakeBody)
print(foodPos)
snakeDirect = "RIGHT"
snakeChgTo = snakeDirect


# game over func : display text only
def gameOver():
    myFont = pygame.font.SysFont('monaco', 48)
    gameOverSurface = myFont.render('GG!', True, red_color)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (PARAM.WIN_X/2, PARAM.HEADER_Y)
    playSurface.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    fpsCtrl.tick(2)
    print("Game will close within 30 seconds")
    time.sleep(30)
    #exit pygame window
    pygame.quit()
    #exit program
    sys.exit()

def showScore(score, choice=1):
    myFont = pygame.font.SysFont('monaco', 20)
    scSurface = myFont.render(f'Score = {score}', True, white_color)
    scRect = scSurface.get_rect()
    if choice == 1:
        scRect.midtop = (PARAM.WIN_X/8, PARAM.HEADER_Y/2)
    else:
        scRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y + 80))
    playSurface.blit(scSurface, scRect)
    #pygame.display.flip()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("CloseWindow Pressed and exit by force")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT) | (event.key == ord('d')):
                snakeChgTo = "RIGHT"
            if (event.key == pygame.K_LEFT) | (event.key == ord('a')):
                snakeChgTo = "LEFT"
            if (event.key == pygame.K_UP) | (event.key == ord('w')):
                snakeChgTo = "UP"
            if (event.key == pygame.K_DOWN) | (event.key == ord('s')):
                snakeChgTo = "DOWN"
            if event.key == pygame.K_ESCAPE:
                print("ESC Pressed and exit by force")
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validate direction : avoid opposite cases
    if (snakeChgTo == "RIGHT") & (snakeDirect != "LEFT"):
        snakeDirect = snakeChgTo
    elif (snakeChgTo == "LEFT") & (snakeDirect != "RIGHT"):
        snakeDirect = snakeChgTo
    elif (snakeChgTo == "UP") & (snakeDirect != "DOWN"):
        snakeDirect = snakeChgTo
    elif (snakeChgTo == "DOWN") & (snakeDirect != "UP"):
        snakeDirect = snakeChgTo

    if snakeDirect == "RIGHT":
        snakePos[0] += 10
    if snakeDirect == "LEFT":
        snakePos[0] -= 10
    if snakeDirect == "UP":
        snakePos[1] -= 10
    if snakeDirect == "DOWN":
        snakePos[1] += 10
    
    snakePos[0] = snakePos[0] % PARAM.WIN_X
    snakePos[1] = snakePos[1] % PARAM.WIN_Y
    for pos_body in snakeBody:
        if pos_body == snakePos:
            print(snakeBody)
            print(snakePos)
            showScore(score, 2)
            gameOver()

    snakeBody.insert(0, list(snakePos))

    # snake body mechanism
    if snakePos == foodPos:
        foodSpawn = False
        print("Eat Food")
        #print(snakeBody)
        score += 1
    else:
        snakeBody.pop()
    
    #print(snakeBody)

    # regenerate food if eaten by snake 
    if foodSpawn == False:
        foodPos = generateFood(snakeBody)
        foodSpawn = True
    
    ### Draw GUI
    # fill entire window
    playSurface.fill(black_color)
    # draw snake body
    for pos in snakeBody:
        pygame.draw.rect(playSurface,
                         cyan_color,
                         pygame.Rect(pos[0], pos[1], 10, 10)
                         )
    pygame.draw.rect(playSurface,
                     brown_color,
                     pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    showScore(score)
    pygame.display.flip()
    fpsCtrl.tick(10)

    

#gameOver()

# debug : stop window disappearing
# time.sleep(20)

