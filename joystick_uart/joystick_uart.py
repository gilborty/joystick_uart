# -*- coding: utf-8 -*-
"""A simple application to read joystick inputs and send them over UART

Example:
        $ python joystick_uart.py


Attributes:

Todo:

"""

import pygame

import debug_messages as dm

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print_to_screen(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10

#Global variable for the main execution loop
is_running = False

def init():
    """ Function to Initialize

        Args:

        Returns:
            bool: The return value. True if initialization was successful, False if it failed
    """

    #Initialize pygame
    dm.print_info("Initializing PyGame")
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [500, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    #Loop until the user clicks the close button.
    global is_running
    is_running = True

    # Initialize the joysticks
    pygame.joystick.init()

    return True


def main():
    """ The main point of execution of the script

        Args:

        Returns:
    """
    global is_running

    if init():
        #Start the main loop of the script
        dm.print_info("Starting joystick_uart")

        #Print to window handle
        text_print = TextPrint()

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        while is_running:

            # EVENT PROCESSING STEP
            for event in pygame.event.get(): # User did something
                
                #Handle key presses
                if event.type == pygame.KEYDOWN:
                    
                    #If user presses escape key, quit
                    if event.key == pygame.K_ESCAPE:
                        is_running = False

            #Get the number of joysticks connected
            joystick_count = pygame.joystick.get_count()

            #For all of the joysticks connected
            for index in range(joystick_count):
                
                #init this joystic
                joystick = pygame.joystick.Joystick(index)
                joystick.init()



            
            # Limit to 30 frames per second
            clock.tick(30)

        dm.print_warning("Closing.")
        pygame.quit()

    else:
        dm.print_fatal("Failed to initialize. Exiting")
        pygame.quit()





if __name__ == "__main__":

    main()
