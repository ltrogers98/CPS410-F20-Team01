import pygame
import time
from pynput.keyboard import Key,Controller
from pygame.locals import *

#initialize pygame + joystick
pygame.init()
pygame.joystick.init()

#initialize keyboard
keyboard = Controller()

#set joystick to equal the first joystick found on device
joystick = pygame.joystick.Joystick(0)

run = True
while(run):
    
    """
    This for loop will continuously look for input from the joystick.
    Important not to delete
    """
    for event in pygame.event.get():
        #if button is pressed on joystick, exit while loop
        if event.type == pygame.JOYBUTTONDOWN:
            run = False
    
    x = joystick.get_axis(0)#value of x-axis reading on joystick ranging from 1 to -1
    y = joystick.get_axis(1)#value of y-axis reading on joystick ranging from 1 to -1
    
    """
    Check each pair (x,y) and give output equivalent to
    how strongly the joystick is being pointed in a certain
    direction.

    Works by getting an x and y value every iteration (multiple
    times per second) and checks the magnitude of these values with
    a LARGE if-else block. sleep statements are used to delay iterations
    that contain more decisive input. X and Y values, ranging from -1 to 1,
    will be considered at peak decisive input if the absolute value is
    greater than 0.8. Any input with a value greater than 0.8 will be
    slept for the longest. Any input with a value in between 0.6 and 0.8
    will be slept for the second longest. Sleep times are as follows:
    --------------------------------------------------------
    |Absolute value of largest intput  |     Sleep time    |
    |             >=0.8                |       .2s         |
    |             >=0.6                |       .15s        |
    |             >=0.4                |       .1s         |
    |             >=0.2                |       .05s        |
    |              <0.2                |       .025s       |
    --------------------------------------------------------
    """
    if abs(x) < 0.2 and abs(y) < 0.2:
        time.sleep(.025)
        continue
    #top-left quadrant
    elif x >= 0.8 and abs(y) < 0.2:#strong left
        keyboard.press('a')
        time.sleep(.2)
        keyboard.release('a')
    elif x >= 0.8 and y >= 0.8:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.8 and y >= 0.6:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.8 and y >= 0.4:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.8 and y >= 0.2:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.6 and abs(y) < 0.2:#medium-strong left
        keyboard.press('a')
        time.sleep(.15)
        keyboard.release('a')
    elif x >= 0.6 and y >= 0.8:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.6 and y >= 0.6:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.6 and y >= 0.4:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.6 and y >= 0.2:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.4 and abs(y) < 0.2:#medium-weak left
        keyboard.press('a')
        time.sleep(.1)
        keyboard.release('a')
    elif x >= 0.4 and y >= 0.8:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.4 and y >= 0.6:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.4 and y >= 0.4:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.4 and y >= 0.2:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.2 and abs(y) < 0.2:#weak left
        keyboard.press('a')
        time.sleep(.05)
        keyboard.release('a')
    elif x >= 0.2 and y >= 0.8:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.2 and y >= 0.6:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.2 and y >= 0.4:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('a')
        keyboard.release('w')
    elif x >= 0.2 and y >= 0.2:
        keyboard.press('a')
        keyboard.press('w')
        time.sleep(.05)
        keyboard.release('a')
        keyboard.release('w')
    #bottom-left quadrant
    elif x >= 0.8 and y <= -0.8:#strong left
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.8 and y <= -0.6:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.8 and y <= -0.4:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.8 and y <= -0.2:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.6 and y <= -0.8:#medium-strong left
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.6 and y <= -0.6:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.6 and y <= -0.4:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.6 and y <= -0.2:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.2 and y <= -0.8:#weak left
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.2 and y <= -0.6:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.2 and y <= -0.4:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.1)
        keyboard.release('a')
        keyboard.release('s')
    elif x >= 0.2 and y <= -0.2:
        keyboard.press('a')
        keyboard.press('s')
        time.sleep(.05)
        keyboard.release('a')
        keyboard.release('s')
    #top-right quadrant
    elif x <= -0.8 and abs(y) < 0.2:#strong right
        keyboard.press('d')
        time.sleep(.2)
        keyboard.release('d')
    elif x <= -0.8 and y >= 0.8:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.8 and y >= 0.6:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.8 and y >= 0.4:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.8 and y >= 0.2:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.6 and abs(y) < 0.2:#medium-strong right
        keyboard.press('d')
        time.sleep(.15)
        keyboard.release('d')
    elif x <= -0.6 and y >= 0.8:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.6 and y >= 0.6:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.6 and y >= 0.4:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.6 and y >= 0.2:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.4 and abs(y) < 0.2:#medium-weak right
        keyboard.press('d')
        time.sleep(.1)
        keyboard.release('d')
    elif x <= -0.4 and y >= 0.8:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.4 and y >= 0.6:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.4 and y >= 0.4:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.4 and y >= 0.2:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.2 and abs(y) < 0.2:#weak right
        keyboard.press('d')
        time.sleep(.05)
        keyboard.release('d')
    elif x <= -0.2 and y >= 0.8:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.2 and y >= 0.6:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.2 and y >= 0.4:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('d')
        keyboard.release('w')
    elif x <= -0.2 and y >= 0.2:
        keyboard.press('d')
        keyboard.press('w')
        time.sleep(.05)
        keyboard.release('d')
        keyboard.release('w')
    #bottom-right quadrant
    elif x <= -0.8 and y <= -0.8:#strong right
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.8 and y <= -0.6:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.8 and y <= -0.4:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.8 and y <= -0.2:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.6 and y <= -0.8:#medium-strong right
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.6 and y <= -0.6:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.6 and y <= -0.4:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.6 and y <= -0.2:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.4 and y <= -0.8:#medium-weak right
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.4 and y <= -0.6:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.4 and y <= -0.4:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.1)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.4 and y <= -0.2:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.1)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.2 and y <= -0.8:#weak right
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.2 and y <= -0.6:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.2 and y <= -0.4:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.1)
        keyboard.release('d')
        keyboard.release('s')
    elif x <= -0.2 and y <= -0.2:
        keyboard.press('d')
        keyboard.press('s')
        time.sleep(.05)
        keyboard.release('d')
        keyboard.release('s')
    #only input on y axis
    elif abs(x) < 0.2 and y >= 0.8:#strong up
        keyboard.press('w')
        time.sleep(.2)
        keyboard.release('w')
    elif abs(x) < 0.2 and y >= 0.6:#medium-strong up
        keyboard.press('w')
        time.sleep(.15)
        keyboard.release('w')
    elif abs(x) < 0.2 and y >= 0.4:#medium-weak up
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('w')
    elif abs(x) < 0.2 and y >= 0.2:#weak up
        keyboard.press('w')
        time.sleep(.05)
        keyboard.release('w')
    elif abs(x) < 0.2 and y >= -0.8:#strong down
        keyboard.press('s')
        time.sleep(.2)
        keyboard.release('s')
    elif abs(x) < 0.2 and y <= -0.6:#medium-strong down
        keyboard.press('s')
        time.sleep(.15)
        keyboard.release('s')
    elif abs(x) < 0.2 and y <= -0.4:#medium-weak down
        keyboard.press('s')
        time.sleep(.1)
        keyboard.release('s')
    elif abs(x) < 0.2 and y <= -0.2:#weak down
        keyboard.press('s')
        time.sleep(.5)
        keyboard.release('s')

#exit
pygame.quit()
