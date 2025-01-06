# https://www.lastcloudia.com/en/

import time
from PIL import ImageGrab
import mouse
import win32gui #pip install pywin32

global_window_handle = 0

def findWindow():
    win32gui.EnumWindows(callback, None)

    # print(windowHandle)

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)

    if "Last Cloudia" == win32gui.GetWindowText(hwnd):
        global global_window_handle

        global_window_handle = hwnd
        print("Window Found: %s" % win32gui.GetWindowText(hwnd))
        # print(hwnd)
        # print("\tLocation: (%d, %d)" % (global_x, global_y))
        # print("\t    Size: (%d, %d)" % (global_w, global_h))
        # print("Global X", global_x)
        # print("Global Y", global_y)
        # print("Global W", global_w)
        # print("Global H", global_h)
        
        return # Return to end function when proper window is found

# def old_missionOverBox(rect):
#     window_x = rect[0]
#     window_y = rect[1]
#     window_w = rect[2] - rect[0]
#     window_h = rect[3] - rect[1]

#     x = window_x + (.83 * window_w)
#     y = window_y + (.93 * window_h)
#     x2 = (window_x + window_w) - (.15 * window_w)
#     y2 = (window_y + window_h) - (.06 * window_h)

#     return (x, y, x2, y2)

def missionOverBox(rect):
    window_x = rect[0]
    window_y = rect[1]
    window_w = rect[2] - rect[0]
    window_h = rect[3] - rect[1]

    x = window_x + (.495 * window_w)
    y = window_y + (.72 * window_h)
    x2 = (window_x + window_w) - (.495 * window_w)
    y2 = (window_y + window_h) - (.27 * window_h)

    return (x, y, x2, y2)

if __name__ == '__main__':
    findWindow()

    # THIS IS TEST CODE TO TUNE THE "BOX"
    # position = ladourBox()
    # position = ntBox()

    # im = ImageGrab.grab(bbox = position)
    # im.show()
    # THIS IS TEST CODE TO TUNE THE "BOX"

    # rect = win32gui.GetWindowRect(global_window_handle)
    # position = missionOverBox(rect)
    # im = ImageGrab.grab(bbox = position)
    # im.show()

    # mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), 
    #            rect[1] + (.86 * (rect[3] - rect[1])))

    runCount = 0

    while True:
        rect = win32gui.GetWindowRect(global_window_handle)

        # THESE LINES DEFINE WHICH MAP THIS IS SET FOR
        position = missionOverBox(rect)
        # position = ladourBox(rect)
        # position = ntBox(rect)
        # THESE LINES DEFINE WHICH MAP THIS IS SET FOR

        # Scans left to right, top to bottom, like reading a book
        # for i in range(1):
        im = ImageGrab.grab(bbox = position)

        # width, height = im.size
        for i, pixel in enumerate(im.getdata()):
            if pixel == (2,9,35): #IF SPECIFIC BLUE IS FOUND

                # THE FOLLOWING 2 LINES ARE TEST CODE IF YOU WANT TO SEE THE PHOTO BEING CHECKED
                # im.show()
                # exit()
                # THE ABOVE 2 LINES ARE TEST CODE IF YOU WANT TO SEE THE PHOTO BEING CHECKED

                print('\nRun:', runCount, 'Pixel Found at:', i)


                mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), rect[1] + (.5 * (rect[3] - rect[1]))) # Move mouse to center of Last Cloudia screen
                print("Moved Mouse to center of \"Last Cloudia\" screen")
                time.sleep(5)

                mouse.click() # Click off "RESULT - Summary" screen
                print("Clicked on \"RESULT - Summary\" screen")
                time.sleep(1.8)

                mouse.click() # Click off "RESULT - EXP" screen
                time.sleep(.8)
                mouse.click() # Click off "RESULT - EXP" screen for a 2nd time, as it takes 2 clicks for some reason ...
                print("Clicked on \"RESULT - EXP\" screen")
                time.sleep(1.8)

                mouse.click() # Click off "RESULT - Sub Ark" screen
                print("Clicked on \"RESULT - Sub Ark\" screen")
                time.sleep(1.8)

                mouse.move(rect[0] + (.67 * (rect[2] - rect[0])), rect[1] + (.64 * (rect[3] - rect[1]))) # Move mouse to "YES" button
                time.sleep(.25)
                mouse.click() # Click "YES" button to replay the quest
                print("Clicked \"Yes\"")
                time.sleep(1.8)

                mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), rect[1] + (.86 * (rect[3] - rect[1]))) # Move mouse to "START QUEST" button
                print("Moved mouse to \"Start Quest\" button")
                time.sleep(1)

                mouse.click() # Click "START QUEST" button
                print("Clicked \"START QUEST\", sleeping for 20 seconds")
                time.sleep(20) # Sleep for 15 seconds to allow next mission to start and complete
                print("Slept for 20 seconds, searching")
                



                runCount = runCount + 1
                break # Exit closest 'for' loop, return to looking for next caught fish