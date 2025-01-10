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

#This is the math for "Fishing Spot" next to Ladour
def ladourBox(rect):
    window_x = rect[0]
    window_y = rect[1]
    window_w = rect[2] - rect[0]
    window_h = rect[3] - rect[1]

    x = window_x + (.31 * window_w)
    y = window_y + (.4 * window_h)
    x2 = (window_x + window_w) - (.68 * window_w)
    y2 = (window_y + window_h) - (.59 * window_h)

    return (x, y, x2, y2)

#This is the math for "Fishing Spot" next to Nameless Town
def ntBox(rect):
    window_x = rect[0]
    window_y = rect[1]
    window_w = rect[2] - rect[0]
    window_h = rect[3] - rect[1]

    x = window_x + (.29 * window_w)
    y = window_y + (.50 * window_h)
    x2 = (window_x + window_w) - (.7 * window_w)
    y2 = (window_y + window_h) - (.49 * window_h)

    return (x, y, x2, y2)

def zardBox(rect):
    window_x = rect[0]
    window_y = rect[1]
    window_w = rect[2] - rect[0]
    window_h = rect[3] - rect[1]

    x = window_x + (.29 * window_w)
    y = window_y + (.567 * window_h)
    x2 = (window_x + window_w) - (.69 * window_w)
    y2 = (window_y + window_h) - (.422 * window_h)

    return (x, y, x2, y2)

def NEW_Box(rect):
    window_x = rect[0]
    window_y = rect[1]
    window_w = rect[2] - rect[0]
    window_h = rect[3] - rect[1]

    x = window_x + (.0 * window_w)
    y = window_y + (.0 * window_h)
    x2 = (window_x + window_w) - (.0 * window_w)
    y2 = (window_y + window_h) - (.0 * window_h)

    return (x, y, x2, y2)


if __name__ == '__main__':
    findWindow()

    # THIS IS TEST CODE TO TUNE THE "BOX"
    # position = ladourBox()
    # position = ntBox()
    # rect = win32gui.GetWindowRect(global_window_handle)
    # position = zardBox(rect)

    # im = ImageGrab.grab(bbox = position)
    # im.show()
    # exit()
    # THIS IS TEST CODE TO TUNE THE "BOX"

    runCount = 0

    print("Make sure the Last Cloudia window is open and visible on your main monitor")
    print("Starting bot in 5 seconds")
    time.sleep(.5)
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

    print("Moving mouse to \"Cast Out\" button")
    rect = win32gui.GetWindowRect(global_window_handle)
    mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), rect[1] + (.80 * (rect[3] - rect[1]))) # Move mouse to "Cast Out" button

    print("Clicking \"Cast Out\"")
    mouse.click()

    while True:
        rect = win32gui.GetWindowRect(global_window_handle)

        # THESE LINES DEFINE WHICH MAP THIS IS SET FOR
        # position = ladourBox(rect)
        # position = ntBox(rect)
        position = zardBox(rect)
        # THESE LINES DEFINE WHICH MAP THIS IS SET FOR

        # Scans left to right, top to bottom, like reading a book
        # for i in range(1):
        im = ImageGrab.grab(bbox = position)

        # width, height = im.size
        for i, pixel in enumerate(im.getdata()):
            if pixel == (255,255,255): #IF WHITE IS FOUND

                # THE FOLLOWING 2 LINES ARE TEST CODE IF YOU WANT TO SEE THE PHOTO BEING CHECKED
                # im.show()
                # exit()
                # THE ABOVE 2 LINES ARE TEST CODE IF YOU WANT TO SEE THE PHOTO BEING CHECKED

                print('\nRun:', runCount, 'Pixel Found at:', i)

                print(runCount, "Moving mouse to \"Reel In\" button")
                rect = win32gui.GetWindowRect(global_window_handle)
                mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), rect[1] + (.80 * (rect[3] - rect[1]))) # Move mouse to "Reel In" button

                # This is the code that automates clicking
                # CLICK "REEL IN"
                mouse.click()
                print(runCount, 'Clicked Reel In')

                # WAIT FOR FISH TO BE REELED IN
                print(runCount, 'Waiting for fish to be reeled in')
                time.sleep(6.7) #Big "Megrona Whale" take a long time to reel in, after a lot of testing 6.75 seems good and 6.5 caused issues on NT

                # CLICK "CLOSE" ON CAUGHT FISH PAGE
                mouse.click()
                print(runCount, 'Clicked Close')

                # Wait for 
                print(runCount, 'Waiting for screen change')
                time.sleep(.3) # .25 seems safe, but stick with .3 in case of slower PCs

                print(runCount, "Moving mouse to \"Cast Out\" button")
                rect = win32gui.GetWindowRect(global_window_handle)
                mouse.move(rect[0] + (.5 * (rect[2] - rect[0])), rect[1] + (.80 * (rect[3] - rect[1]))) # Move mouse to "Cast Out" button

                #CLICK "CAST OUT"
                mouse.click()
                print(runCount, 'Clicked Cast Out')



                runCount = runCount + 1
                break # Exit closest 'for' loop, return to looking for next caught fish