import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    dogs = pygame.image.load("2dogs.JPG")
    #  1: Create an image with the 2dogs.JPG image
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dogs = pygame.transform.scale(dogs, (IMAGE_SIZE,IMAGE_SIZE))

    # Prepare the text caption(s)
    silly_font = pygame.font.SysFont("jokerman", 40)
    silly_text = silly_font.render("hehehehheh", False, "green")
    font = pygame.font.SysFont("extra", 28)
    caption = font.render("dog based superposition", False, "black" )
    #jokerman, extra, bell, comicsansms
    # TODO 4: Create a font object with a size 28 font.
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).

    # Prepare the music
    bark = pygame.mixer.Sound("bark.wav")
    # TODO 8: Create a Sound object from the "bark.wav" file.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark.play()
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        screen.blit(dogs, (0,0))
        x = screen.get_width() / 2 - caption.get_width() / 2
        y = screen.get_height() - caption.get_height()
        screen.blit(caption, (x,y))
        screen.blit(silly_text, (screen.get_width() / 2, screen.get_height() /2))
        #  2: Draw (blit) the image onto the screen at position (0, 0)

        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
