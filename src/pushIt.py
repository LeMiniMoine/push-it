import pygame
from pygame import mixer

import manager
from manager import Manager

pygame.init()
mixer.init()


def main():
    mgr = Manager()
    manager.set_first_screen(mgr.screen, mgr.images)
    running = True

    while running:
        event = manager.check_for_events()
        if event == manager.K_F1:
            manager.launch_animation(mgr.screen, mgr.images, mgr.timings, mgr.sounds)
        elif event == manager.MOUSEBUTTONDOWN:
            running = False

    manager.quit_script()


main()
