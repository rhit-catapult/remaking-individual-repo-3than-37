import pygame
import sys
import time  
import cloud_module
import hero_module

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("rainy day")
    clock = pygame.time.Clock()
    x = 600
    y = 200
    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = cloud_module.Cloud(screen, x, y, "another_cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP]:
            print("up")
            cloud.y -= 5
        if keys [pygame.K_DOWN]:
            print("down")
            cloud.y += 5
        if keys [pygame.K_LEFT]:
            print("left")
            cloud.x -= 5
        if keys [pygame.K_RIGHT]:
            print("right")
            cloud.x += 5


        screen.fill(pygame.Color(255,255,255))
        
        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)
        mike.draw()
        alyssa.draw()

        pygame.display.update()
    

main()