# -*- coding: utf-8 -*-
"""A simple application to read joystick inputs and send them over UART

Modified from: http://www.pygame.org/docs/ref/joystick.html

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
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
is_running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
text_print = TextPrint()

# -------- Main Program Loop -----------
while is_running == True:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something

        #Handle quits
        if event.type == pygame.QUIT: 
            is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False

    # DRAWING STEP
    screen.fill(WHITE)
    text_print.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    text_print.print_to_screen(screen, "Number of joysticks: {}".format(joystick_count))
    text_print.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        text_print.print_to_screen(screen, "Joystick {}".format(i))
        text_print.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        text_print.print_to_screen(screen, "Joystick name: {}".format(name))
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        text_print.print_to_screen(screen, "Number of axes: {}".format(axes))
        text_print.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            text_print.print_to_screen(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        text_print.unindent()
            
        buttons = joystick.get_numbuttons()
        text_print.print_to_screen(screen, "Number of buttons: {}".format(buttons))
        text_print.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            text_print.print_to_screen(screen, "Button {:>2} value: {}".format(i,button))
        text_print.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        text_print.print_to_screen(screen, "Number of hats: {}".format(hats))
        text_print.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            text_print.print_to_screen(screen, "Hat {} value: {}".format(i, str(hat)))
        text_print.unindent()
        
        text_print.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
dm.print_warning("Closing...")
pygame.quit()
