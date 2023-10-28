import pygame, sys, random, time

check_errors = pygame.init()

# sington : global used const parameter
class PARAM:
    WIN_X = 640
    WIN_Y = 480
    HEADER_Y = int(WIN_Y/8)
    GRID = 10
    MAX_X = int(WIN_X/GRID)
    MAX_Y = int(WIN_Y/GRID)
    FPS = 10
    # Colors 
    # red: GameOver text
    # cyan: snake
    # black: background
    # white: score text
    # brown: food
    RED_COLOR = pygame.Color(188, 0, 0)
    CYAN_COLOR = pygame.Color(0, 250, 250)
    BLACK_COLOR = pygame.Color(0, 10, 0)
    WHITE_COLOR = pygame.Color(255, 255, 255)
    BROWN_COLOR = pygame.Color(165, 42, 42)

class snakeGame:
    def __init__(self):
        # specify window size (main user surface)
        # single parameter with tuple
        self.playSurface = pygame.display.set_mode((PARAM.WIN_X, PARAM.WIN_Y))
        pygame.display.set_caption('Test for Snake Game!')
        # FPS 
        self.fpsCtrl = pygame.time.Clock()

        # snake shape
        # snakeBody format : head , body, body, ..., tail
        self.snakePos = [int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)]
        self.snakeBody = [[int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)], 
                          [int(PARAM.WIN_X/2) - PARAM.GRID*1, self.snakePos[1]],
                          [int(PARAM.WIN_X/2) - PARAM.GRID*2, self.snakePos[1]]
                         ]
        self.foodPos = self.generate_food()
        self.snakeDirect = "RIGHT"
        self.snakeChgTo = self.snakeDirect
        self.score = 0
        
        # Food generation : avoid hitting snake
        #self.foodSpawn = False

        pygame.display.flip()
        self.fpsCtrl.tick(PARAM.FPS)

    def reset(self):
        self.snakePos = [int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)]
        self.snakeBody = [[int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)], 
                          [int(PARAM.WIN_X/2) - PARAM.GRID*1, self.snakePos[1]],
                          [int(PARAM.WIN_X/2) - PARAM.GRID*2, self.snakePos[1]]
                         ]
        self.foodPos = self.generate_food()
        self.snakeDirect = "RIGHT"
        self.snakeChgTo = self.snakeDirect
        self.score = 0

    def generate_food(self):
        isGenerated = False
        gen_foodPos = []
        # Loop to make sure food not generate on snake's body
        while isGenerated == False:
            gen_foodPos = [int(random.randrange(1, PARAM.MAX_X)*PARAM.GRID),
                           int(random.randrange(1, PARAM.MAX_Y)*PARAM.GRID)]
            isGenerated = True
            for snake_body_p in self.snakeBody:
                if snake_body_p == gen_foodPos:
                    isGenerated = False
        return gen_foodPos

    def show_score(self, choice="play"):
        myFont = pygame.font.SysFont('monaco', 20)
        if choice == "finish":
            hintSurface = myFont.render(f'GG!', True, PARAM.RED_COLOR)
            hintRect = hintSurface.get_rect()
            hintRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+60))
            self.playSurface.blit(hintSurface, hintRect)

        scSurface = myFont.render(f'Score = {self.score}', True, PARAM.WHITE_COLOR)
        scRect = scSurface.get_rect()
        if choice == "play":
            scRect.midtop = (PARAM.WIN_X/8, PARAM.HEADER_Y/2)
        elif (choice == "finish") | (choice == "init"):
            scRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y + 80))
        self.playSurface.blit(scSurface, scRect)
        
        if choice != "play":
            hintSurface = myFont.render(f'Press Enter to start', True, PARAM.WHITE_COLOR)
            hintRect = hintSurface.get_rect()
            hintRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+100))
            self.playSurface.blit(hintSurface, hintRect)

            hintSurface2 = myFont.render(f'Press ESC to exit game', True, PARAM.WHITE_COLOR)
            hintRect2 = hintSurface2.get_rect()
            hintRect2.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+120))
            self.playSurface.blit(hintSurface2, hintRect2)
        
    def update_direction_by_keyin(self, event):
        if (event.key == pygame.K_RIGHT) | (event.key == ord('d')):
            self.snakeChgTo = "RIGHT"
        if (event.key == pygame.K_LEFT) | (event.key == ord('a')):
            self.snakeChgTo = "LEFT"
        if (event.key == pygame.K_UP) | (event.key == ord('w')):
            self.snakeChgTo = "UP"
        if (event.key == pygame.K_DOWN) | (event.key == ord('s')):
            self.snakeChgTo = "DOWN"

        if (self.snakeChgTo == "RIGHT") & (self.snakeDirect != "LEFT"):
            self.snakeDirect = self.snakeChgTo
        elif (self.snakeChgTo == "LEFT") & (self.snakeDirect != "RIGHT"):
            self.snakeDirect = self.snakeChgTo
        elif (self.snakeChgTo == "UP") & (self.snakeDirect != "DOWN"):
            self.snakeDirect = self.snakeChgTo
        elif (self.snakeChgTo == "DOWN") & (self.snakeDirect != "UP"):
            self.snakeDirect = self.snakeChgTo

    def check_snake_body(self):
        if self.snakeDirect == "RIGHT":
            self.snakePos[0] += PARAM.GRID
        if self.snakeDirect == "LEFT":
            self.snakePos[0] -= PARAM.GRID
        if self.snakeDirect == "UP":
            self.snakePos[1] -= PARAM.GRID
        if self.snakeDirect == "DOWN":
            self.snakePos[1] += PARAM.GRID
        
        is_game_over = False
        for pos_body in self.snakeBody:
            if pos_body == self.snakePos:
                is_game_over = True
                break
                
        if (self.snakePos[0] > PARAM.WIN_X) | (self.snakePos[0] < 0):
            is_game_over = True 
        if (self.snakePos[1] > PARAM.WIN_Y) | (self.snakePos[1] < 0):
            is_game_over = True 
        

        self.snakeBody.insert(0, list(self.snakePos))
        if self.snakePos == self.foodPos:
            #self.foodSpawn = False
            self.score += 1

            self.foodPos = self.generate_food()
            #self.foodSpawn = True
        else:
            self.snakeBody.pop()
        
        return is_game_over
    
    def update_play_gui(self):
        self.playSurface.fill(PARAM.BLACK_COLOR)
        for pos in self.snakeBody:
            #snake
            pygame.draw.rect(self.playSurface,
                             PARAM.CYAN_COLOR,
                             pygame.Rect(pos[0], pos[1], 10, 10)
                            )
        #food
        pygame.draw.rect(self.playSurface,
                         PARAM.BROWN_COLOR,
                         pygame.Rect(self.foodPos[0], self.foodPos[1], 10, 10))
        self.show_score("play")
        pygame.display.flip()
        self.fpsCtrl.tick(PARAM.FPS)            

if __name__ == "__main__":
    p_game = snakeGame()
    is_game_over = True
    is_exit_game = False
    current_stat = "init"
    while not is_exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Close Window Pressed and exit by force")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    is_game_over = False
                    p_game.reset()

                if not is_game_over:
                    p_game.update_direction_by_keyin(event)
                elif event.key == pygame.K_ESCAPE:
                    # double ESC to really exit game
                    is_exit_game = True

                if (not is_exit_game) & (event.key == pygame.K_ESCAPE):
                    print("ESC Pressed and finish Game")
                    #p_game.show_score("finish")
                    #p_game.game_over()
                    is_game_over = True
                    #pygame.event.post(pygame.event.Event(pygame.QUIT))
        if (not is_exit_game) & (not is_game_over):
            is_game_over = p_game.check_snake_body()
            if is_game_over:
                current_stat = "finish"
        
        if is_game_over:
            #print("Game Over")
            p_game.show_score(current_stat)
            pygame.display.flip()
            p_game.fpsCtrl.tick(2)
        else:
            p_game.update_play_gui()

    #exit pygame
    pygame.quit()
    print("Exit by double-pressing ESC")
    #exit program
    sys.exit()
