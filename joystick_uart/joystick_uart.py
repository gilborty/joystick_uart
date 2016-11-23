# -*- coding: utf-8 -*-
"""A simple application to read joystick inputs and send them over UART

Modified from: http://www.pygame.org/docs/ref/joystick.html

Example:
        $ python joystick_uart.py


Attributes:

Todo:

"""

import pygame
import serial

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

#Serial init
default_port = '/dev/ttyUSB0'
default_baud_rate = 115200

ser = serial.Serial(
    port=default_port,
    baudrate=default_baud_rate,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

# Main script init
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

# Axis state info
lastAxis = 0.0
firstTime = True

# Button state info
enablePressed = False
disablePressed = False

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

        #Since we are only controlling forward and backward control of motors, only read the value from axis 1
        text_print.indent()

        #Boolean for zero input
        axis = joystick.get_axis(1)
        text_print.print_to_screen(screen, "Axis {} value: {:>6.3f}".format(1, axis))
    
        if firstTime:
            ser.write("Axis:" + str(axis) + '\r\n') 
            ser.flush()
            dm.print_info("Wrote axis:" + str(axis))
            lastAxis = axis
            firstTime = False
        elif axis != lastAxis:
            ser.write("Axis:" + str(axis) + '\r\n') 
            ser.flush()
            dm.print_info("Wrote axis:" + str(axis))
            lastAxis = axis

        #Button 10 Disable
        disable_button = joystick.get_button(10)
        text_print.print_to_screen(screen, "Disable Button: {}".format(disable_button))

        # Not pressed and wasn't pressed 
            # Do nothing
        # Not pressed but had been pressed (released)
        if (not disable_button) and disablePressed:
            disablePressed = False
        # Pressed but hadn't been pressed (pressed)
        elif disable_button and (not disablePressed):
            ser.write("Disable" + '\r\n')
            ser.flush()
            dm.print_info("Wrote disable")
            disablePressed = True
        # Pressed and had been pressed (held)
            # Do nothing
        
        #Button 11 Enable
        enable_button = joystick.get_button(11)

        # Not pressed and wasn't pressed 
            # Do nothing
        # Not pressed but had been pressed (released)
        if (not enable_button) and enablePressed:
            enablePressed = False
        # Pressed but hadn't been pressed (pressed)
        elif enable_button and (not enablePressed):
            ser.write("Enable" + '\r\n')
            ser.flush()
            dm.print_info("Wrote Enable")
            enablePressed = True
        # Pressed and had been pressed (held)
            # Do nothing

        text_print.print_to_screen(screen, "Enable Button: {}".format(enable_button))

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
ser.close()
pygame.quit()
