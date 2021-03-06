import pygame
from pygame.locals import *

import sys


class Display():

    def __init__(self, wait):
        self.screen = pygame.display.set_mode((700, 502))

        self.clock = pygame.time.Clock()
        self.wait = wait


    def print(self, array, highlights):
        self.screen.fill((0, 0, 0))
        bar_size = (700 / len(array)) / 1.4
        space = 0.4 * bar_size

        x = space // 2
        for i, val in enumerate(array):
            y = round((500 * val) / len(array))

            # green bars for current bars. white for all others
            color = (0, 255, 0) if i in highlights else (255, 255, 255)

            pygame.draw.rect(self.screen, color, pygame.Rect(round(x), 501 - y, round(bar_size), y))
            x += bar_size + space

        pygame.display.update()


        #check if window was closed
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_q:
                pygame.quit()
                sys.exit()

        if self.wait: pygame.time.wait(self.wait)


    def draw_completed_array(self, array):
        bar_size = (700 / len(array)) / 1.4
        space = 0.4 * bar_size

        # we have 500 ms for the whole array
        wait_time = 500 // len(array)

        # this is just because the switching looks ugly otherwise
        # because the last switched indexes are still green
        self.print(array, ())

        x = space // 2
        for i, val in enumerate(array):
            y = round((500 * val) / len(array))

            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(round(x), 501 - y, round(bar_size), y))
            x += bar_size + space

            pygame.time.wait(wait_time)
            pygame.display.update()

