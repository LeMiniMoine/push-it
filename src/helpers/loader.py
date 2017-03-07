import json

from pygame import display
from pygame import mouse
from pygame import image
from pygame import transform
from pygame import mixer
from pygame import FULLSCREEN


class ConfigLoader:
    def __init__(self):
        self.images = read_config('resources/configs/images_config.json')
        self.timings = read_config('resources/configs/timings_config.json')
        self.sounds = read_config('resources/configs/sounds_config.json')


class SoundsLoader:
    def __init__(self, config):
        self.explosion = mixer.Sound(config['explosion'])
        self.winning = mixer.Sound(config['winning'])


class TimingsLoader:
    def __init__(self, config):
        self.firstTimingInMs = config['first_screen_in_s'] * 1000
        self.secondTimingInMs = config['second_screen_in_s'] * 1000
        self.thirdTimingInMs = config['third_screen_in_s'] * 1000


class FullScreen:
    def __init__(self):
        mouse.set_visible(False)
        self.width = display.Info().current_w
        self.height = display.Info().current_h
        self.__screen = display.set_mode((self.width, self.height), FULLSCREEN)

    def switch_background(self, image):
        self.__screen.blit(image, [0, 0])
        display.flip()


class ImagesLoader:
    def __init__(self, config, screen_width, screen_height):
        self.__config = config
        self.base = self.__load_base_images(screen_width, screen_height)
        self.results = self.__load_results_images_as_matrix(screen_width, screen_height)
        self.total_gifts_ratio = self.results[3][0]

    def __load_base_images(self, screen_width, screen_height):
        pic_intro = load_image_scaled(self.__config['first_image_path'], screen_width, screen_height)
        pic_button_pushed = load_image_scaled(self.__config['second_image_path'], screen_width, screen_height)
        return {'intro': pic_intro, 'pushed': pic_button_pushed}

    def __load_results_images_as_matrix(self, screen_width, screen_height):
        first_rebel_pic = load_image_scaled(self.__config['first_rebel_image_path'], screen_width, screen_height)
        second_rebel_pic = load_image_scaled(self.__config['second_rebel_image_path'], screen_width, screen_height)
        third_rebel_pic = load_image_scaled(self.__config['third_rebel_image_path'], screen_width, screen_height)
        fourth_rebel_pic = load_image_scaled(self.__config['fourth_rebel_image_path'], screen_width, screen_height)

        first_gift_pic = load_image_scaled(self.__config['first_gift_image_path'], screen_width, screen_height)
        second_gift_pic = load_image_scaled(self.__config['second_gift_image_path'], screen_width, screen_height)
        third_gift_pic = load_image_scaled(self.__config['third_gift_image_path'], screen_width, screen_height)
        fourth_gift_pic = load_image_scaled(self.__config['fourth_gift_image_path'], screen_width, screen_height)

        first_gift_ratio = self.__config['first_gift_ratio']
        second_gift_ratio = self.__config['second_gift_ratio'] + first_gift_ratio
        third_gift_ratio = self.__config['third_gift_ratio'] + second_gift_ratio
        fourth_gift_ratio = self.__config['fourth_gift_ratio'] + third_gift_ratio

        matrix_width, matrix_height = 3, 4

        results = [[0 for x in range(matrix_width)] for y in range(matrix_height)]

        results[0][0], results[0][1], results[0][2] = first_gift_ratio, first_rebel_pic, first_gift_pic
        results[1][0], results[1][1], results[1][2] = second_gift_ratio, second_rebel_pic, second_gift_pic
        results[2][0], results[2][1], results[2][2] = third_gift_ratio, third_rebel_pic, third_gift_pic
        results[3][0], results[3][1], results[3][2] = fourth_gift_ratio, fourth_rebel_pic, fourth_gift_pic

        return results


def load_image_scaled(path, screen_width, screen_height):
    return transform.scale(image.load(path), (screen_width, screen_height))


def read_config(file_path):
    return json.load(open(file_path))
