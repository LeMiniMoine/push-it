from pygame import quit as quit_pygame
from pygame import time
from pygame import mixer
from pygame import event as events
from pygame import K_F1
from pygame import KEYDOWN
from pygame import MOUSEBUTTONDOWN
from random import randint

from helpers.loader import ConfigLoader
from helpers.loader import FullScreen
from helpers.loader import ImagesLoader
from helpers.loader import SoundsLoader
from helpers.loader import TimingsLoader


class Manager:
    def __init__(self):
        self.__config = ConfigLoader()
        self.screen = FullScreen()
        self.images = ImagesLoader(self.__config.images, self.screen.width, self.screen.height)
        self.timings = TimingsLoader(self.__config.timings)
        self.sounds = SoundsLoader(self.__config.sounds)


def set_first_screen(screen, images):
    screen.switch_background(images.base['intro'])


def check_for_events():
    for event in events.get():
        if event.type == KEYDOWN and event.key == K_F1:
            events.set_blocked(KEYDOWN)
            events.clear()
            return K_F1
        if event.type == MOUSEBUTTONDOWN:
            return MOUSEBUTTONDOWN


def launch_animation(screen, images, timings, sounds):
    sounds.explosion.play()
    screen.switch_background(images.base['pushed'])
    time.delay(timings.firstTimingInMs)
    result = randint(1, images.total_gifts_ratio)
    result_found = False
    for y in range(len(images.results)):
        if not result_found and result < images.results[y][0]:
            sounds.winning.play()
            result_found = True
            screen.switch_background(images.results[y][1])
            time.delay(timings.secondTimingInMs)
            screen.switch_background(images.results[y][2])
            time.delay(timings.thirdTimingInMs)
    events.set_allowed(KEYDOWN)
    screen.switch_background(images.base['intro'])


def quit_script():
    mixer.quit()
    quit_pygame()
