import os
import tkinter as tk
import gc
import time
from tkinter import Tk, filedialog
import pyautogui

def copy(command):
    os.popen(command)

#THIS IS THE MOUSE WIGGLER FUNCTION
def move_mouse(count):
    #TO DISABLE MOUSE WIGGLE COMMENT OUT THE FOLLOWING CODE
    if count % 2 == 0:
        pyautogui.moveRel(0, 25, duration = 0.25)
    else:
        pyautogui.moveRel(0, -25, duration = 0.25)
    time.sleep(0.25)
    #END COMMENT OUT
    
    #ALSO UNCOMMENT THE FOLLOWING TWO LINES
    #time.sleep(0.5)
    #pass
    

root = tk.Tk()
root.attributes('-topmost', True)
base_path = filedialog.askdirectory()
root.withdraw()

files1 = []
files2 = []
files3 = []
filesnew1 = []
filesnew2 = []
filesnew3 = []
path = os.getcwd()
try:
    os.mkdir(path + '/images')
except:
    pass

for r,d,f in os.walk(base_path):
    for file in f:
        if '.jpeg' in file:
            files1.append(os.path.join(r, file))
            filesnew1.append(file)
        elif '.jpg' in file:
            files2.append(os.path.join(r, file))
            filesnew2.append(file)
        elif '.png' in file:
            files3.append(os.path.join(r, file))
            filesnew3.append(file)

#tHIS MOVES YOUR CURSOR TO A STANDARD POSITION TO ENSURE THE WIGGLE DOES NOT COLLIDE WITH THE EDGE OF YOUR DISPLAY, WHICH THROWS AN ERROR           
pyautogui.moveTo(300, 300, 1)

count = 0
for count in range(0,len(files1)):
    command = 'copy \"' + files1[count] + '\" \"' + path + '/images/' + filesnew1[count] + '\"'
    copy(command)
    print(filesnew1[count])
    #MOUSE WIGGLER CALL
    move_mouse(count)
    
gc.collect()
time.sleep(30)
count = 0
for count in range(0,len(files2)):
    command = 'copy \"' + files2[count] + '\" \"' + path + '/images/' + filesnew2[count] + '\"'
    copy(command)
    print(filesnew2[count])
    #MOUSE WIGGLER CALL
    move_mouse(count)

gc.collect()
time.sleep(30)
count = 0
for count in range(0,len(files3)):
    command = 'copy \"' + files3[count] + '\" \"' + path + '/images/' + filesnew3[count] + '\"'
    copy(command)
    print(filesnew3[count])
    #MOUSE WIGGLER CALL
    move_mouse(count)
    
print('\n\n')
print("The program has finished running. Your files can be found in: " + str(path)+ '/images')
