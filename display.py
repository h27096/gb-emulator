import pygame

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((160, 144))
        pygame.display.set_caption("Game Boy Emulator")

    def update(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill((0, 0, 0))
