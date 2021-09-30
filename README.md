# USB_Image_Grabber
A program designed to collect all the images in a chosen directory. 

NOTE: THIS PROGRAM EXECUTES A MOUSE WIGGLER FUNCTION TO STOP YOUR PC FROM SLEEPING WHILE COLLECTING IMAGES. AS SUCH THIS IS INTENDED TO BE A 'SET AND FORGET' PROGRAM, DO NOT PLAN ON USING YOUR PC FOR THE DURATION OF ITS EXECUTION. I WILL ADD A COMMENT IN THE CODE IF YOU WOULD LIKE TO DISABLE THIS FUCTION.

# What is this?
I created this program based on commercially available products designed to aid in collecting pictures off a personal computer. It uses a windows batch file as well as python venv 3.8.10. Due to the use of a batch file for added simplicity as well as relying on a windows version of the python interpreter it was written for use on windows only.

# What does it do?
Within the `app` folder is a python script named `images.py` and a python 3.8.10 venv. The python script is the main portion of the program and utilizes tkinter to create a directory selection dialog. Using the selected directory as the start point it crawls all subdirectories looking for files ending in `.jpg`, `.jpeg`, or `.png`. Any files it finds that match those extensions is copied to a folder `images` (this will be created by the script upon execution).

# How can I use it?
To get started, first place all files of this repository on some kind of storage media ie usb dirve. Feel free to run it locally on you computer, but this was created with high portability in mind. I created this with the intention of it being dead simple and easy to use. To run, simply double click the `run.bat` file to execute the program. Next, a popup folder selection dialog will appear. Select whatever directory you wish to search for images in (i.e. C:\Users\USERNAME, where USERNAME is your windows account name) and wait for the program to complete and display 'The program has finished running.' in the popup command prompt. Your images will be found in the 'images' directory. During execution the popup command prompt will display the filenames and locations of files which are being copied to the images folder. Additionally the program will wiggle the mouse cursor for the duration of executioin to avoid your computer going to sleep/locking while running. Note: This script is meant to be an easy to use 'set it and forget it' style program so do not run it if you are intending to use you computer at the same time as the mouse wiggling may make doing anything difficult. Please note that the program will take a few minutes to display output in the command promt popup.
## If you want the simplest possible solution please download the `images.exe` file within the `exe version` folder. This is a simple, single file windows executable that does all the same functions as the python version.

# Why does this script call time.sleep so often?
This is because if you have many large image files python will attempt to issue the copy command as quickly as possible. This may lead to an 'out of memory' error. To fix this I add in a delay allowing the OS to at least partially process each copy command before issuing another in an attempt to stagger the memory being used at any one time. If you run into an out of memory error try adjusting the `sleep_time` variable at the top of `images.py` to be slightly longer (ie 0.3 -> 0.5).

# Donations
BTC - bc1q8wdfa8xvqhgdyudy9hdaqzelps2rarl9vzas4m <br/>
ETH - 0x77f533a7D98B6888f90543959fB5b8Ea3539eE0c <br/>
LTC - LSfCvorJ4FUUKZiKnw1f2xaH2akdUm44AS  <br/>
