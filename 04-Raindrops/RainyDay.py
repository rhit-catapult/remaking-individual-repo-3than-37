import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen =screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)
        """ Creates a Raindrop sprite that travels down at a random speed. """

    def move(self):
        self.y += self.speed
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # done 11: Change the  y  position of this Raindrop by its speed.
        

    def off_screen(self):
        return self.y > self.screen.get_height()


        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # done 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        

    def draw(self):
        pygame.draw.line(self.screen, (pygame.Color("dark green")), (self.x, self.y), (self.x, self.y + 5), 2)
        """ Draws this sprite onto the screen. """
        # done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).


class Hero:
    def __init__(self, screen: pygame.Surface, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_unbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_unbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0       
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_unbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_unbrella, (self.x, self.y))
        """ Draws this sprite onto the screen. """


    def hit_by(self, raindrop):
        hit_box = pygame.Rect(self.x, self.y, self.image_unbrella.get_width(), self.image_unbrella.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_cloud = pygame.image.load(image_filename)
        self.raindrops = []
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
    
    def draw(self):
        self.screen.blit(self.image_cloud, (self.x, self.y))
        """ Draws this sprite onto the screen. """
        # done 25: Draw (blit) this Cloud's image at its current position.
        

    def rain(self):
        for k in range(5):
            drop_x = random.randint(self.x, self.x + self.image_cloud.get_width())
            drop_y = self.y + self.image_cloud.get_height() -5
            rainspawn = Raindrop(self.screen, drop_x,drop_y)
            self.raindrops.append(rainspawn)

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("rainy day")
    clock = pygame.time.Clock()
    x = 600
    y = 200
    # test_drop = Raindrop(screen, 320, 10)
    mike = Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = Cloud(screen, x, y, "another_cloud.png")

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
# done 0: Call main.
