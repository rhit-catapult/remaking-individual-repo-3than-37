import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-10, 10)
        self.size = random.randint(4, 20)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def draw(self):
        pygame.draw.circle(self.screen, (self.color), (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def edge_y(self):
        return self.y < self.size or self.y + self.size > self.screen.get_height()

    def edge_x(self):
        return self.x < self.size or self.x + self.size > self.screen.get_height()



# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    screen_size = random.randint(300, 1000)
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball_work = Ball(screen)

    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('white'))

        ball_work.draw()
        ball_work.move()

        if ball_work.edge_y():
            ball_work.speed_y = -ball_work.speed_y

        if ball_work.edge_x():
            ball_work.speed_x = -ball_work.speed_x
        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
