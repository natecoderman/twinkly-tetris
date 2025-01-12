import pygame
import sys
import xled
import threading
import random
import time

import os
import signal

DEFINE_HEIGHT = 16 #y axis, in pixels
DEFINE_WIDTH = 8 #x axis, in pixels
DEFINE_DEVICE = "Twinkly_D11F1D"

DEFINE_SIZE = 1

class Frame:
    def __init__(self, matrix):
        self.matrix = matrix
    def read(self):
        # Start from the bottom-right corner and snake up/down
        bin_string = b""

        
        for i in range(DEFINE_SIZE):
            bin_string += bytes([0, 0, 0])
        
        return bin_string
    



def timeout_handler():
    print("failed to connect: timeout") 
    # exit
    os.kill(os.getpid(), signal.SIGINT) # if this doesn't work, divide by zero
    os.kill(os.getpid(), signal.SIGSEGV)


timeout = 5  # Set your timeout duration in seconds
timer = threading.Timer(timeout, timeout_handler)
timer.start()

try:
    discovered_device = xled.discover.discover()

finally:
    timer.cancel()
    print("Discover completed within timeout.")

if (discovered_device.id != DEFINE_DEVICE):
    print("failed to connect: wrong device. connected: " + discovered_device.id)
    sys.exit()
else:
    print("success of " + discovered_device.id)




control = xled.ControlInterface(discovered_device.ip_address, discovered_device.hw_address)

matTest = [[(0, 0, 0) for _ in range(DEFINE_HEIGHT)] for _ in range(DEFINE_WIDTH)] # initialize matrix of colors
matStore = [[None for _ in range(DEFINE_HEIGHT)] for _ in range(DEFINE_WIDTH)] # holds data of what spaces are already full of blocks


frameTest = Frame(matTest)
control.set_mode('rt')


#print(matTest)

for i in range(128):
    control.set_rt_frame_socket(frameTest, 2)
    DEFINE_SIZE += 1
    time.sleep(0.2)


