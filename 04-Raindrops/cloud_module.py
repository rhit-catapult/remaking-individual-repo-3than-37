import pygame
import random 
import raindrop_module

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_cloud = pygame.image.load(image_filename)
        self.raindrops = []
    
    def draw(self):
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self):
        for k in range(5):
            drop_x = random.randint(self.x, self.x + self.image_cloud.get_width())
            drop_y = self.y + self.image_cloud.get_height() -5
            rainspawn = raindrop_module.Raindrop(self.screen, drop_x,drop_y)
            self.raindrops.append(rainspawn)