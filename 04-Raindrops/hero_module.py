import pygame
import time 

class Hero:
    def __init__(self, screen: pygame.Surface, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_unbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_unbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0       

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_unbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_unbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        hit_box = pygame.Rect(self.x, self.y, self.image_unbrella.get_width(), self.image_unbrella.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)