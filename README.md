# Twinkly Tetris
Do you have the Twinkly Squares LED panels? With this program, you can play tetris on them! 

This does not break, modify, or otherwise change your twinkly device. Simply use the twinkly app again to kick the device back into normal operation :) 

## Setup
Ran on python version 3.11.11
- I used anaconda to install an earlier python version, but up to you

Python libraries
- You may need to install some libraries. You can see all imports at the top of main.py
- I used pip for installation, but up to you

## Use

### Running
navigate into this folder and run:
```
main.py <numPanels> <rotate> <classicMode> <device>
```
All command line args have default values, so you can include as few as you want. Default behavior defined below

numPanels
- Default is 1. Number of twinkly squares used. currently supports 1 panel, or 2 panels set as 1 panel wide x 2 panels tall

Rotate 
- Default is 0. For 1 panel only, can rotate 0, 90, 180, or 270 degrees using values 0, 1, 2, or 3

classicMode
- Default is off. If value is 1, then game will be in classic mode and have pieces in classic tetris colors. Any other value will randomize piece colors

Device
- Have multiple twinkly devices? If not, then ignore this one. You can specify the device to connect to, so that the program either connects to the specified device or terminates. See troubleshooting for more information

### Controls/Gameplay
- Left and right arrow keys for moving a piece
- Down arrow key makes a piece fall faster
- “r” key to rotate piece
- Works the same as normal tetris, make a line to clear it. A score is given at the end, one digit at a time (also outputted to the command line)


## Troubleshooting
- Having the twinkly app open while running the software causes problems. Just close the app before running the program
- Resetting your device can also help. Go to the devices tab, select your device, and press the trash can. Then reconnect it. WARNING: this may delete your twinkly device's saved presets and such
- Multiple devices: you can find your device id when you connect the device, can do it through the xled library(look at the github in the credits), or there may be an option through the app that I haven’t found. It will be the word ‘Twinkly’ followed by an underscore and some characters, for example "Twinkly_D11F1D"

## Explanation
There's a couple setup lines that can be seen at the bottom of twinklyConnect.py which define the device and set the mode to real time. 
Most of the code is typical tetris, using a big matrix to store and update RGB values for all the pixels in the twinkly square(s). This matrix is sent to the twinkly device periodically, to serve as screen refreshes. This is done with
```
control.set_rt_frame_socket(frameTest, 2)
```
This function calls frameTest’s read function, which is defined in frameClass.py. Essentially it makes a big string of binary, unsigned ints from the matrix. Each pixel has 3 unsigned ints, corresponding to the r, g, and b values. The comments in the code explain how the pixels are mapped

## Credits

This project was made by Nathaniel Grenke

A huge thank you to Pavol Babinčák and the contributors to the xled library. Their project can be found at https://github.com/scrool/xled
