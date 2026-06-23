# The two lines below allow you to use PyGame and System functions.
# Often programmers use code that other developers have written.
import pygame
import sys

# Let's turn pygame ON
pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("Ethan Falk")

# Now the screen is where all the magic is going to happen. Our screen will
# have a width of 640 pixels and a height of 480 pixels. The (0,0) point will
# be at the top left of our screen. 
screen = pygame.display.set_mode((320, 480))

# This is a loop that will run forever, simply because True is always true
while True:
    # Here's another loop inside of the first loop. Notice the indentation,
    # moving one tab width into the while loop makes this statement part of the
    # loop instead of outside of it.
    for event in pygame.event.get():
        # Let's just print all the events that happen in our window, wonder
        # what those could be?
        print(event)

        # we must allow our users to quit the game right? I mean not everyone
        # wants to play forever.
        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    # Make the background white by uncommenting the line below
    screen.fill(pygame.Color("white"))

    # Draw things on the screen

    #draw a circle (any size, any color, anywhere)
    pygame.draw.circle(screen, "blue", (0,0), 50 )

    #draw a red circle in the middle of the screen with a radius 100
    pygame.draw.circle(screen, "red", (160,240), 100  )

    #draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    pygame.draw.circle(screen, "yellow", (320,480), 10  )

    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()
