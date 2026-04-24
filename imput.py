import pygame

class Input:
    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
