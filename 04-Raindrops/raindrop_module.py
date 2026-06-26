import pygame
import random 

class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen =screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > self.screen.get_height()


    def draw(self):
        pygame.draw.line(self.screen, (pygame.Color("dark green")), (self.x, self.y), (self.x, self.y + 5), 2)