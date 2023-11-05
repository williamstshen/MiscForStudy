import pygame, sys, random, time
from enum import Enum 

check_errors = pygame.init()

# sington : global used const parameter
class Direct(Enum):
    # Order by clockwise
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

class PARAM:
    WIN_X = 640
    WIN_Y = 480
    HEADER_Y = int(WIN_Y/8)
    GRID = 10
    INIT_FPS = 10
    MAX_X = int(WIN_X/GRID)
    MAX_Y = int(WIN_Y/GRID)
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

#####
##### game main Class include UI
#####
class snakeGame:
    def __init__(self):
        
        ## ===== specify for UI related
        # single parameter with tuple
        self.playUI = pygame.display.set_mode((PARAM.WIN_X, PARAM.WIN_Y))
        pygame.display.set_caption('Test for Snake Game!')
        # FPS 
        self.fps = PARAM.INIT_FPS
        self.clockUI = pygame.time.Clock()
        ## =====
        
        ## ===== specify for object contents 
        # snake shape
        # snakeBody format : head , body, body, ..., tail
        # 231105: remove Pos and use "snakeBody" only
        init_pos = [int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)]
        
        self.snakeBody = [init_pos, 
                          [init_pos[0] - PARAM.GRID*1, init_pos[1]],
                          [init_pos[0] - PARAM.GRID*2, init_pos[1]] 
                         ]
        self.foodPos = self.place_food()
        self.snakeDirect = Direct.RIGHT
        self.score = 0

        self.gameOver = False
        self.gameRun = False
        ## =====
        
        # 231105: move to update_ui
        #pygame.display.flip()
        #self.fpsCtrl.tick(PARAM.FPS)

    def reset(self):
        init_pos = [int(PARAM.WIN_X/2), int(PARAM.WIN_Y/2)]
        self.snakeBody = [init_pos, 
                          [init_pos[0] - PARAM.GRID*1, init_pos[1]],
                          [init_pos[0] - PARAM.GRID*2, init_pos[1]] 
                         ]
        
        self.foodPos = self.place_food()
        self.snakeDirect = Direct.RIGHT
        self.score = 0
        self.fps = PARAM.INIT_FPS

        self.gameOver = False
        self.gameRun = False

    def place_food(self):
        isGenerated = False
        gen_foodPos = []
        # Loop to make sure food not generate on snake's body
        while not isGenerated:
            gen_foodPos = [int(random.randrange(1, PARAM.MAX_X)*PARAM.GRID),
                           int(random.randrange(1, PARAM.MAX_Y)*PARAM.GRID)]
            isGenerated = True
            if gen_foodPos in self.snakeBody:
                isGenerated = False
        return gen_foodPos

    def update_ui(self):
        self.playUI.fill(PARAM.BLACK_COLOR)
        myFont = pygame.font.SysFont('monaco', 20)
        if self.gameOver:
            headerSurface = myFont.render(f'Game Over. GG!', True, PARAM.RED_COLOR)
            headerRect = headerSurface.get_rect()
            headerRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+60))
            self.playUI.blit(headerSurface, headerRect)
        elif not self.gameRun:
            headerSurface = myFont.render(f'Welcome snake Game!', True, PARAM.WHITE_COLOR)
            headerRect = headerSurface.get_rect()
            headerRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+60))
            self.playUI.blit(headerSurface, headerRect)
        
        cur_level = int((self.fps - PARAM.INIT_FPS)/2)
        scSurface = myFont.render(f'Score = {self.score} L{cur_level}', True, PARAM.WHITE_COLOR)
        scRect = scSurface.get_rect()
        if self.gameOver | (not self.gameRun):
            # put score at middle of screen
            scRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y + 80))
        else:
            scRect.midtop = (PARAM.WIN_X/8, PARAM.HEADER_Y/2)

        self.playUI.blit(scSurface, scRect)
        
        if self.gameOver | (not self.gameRun):
            hintSurface = myFont.render(f'Press Enter to start', True, PARAM.WHITE_COLOR)
            hintRect = hintSurface.get_rect()
            hintRect.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+100))
            self.playUI.blit(hintSurface, hintRect)

            hintSurface2 = myFont.render(f'Press ESC to exit game', True, PARAM.WHITE_COLOR)
            hintRect2 = hintSurface2.get_rect()
            hintRect2.midtop = (PARAM.WIN_X/2, (PARAM.HEADER_Y+120))
            self.playUI.blit(hintSurface2, hintRect2)
        
        ## Draw snake and food when in game 
        if (not self.gameOver) & self.gameRun:
            # snake
            for pos in self.snakeBody:
                pygame.draw.rect(self.playUI,
                                 PARAM.CYAN_COLOR,
                                 pygame.Rect(pos[0], pos[1], 
                                             PARAM.GRID, PARAM.GRID)
                                )
            # food
            pygame.draw.rect(self.playUI,
                             PARAM.BROWN_COLOR,
                             pygame.Rect(self.foodPos[0], self.foodPos[1], 
                                         PARAM.GRID, PARAM.GRID))
        pygame.display.flip()
        self.clockUI.tick(self.fps)
        
    def update_snake_food_human(self, in_direct):
        # update object content by input operation (in Enum Direct)
        all_direct = [v for v in Direct]
        if in_direct in all_direct:
            # filter out opposite (effectiveless) operation
            nxt_direct_turn_left = (self.snakeDirect.value - 1) % len(all_direct)
            nxt_direct_turn_right = (self.snakeDirect.value + 1) % len(all_direct)
            if (in_direct.value == nxt_direct_turn_left) | (in_direct.value == nxt_direct_turn_right):
                self.snakeDirect = in_direct

        snakeHead = [self.snakeBody[0][0], self.snakeBody[0][1]]
        if self.snakeDirect == Direct.RIGHT:
            snakeHead[0] += PARAM.GRID
        if self.snakeDirect == Direct.LEFT:
            snakeHead[0] -= PARAM.GRID
        if self.snakeDirect == Direct.UP:
            snakeHead[1] -= PARAM.GRID
        if self.snakeDirect == Direct.DOWN:
            snakeHead[1] += PARAM.GRID

        self.snakeBody.insert(0, list(snakeHead))
        if self.foodPos in self.snakeBody:
            # food eaten : snake developed and replace new food
            self.foodPos = self.place_food()
            self.score += 1
            # score every 10 to level-up FPS by 2
            self.fps = int(2*(int(self.score/10))) + PARAM.INIT_FPS
        else :
            self.snakeBody.pop()

    def is_collision(self):
        result = False
        snakeHead = self.snakeBody[0]
        if snakeHead in self.snakeBody[1:]:
            result = True
        if (snakeHead[0] > PARAM.WIN_X) | (snakeHead[0] < 0):
            result = True 
        if (snakeHead[1] > PARAM.WIN_Y) | (snakeHead[1] < 0):
            result = True
        return result

#####
##### Reinforcement Learning related model and tran definition
##### 



#####
##### Common Function between object in main 
#####

def trans_key_event_to_direct(event):
    result = None
    if (event.key == pygame.K_RIGHT) | (event.key == ord('d')):
        result = Direct.RIGHT
    if (event.key == pygame.K_LEFT) | (event.key == ord('a')):
        result = Direct.LEFT
    if (event.key == pygame.K_UP) | (event.key == ord('w')):
        result = Direct.UP
    if (event.key == pygame.K_DOWN) | (event.key == ord('s')):
        result = Direct.DOWN
    return result

if __name__ == "__main__":
    p_game = snakeGame()
    is_exit_game = False
    is_game_over = False
    highest_score = 0
    cur_direct = None

    while not is_exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Close Window Pressed and exit by force")
                is_exit_game = True
            elif event.type == pygame.KEYDOWN:
                if is_game_over :
                    if p_game.score > highest_score:
                        highest_score = p_game.score
                    if event.key==pygame.K_RETURN:
                        is_game_over = False
                        p_game.reset()
                        p_game.gameRun = True
                    elif event.key==pygame.K_ESCAPE:
                        is_exit_game = True
                else:
                    if event.key==pygame.K_RETURN:
                        p_game.gameRun = True
                    new_direct = trans_key_event_to_direct(event)
                    if new_direct is not None:
                        cur_direct = new_direct

        if (not is_game_over) & (not is_exit_game) & p_game.gameRun:
            p_game.update_snake_food_human(cur_direct)
            is_game_over = p_game.is_collision()
            p_game.gameOver = is_game_over
            p_game.gameRun = not is_game_over

        p_game.update_ui()

    #exit pygame
    pygame.quit()
    print(f"Exit Game with Highest Score={highest_score}")
    #exit program
    sys.exit()
