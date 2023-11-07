import pygame, sys, random, time
from enum import Enum 
from collections import deque

import random
import numpy as np
import tensorflow as tf


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

    N_GAME_CREATE = 100
    MAX_MEMORY = 100000

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

    def is_collision(self, snakeHead):
        result = False
        #snakeHead = self.snakeBody[0]
        if snakeHead in self.snakeBody[1:]:
            result = True
        if (snakeHead[0] > PARAM.WIN_X) | (snakeHead[0] < 0):
            result = True 
        if (snakeHead[1] > PARAM.WIN_Y) | (snakeHead[1] < 0):
            result = True
        return result

#####
##### Reinforcement Learning related model and tran definition
##### instead of Youtube RL with torch for snake, here to try using Keras
##### 
class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = PARAM.N_GAME_CREATE
        self.model = Linear_QNet()
        self.trainer = QTrainer()
        self.memory = deque(maxlen=PARAM.MAX_MEMORY)

    
    def get_state(self, p_snake_game):
        # to return state value as below
        # [danger_straight, danger_turn_right, danger_turn_left,
        #  direct_right, direct_down, direct_left, direct_up,
        #  food_right, food_down, food_left, food_up]
        # danger_* is multi-value
        # direct_* is one-hot
        # food* is multi-value (1 or 2 values)

        head = p_snake_game.snakeBody[0]
        food = p_snake_game.foodPos
        # init value
        danger_straight, danger_turn_r, danger_turn_l = (0, 0, 0)
        direct_r, direct_d, direct_l, direct_u = (0, 0, 0, 0)
        food_r, food_d, food_l, food_u = (0, 0, 0, 0)
        
        direct_r = 1 if (p_snake_game.snakeDirect == Direct.RIGHT) else 0
        direct_d = 1 if (p_snake_game.snakeDirect == Direct.DOWN) else 0
        direct_l = 1 if (p_snake_game.snakeDirect == Direct.LEFT) else 0
        direct_u = 1 if (p_snake_game.snakeDirect == Direct.UP) else 0

        straight_head = [head[0] + direct_r*PARAM.GRID - direct_l*PARAM.GRID, 
                         head[1] + direct_d*PARAM.GRID - direct_u*PARAM.GRID] 
        danger_straight = p_snake_game.is_collision(straight_head)
        
        # up->right or down->left for x
        # right->down or left->up for y
        turn_right_head = [head[0] + direct_u*PARAM.GRID - direct_d*PARAM.GRID, 
                           head[1] + direct_r*PARAM.GRID - direct_l*PARAM.GRID] 
        danger_turn_r = p_snake_game.is_collision(turn_right_head)

        # up->left or down->right for x
        # right->up or left->down for y
        turn_left_head = [head[0] + direct_d*PARAM.GRID - direct_u*PARAM.GRID, 
                          head[1] + direct_l*PARAM.GRID - direct_r*PARAM.GRID] 
        danger_turn_l = p_snake_game.is_collision(turn_left_head)

        food_r = 1 if ((head[0] - food[0]) < 0) else 0
        food_l = 1 if ((head[0] - food[0]) >= 0) else 0
        food_d = 1 if ((head[1] - food[1]) < 0) else 0
        food_u = 1 if ((head[1] - food[1]) >= 0) else 0

        return [danger_straight, danger_turn_r, danger_turn_l,
                direct_r, direct_d, direct_l, direct_u,
                food_r, food_d, food_l, food_u]
    
    def get_action(self, agi_state):
        # based on state gotten from Agent.get_state
        # return values (one-hot) = [is_straight, turn_right, turn_left]
        result = [0, 0, 0]
        
        # before running N training games, use random action
        self.epsilon = PARAM.N_GAME_CREATE - self.n_games
        if random.randint(0, PARAM.N_GAME_CREATE*3) < self.epsilon:
            move_idx = random.randint(0, len(result))
            result[move_idx] = 1
        else:
            # Main Reinforcement-Learning Part
            # torch tensor -> tf tensor 
            ts_state = tf.Tensor(agi_state, shape=(1, 11), dtype=tf.float16)
            prediction = self.model(ts_state)
            move_idx = tf.keras.argmax(prediction).item()
            result[move_idx] = 1
        return result
    
    def save_data(self, state_prev, agi_move, state_next, reward, is_game_over):
        self.memory.append((state_prev, agi_move, state_next, reward, is_game_over))

    def train_short_memory(self, state_prev, agi_move, state_next, reward, is_game_over):
        self.trainer.train_step(state_prev, agi_move, state_next, reward, is_game_over)
        pass
    def train_long_memory():
        pass


class Linear_QNet(tf.Module):
    def __init__(self):
        super().__init__()

class QTrainer:
    def __init__(self, model):
        self.lr = 0.001
        self.model = model
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.lr)

    def train_step(self, state_prev, agi_move, state_next, reward, is_game_over):
        state_prev_tf = tf.Tensor(state_prev, dtype=tf.float16)
        state_next_tf = tf.Tensor(state_prev, dtype=tf.float16)
        agi_move_tf = tf.Tensor(state_prev, dtype=tf.int16)
        reward_prev_tf = tf.Tensor(state_prev, dtype=tf.float16)
        is_game_over_local = is_game_over
        if len(state_prev) <= 1:
            # translate to (1, x)
            # tf.exapnded_dims = torch.unsqueeze
            state_prev_tf = tf.expand_dims(state_prev_tf, axis=0)
            state_next_tf = tf.expand_dims(state_next_tf, axis=0)
            agi_move_tf = tf.expand_dims(agi_move_tf, axis=0)
            reward_prev_tf = tf.expand_dims(reward_prev_tf, axis=0)
            is_game_over_local = (is_game_over_local, )
        
        pred = self.model(state_prev_tf)
        target = pred.clone()
        ##TODO: belows are pytorch, need to realize and translate to tensorflow basic
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()
        



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

def trans_agi_move_to_direct(p_game, agi_move):
    #[straight, turn right, turn left]
    all_direct = [v for v in Direct]
    nxt_direct_turn_left = (p_game.snakeDirect.value - 1) % len(all_direct)
    nxt_direct_turn_right = (p_game.snakeDirect.value + 1) % len(all_direct)

    if agi_move[1] == 1:
        # turn right : v + 1
        return all_direct[nxt_direct_turn_right]
    elif agi_move[2] == 1:
        # turn left : v - 1
        return all_direct[nxt_direct_turn_left]
    return p_game.snakeDirect


    if (event.key == pygame.K_RIGHT) | (event.key == ord('d')):
        result = Direct.RIGHT
    if (event.key == pygame.K_LEFT) | (event.key == ord('a')):
        result = Direct.LEFT
    if (event.key == pygame.K_UP) | (event.key == ord('w')):
        result = Direct.UP
    if (event.key == pygame.K_DOWN) | (event.key == ord('s')):
        result = Direct.DOWN
    return result

def agent_train():
    p_agent = Agent()
    p_game = snakeGame()
    is_game_over = 0
    is_exit_game = False
    highest_score = 0
    score_all = []
    prev_score = 0
    reward = 0

    while not is_exit_game:
        state_prev = p_agent.get_state(p_game)
        agi_move = p_agent.get_action(state_prev)
        p_game.update_snake_food_human(trans_agi_move_to_direct(agi_move))
        is_game_over = 1 if p_game.is_collision(p_game.snakeBody[0]) else 0
        cur_score = p_game.score
        if is_game_over == 1:
            reward = -10
        elif cur_score > prev_score:
            reward = 10
            prev_score = cur_score
        else:
            reward = 0
        state_new = p_agent.get_state(p_game)
        
        # middle train with state/action between steps
        p_agent.train_short_memory()

        p_agent.save_data(state_prev, agi_move, reward, state_new, is_game_over)

        if is_game_over == 1:
            p_game.reset()
            p_agent.n_games += 1
            # train again with random pick existed database 
            # for next games
            p_agent.train_long_memory()
            if cur_score > highest_score:
                highest_score = cur_score
                p_agent.model.save()
            score_all.append(cur_score)
            p_game.gameRun = True
            p_game.gameOver = False
            prev_score = 0
            







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
            is_game_over = p_game.is_collision(p_game.snakeBody[0])
            p_game.gameOver = is_game_over
            p_game.gameRun = not is_game_over

        p_game.update_ui()

    #exit pygame
    pygame.quit()
    print(f"Exit Game with Highest Score={highest_score}")
    #exit program
    sys.exit()
