import pyautogui # type: ignore
import time
import pygetwindow as gw    # type: ignore

def printWindowList():
    windList = gw.getAllTitles()
    print(windList)

def testIO():
    order_list = set()
    order_number = input("Scan OrderNumber: ")
    while order_number.lower() != "n":
        if len(order_number) == 8 and order_number[0] != "." and int(order_number) > 40000000:
            order_list.add(order_number)
        else:
            print("Incorrect order #. Please make sure you are using the correct dakis number and not a bag number.")
        order_number = input("Next Order Number (If finished press n ): ")

    for order in order_list:
        print(order)
        #time.sleep(1)


def getActiveWindow():
    WindowName ='Dakis Job Downloader'
    currentWindow = gw.getActiveWindowTitle()
    if WindowName == currentWindow:
        return True
    else:
        return False      

def get_cursor_coords():
    ans = input("Ready for coordinates? (Y/N) ")
    while ans.lower() == "y":
        print("Mouse coordinates:", pyautogui.position())
        ans = input("Enter another variable? (Y/N)\n")

def open_find():
    pyautogui.click(x=1371, y=51)

def mark_order():
    pyautogui.click(x=796, y=43)

def mark_as_done():
    pyautogui.click(x=819, y=83)

def no_button():
    pyautogui.click(x=1158, y=551)

def scanner_in():
    order_num = input("Enter order number: ")
    print(order_num)

def multi_order_checkout():
    order_list = set()
    order_number = input("Scan OrderNumber: ")
    while order_number.lower() != "n":
        if len(order_number) == 8 and order_number[0] != "." and int(order_number) > 40000000:
            order_list.add(order_number)
        else:
            print("Incorrect order #. Please make sure you are using the correct dakis number and not a bag number.")
        order_number = input("Next Order Number (If finished press n ): ")

    for order in order_list:
        checkout_orders(order)
        #time.sleep(1)

def checkout_orders(order_number):
    open_find() #open find menu 
    time.sleep(.2)
    pyautogui.write(order_number) #Input order number
    pyautogui.press('enter') # DUH
    time.sleep(1.4)
    mark_order() #Open mark order menu
    #time.sleep(0.5)
    mark_as_done() #Click done button
    #time.sleep(3)
    correctWindow = getActiveWindow() # verify that dakis window is open 
    delay = 0 #initalize delay veriable menu
	
    while not correctWindow:
        correctWindow = getActiveWindow() #Wait for the "Dakis Job Downloader" (aka send email notification window) to open.
        time.sleep(.5)
        delay = delay + 1
        if(delay >= 10): #if the window does not open the email message. 
            input = pyautogui.confirm(text="Program cannot find email window or the correct order.\nTo retry press ok. Make sure the email window is opened and on top.\nPress cancel to move to next the order number if problem persists.", title='Program Error', buttons=['Ok','Cancel'])
            if input == 'Ok':
                delay = 5
            else:
                break
    no_button()

def main():
    multi_order_checkout()
    #testIO() 

if __name__ == '__main__':
    main()
