import pygame
import math
from GameConstants import *
from GameObject import *

class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = GameConstants.BALL_SPEED
        self.__increment = GameConstants.MOVEMENT_INCREMENT
        self.__direction = [1,-1]
        self.__in_motion = False

        super(Ball,self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def set_speed(self,new_speed):
        self.__speed = new_speed

    def reset_speed(self):
        self.set_speed(GameConstants.BALL_SPEED)

    def get_speed(self):
        return self.__speed

    def get_direction(self):
        return self.__direction


    def is_in_motion(self):
        return self.__in_motion

    def set_motion(self, is_moving):
        self.__in_motion = is_moving
        self.reset_speed()

    ## This is the original change direction code, that has been replaced:
    # def change_direction2(self, game_object):
    #     position = self.get_position()
    #     size = self.get_size()
    #     object_position = game_object.get_position()
    #     object_size = game_object.get_size()
    #
    #     # ball hits object below:
    #     if \
    #     position[1] > object_position[1] and \
    #     position[1] < object_position[1] + object_size[1]and \
    #     position[0] > object_position[0] and \
    #     position[0] < object_position[0] + object_size[0]:
    #         self.set_position((position[0], object_position[1]+object_size[1]))
    #         self.__direction[1] *= -1
    #
    #
    #     # ball hits object from above:
    #     elif \
    #     position[1] + size[1]> object_position[1] and \
    #     position[1] + size[1]< object_position[1] + object_size[1] and\
    #     position[0] > object_position[0] and \
    #     position[0] < object_position[0] + object_size[0]:
    #         self.set_position((position[0],object_position[1]-size[1]))
    #         self.__direction[1] *= -1
    #
    #     # ball hits object from left:
    #     elif \
    #     position[0] + size[0] > object_position[0] and\
    #     position[0] < object_position[0]:
    #         self.set_position((object_position[0]-size[0],position[1]))
    #         self.__direction[0] *= -1
    #
    #     # ball hits object from right:
    #     elif \
    #     position[0] + size[0] > object_position[0] + object_size[0] and\
    #     position[0] < object_position[0] + object_size[0]:
    #         self.set_position((object_position[0]+object_size[0],position[1]))
    #         self.__direction[0] *= -1
    #
    #     else:
    #         self.__direction[0] *= -1
    #         self.__direction[1] *= -1

    def change_direction(self, game_object):
        direction = self.get_direction()
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if self.hit_from_left(game_object):
            if self.hit_object_left(game_object):
                self.put_left(game_object)
                self.redirect_x()
            elif self.hit_object_above(game_object):
                self.put_above(game_object)
                self.redirect_y()
            elif self.hit_object_below(game_object):
                self.put_below(game_object)
                self.redirect_y()
            else:
                if direction[1] > 0:
                    self.put_above(game_object)
                    self.redirect_y()
                else:
                    self.put_below(game_object)
                    self.redirect_y()

        else:
            if self.hit_object_right(game_object):
                self.put_right(game_object)
                self.redirect_x()
            elif self.hit_object_above(game_object):
                self.put_above(game_object)
                self.redirect_y()
            elif self.hit_object_below(game_object):
                self.put_below(game_object)
                self.redirect_y()
            else:
                if direction[1] > 0:
                    self.put_above(game_object)
                    self.redirect_y()
                else:
                    self.put_below(game_object)
                    self.redirect_y()







    def hit_from_left(self, game_object):
        if self.intersects(game_object) and self.get_direction()[0] > 0:
            return True
        return False

    def hit_from_right(self, game_object):
        if self.intersects(game_object) and self.get_direction()[0] <= 0:
            return True
        return False

    def hit_object_left(self,game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if position[0] + size[0] > object_position[0] and\
        position[0] < object_position[0]:
            return True
        return False

    def hit_object_right(self,game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if position[0] + size[0] > object_position[0] + object_size[0] and\
        position[0] < object_position[0] + object_size[0]:
            return True
        return False

    def hit_object_above(self,game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if position[1] + size[1]> object_position[1] and \
        position[1] < object_position[1]:
            return True
        return False

    def hit_object_below(self,game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if position[1] + size[1] > object_position[1] + object_size[1] and \
        position[1] < object_position[1] + object_size[1]:
            return True
        return False


    def put_left(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        self.set_position((object_position[0]-size[0], position[1]))


    def put_right(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        self.set_position((object_position[0]+object_size[0], position[1]))


    def put_above(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        self.set_position((position[0], object_position[1]-size[1]))


    def put_below(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        self.set_position((position[0], object_position[1]+object_size[1]))



    def redirect_x(self):
        self.__direction[0] *= -1

    def redirect_y(self):
        self.__direction[1] *= -1





    def change_speed(self,game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()


        a = self.get_speed()[0]
        b = self.get_speed()[1]
        k = GameConstants.BALL_PAD_INTERACTION_SPEEDUP
        norm_right = math.sqrt((a**2 + b**2)/((k**2)*(a**2) + (b**2)))
        new_speed_right = [k*a,b]
        norm_left = math.sqrt((a**2 + b**2)/((a**2) + (k**2)*(b**2)))
        new_speed_left = [a,k*b]

        # Left Pad Hit
        if position[0] + size[0] < object_position[0] + GameConstants.BALL_PAD_INTERACTION_THRESHOLD * object_size[0]:
            self.set_speed(new_speed_left)
        # Right Pad Hit
        if position[0] > object_position[0] + (1 - GameConstants.BALL_PAD_INTERACTION_THRESHOLD) * object_size[0]:
            self.set_speed(new_speed_right)

    def update_position(self):

        if not self.is_in_motion():
            pad_position = self.__game.get_pad().get_position()
            self.set_position((pad_position[0]+GameConstants.PAD_SIZE[0]/2-GameConstants.BALL_SIZE[0]/2,
                                pad_position[1]-GameConstants.BALL_SIZE[1]))
            return

        game = self.__game
        position = self.get_position()
        size = self.get_size()
        new_position = (position[0] + (self.__increment*self.__speed[0])*self.__direction[0],
                        position[1] + (self.__increment*self.__speed[1])*self.__direction[1])

        # Bounce off right wall:
        if new_position[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            if game.get_scene() == GameConstants.PLAYING_SCENE:
                game.play_sound(GameConstants.SOUND_HIT_WALL)
            new_position = (GameConstants.SCREEN_SIZE[0]- size[0], new_position[1])
            self.__direction[0] *= -1
        # Bounce off left wall:
        if new_position[0] <= 0:
            if game.get_scene() == GameConstants.PLAYING_SCENE:
                game.play_sound(GameConstants.SOUND_HIT_WALL)
            new_position = (0,new_position[1])
            self.__direction[0] *= -1
        # Bounce off top wall:
        if new_position[1] <= 0:
            if game.get_scene() == GameConstants.PLAYING_SCENE:
                game.play_sound(GameConstants.SOUND_HIT_WALL)
            new_position = (new_position[0], 0)
            self.__direction[1] *= -1
        # Bounce off bottom wall:
        if new_position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            new_position = (new_position[0], GameConstants.SCREEN_SIZE[1]-size[1])
            self.__direction[1] *= -1

        self.set_position(new_position)


    def is_ball_dead(self):
        position = self.get_position()
        size = self.get_size()

        if position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            return True
        return False
