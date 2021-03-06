import pygame

from GameConstants import *
from GameObject import *

from Scene import *
from Brick import *

from Ball import *
from Pad import *

from Level import *
from HighScore import *

from PlayingGameScene import *
from GameOverScene import *
from HighScoreScene import *
from MenuScene import *

class Breakout:
    def __init__(self):
        self.__lives = GameConstants.LIVES
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)
        # self.__level.load_random()


        self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2-GameConstants.PAD_SIZE[0]/2,GameConstants.SCREEN_SIZE[1]*9/10),pygame.image.load(GameConstants.SPRITE_PAD))
        self.__balls = [Ball((GameConstants.SCREEN_SIZE[0]/2,GameConstants.SCREEN_SIZE[1]*2/3),pygame.image.load(GameConstants.SPRITE_BALL),self)]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Breakout!")

        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32) #| pygame.FULLSCREEN, 32)
        pygame.mouse.set_visible(False)

        self.__scenes = [
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self)
            ]

        self.__current_scene = GameConstants.MENU_SCENE
        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAME_OVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_NEW_GAME),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_NEXT_LEVEL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_YOU_DIE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIGH_SCORES),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_BREAKOUT),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_BALL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_MENU)
        )

        print(GameConstants.SCREEN_SIZE)


    def start(self):
        while True:
            self.__clock.tick(GameConstants.FPS)
            self.screen.fill(GameConstants.BACKGROUND_COLOR)
            current_scene = self.__scenes[self.__current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

    def change_scene(self, scene):
        self.__current_scene = scene

    def get_scene(self):
        return self.__current_scene

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score

    def increase_score(self,score):
        self.__score += score

    def get_lives(self):
        return self.__lives

    def get_balls(self):
        return self.__balls

    def add_a_ball(self,ball):
        self.__balls.append(ball)

    def refresh_balls(self):
        self.__balls =  [ball for ball in self.get_balls() if not ball.is_ball_dead()]

    def reset_balls(self):
        self.__balls = [Ball((GameConstants.SCREEN_SIZE[0]/2,GameConstants.SCREEN_SIZE[1]*2/3),pygame.image.load(GameConstants.SPRITE_BALL),self)]

    def get_pad(self):
        return self.__pad

    def play_sound(self, sound_clip):
        sound = self.__sounds[sound_clip]
        sound.stop()
        sound.play()


    def reduce_lives(self):
        self.__lives -= 1

    def reduce_lives_to_zero(self):
            self.__lives = 0

    def increase_lives(self):
        self.__lives += 1

    def reset(self):
        self.__lives = GameConstants.LIVES
        self.__score = 0
        self.__level.load(0)

Breakout().start()
