import os
import pygame
from pygame import mixer

import helpers.manager as manager
from helpers.manager import Manager

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir(os.pardir)

mixer.pre_init(44100, -16, 2, 2048)
mixer.init()
pygame.init()


def main():
    mgr = Manager()
    manager.set_first_screen(mgr.screen, mgr.images)
    running = True

    while running:
        event = manager.check_for_events()
        if event == pygame.K_F1:
            manager.launch_animation(mgr.screen, mgr.images, mgr.timings, mgr.sounds)
        elif event == pygame.MOUSEBUTTONDOWN:
            running = False

    manager.quit_script()


main()
