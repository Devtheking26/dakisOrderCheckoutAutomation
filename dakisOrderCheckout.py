import pyautogui 
import time
import pygetwindow as gw
import pyscreeze 

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
    i = 0
    while i < 4:
        time.sleep(2)
        pos = pyautogui.position()
        print(pos)
        i = i+1

def create_screenshot():
    time.sleep(3)
    screenshot = pyautogui.screenshot('AccutermImage.png')
    
def open_accuterm():

    #img1 = pyautogui.screenshot('bro.png',region=[1095,1030,44,50]) How to create an image that is searchable. (I think the screenshot data is transferred correctly using this)   
    pyautogui.press('win')
    time.sleep(.3)
    pyautogui.write('Accuterm 7')
    time.sleep(.1)
    pyautogui.press('enter')
    time.sleep(1)
 #   accutermLocation = pyautogui.locateOnScreen('AccutermImage.png')
 #   accutermCenter= pyautogui.center(accutermLocation)
 #   pyautogui.click(accutermCenter.x, accutermCenter.y)

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

def test_list():
    orders = set()
    order = input("scan order num\n")
    while order.lower() != "n":
        orders.add(order)
        order = input("scan order num\n")

    return orders

def get_id():
    correctID = False
    user_id = input("Enter your user ID with a B at the end: ")
    while not correctID:
        id_length = len(user_id) 

        if id_length != 5:
            user_id =input("Please enter a correct id. (ie : 1452b) ")
        else:
            correctID = True

    return user_id

def multi_order_checkout():
    dakis_order_list = set()
    accuTerm_order_list = set()
    user_id = get_id()
        
    order_number = input("\nScan OrderNumber: ")
    while order_number.lower() != "n":
        
        if(order_number[0] == "."):
            accuTerm_order_list.add(order_number)

        elif len(order_number) == 8 and int(order_number) > 40000000:
            dakis_order_list.add(order_number)

        else:
            print("Incorrect order #. Please make sure you are using the correct order number.")
        order_number = input("Next Order Number (If finished press n ): ")

    for dakis_order in dakis_order_list:
        checkout_orders(dakis_order)
        #time.sleep(1)
    bag_checkout(accuTerm_order_list, user_id)

def bag_checkout(order_list, user_id):
    open_accuterm()

    if(user_id != None):
        pyautogui.write(user_id)
        pyautogui.press('enter')
            
        time.sleep(2)
        for order in order_list:
                pyautogui.write(order)
                time.sleep(.5)
                pyautogui.press('enter')
        time.sleep(.5)
        pyautogui.write('0')
        pyautogui.press('enter')
        pyautogui.alert(text="DONE!!!!")
            
def checkout_assist(order_number):
    open_find() #open find menu 
    time.sleep(.2)
    pyautogui.write(order_number) #Input order number
    pyautogui.press('enter') #press enter
    time.sleep(.4)
    mark_order() #Open mark order menu
    mark_as_done() #Click done button
    correctWindow = getActiveWindow()

def checkout_orders(order_number):
    open_find() #open find menu 
    time.sleep(.2)
    pyautogui.write(order_number) #Input order number
    pyautogui.press('enter') # DUH
    time.sleep(.4)
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
                checkout_assist(order_number)
                
            else:
                break
    no_button()

def main():
    multi_order_checkout()
    #testIO() 

if __name__ == '__main__':
    main()
