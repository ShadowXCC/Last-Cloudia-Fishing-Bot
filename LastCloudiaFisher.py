#https://humanbenchmark.com/tests/aim

import time
from PIL import ImageGrab
import mouse
import win32gui #pip install pywin32
#dark blue color 29,67,97
# != 34,108,167

# X/Width = 780; Y/Height = 275

# Monitor
# width = 2560 
# height = 1440 

# for i in range(1):
#     im = ImageGrab.grab()
#     im.show()
#     for :
#         for :

# global_x = 0
# global_y = 0
# global_w = 0
# global_h = 0
global_window_handle = 0

def findWindow():
    win32gui.EnumWindows(callback, None)

    # print(windowHandle)

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    # x = rect[0]
    # y = rect[1]
    # w = rect[2] - x
    # h = rect[3] - y
    if "Last Cloudia" == win32gui.GetWindowText(hwnd):
        # global global_x
        # global global_y
        # global global_w
        # global global_h
        global global_window_handle

        # global_x = rect[0]
        # global_y = rect[1]
        # global_w = rect[2] - rect[0]
        # global_h = rect[3] - rect[1]
        global_window_handle = hwnd
        print("Window %s:" % win32gui.GetWindowText(hwnd))
        print(hwnd)
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

if __name__ == '__main__':
    findWindow()

    # THIS IS TEST CODE TO TUNE THE "BOX"
    # position = ladourBox()
    # position = ntBox()

    # im = ImageGrab.grab(bbox = position)
    # im.show()
    # THIS IS TEST CODE TO TUNE THE "BOX"

    runCount = 0

    # global global_x
    # global global_y
    # global global_w
    # global global_h

    while True:
        rect = win32gui.GetWindowRect(global_window_handle)

        # global_x = rect[0]
        # global_y = rect[1]
        # global_w = rect[2] - rect[0]
        # global_h = rect[3] - rect[1]

        # position = ladourBox(rect)
        position = ntBox(rect)

        # Scans left to right, top to bottom, like reading a book
        for i in range(1):
            im = ImageGrab.grab(bbox = position)

            # im = ImageGrab.grab(bbox =(210, 425, 230, 475)) # This is the box for "Fishing Spot" next to Ladour
            # im = ImageGrab.grab(bbox =(210, 530, 230, 550)) # This is the box for "Fishing Spot" next to Nameless Town
            # im.show()
            # width, height = im.size
            for i, pixel in enumerate(im.getdata()):
                if pixel == (255,255,255): #IF WHITE IS FOUND

                    # THE FOLLOWING 2 LINES ARE TEST CODE IF YOU WANT TO SEE THE PHOTO BEING CHECKED
                    # im.show()
                    # exit()

                    print('RunCount:', runCount, i, pixel)

                    # mouse.click()
                    # im.show()
                    # a = a + 1
                    # break

                    # This is the code that automates clicking
                    # CLICK "REEL IN"
                    mouse.click()

                    # WAIT FOR FISH TO BE REELED IN
                    time.sleep(3.6) #Big "Megrona Whale" take a long time to reel in, 3.5 seconds is less time than it takes

                    # CLICK "CLOSE" ON CAUGHT FISH PAGE
                    mouse.click()

                    # Wait for 
                    time.sleep(.5) #1.4 worked 100% over 100's (500+) of runs

                    #CLICK "CAST OUT"
                    mouse.click()
                    runCount = runCount + 1
                    break