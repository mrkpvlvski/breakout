import pygame
from Scene import *
from GameConstants import *
from HighScore import *

class GameOverScene(Scene):

    def __init__(self,game):
        super(GameOverScene,self).__init__(game)
        self.__player_name = ""

    def render(self):
        game = self.get_game()
        self.clear_text()
        self.add_text("Your Name: {}".format(self.__player_name),400,400, size = 30)
        super(GameOverScene,self).render()

    def handle_events(self, events):
        super(GameOverScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()
        game = self.get_game()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_RETURN:
                    HighScore().add(self.__player_name,game.get_score())
                    game.reset()
                    game.play_sound(GameConstants.SOUND_HIGH_SCORES)
                    game.change_scene(GameConstants.HIGHSCORE_SCENE)
                elif event.key >= 65 and event.key <= 122 and len(self.__player_name) < GameConstants.HIGHSCORE_USER_NAME_LENGTH:
                    self.__player_name += chr(event.key).upper()
                # elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                #     self.__player_name = self.__player_name[:-1]


        if pressed_keys[pygame.K_w] and pressed_keys[pygame.K_q]:
            exit()
        if pressed_keys[pygame.K_DELETE] or pressed_keys[pygame.K_BACKSPACE]:
            self.__player_name = self.__player_name[:-1]
