import pyautogui 
import time
import pygetwindow as gw
import pyscreeze
import winsound

class WindowNotFound(Exception):
    pass

def total_count(count): #counts all orders checkout using program ERROR No Such directory.
    
    with open("total_orders",'r+') as f3:
        current_num = f3.read()
        if current_num == "":
            f3.write(str(count))
            f3.truncate()
            
        else:
            total = int(count) + int(current_num)
            f3.seek(0)
            f3.write(str(total))
            f3.truncate()

def write_backup_files(dakisList, accutermList): #Can be directly imported to the program.
    f1 = open("accuterm_backup",'w')
    f2 = open("dakis_backup",'w')
    count = 0


    for order in dakisList:
        order = order +'\n'
        f2.write(order)
        count+=1

    for order in accutermList:
        order = order +'\n'
        f1.write(order)
        count+=1
    f1.close()
    f2.close()
    
    #total_count(count) Currently broken

def select_function():
    user_id = get_id()
    valid_choice = False
    file_choice = input("Select a operation type:\n\nPress Enter for Standard Operation.\n\nPress 2 for accuterm backup only.\nPress 0 to cancel. \n\nEnter Selection: ")
    
    while not valid_choice:
        if file_choice == '': #Standard order operation
            valid_choice = True
            multi_order_checkout(user_id)
            
        elif file_choice == '2': #Accuterm backup proccess
            valid_choice = True
            blist = get_list("accuterm_backup")

            if len(blist) > 0:
                bag_checkout(blist, user_id)
                print("Choice 3: ", blist)
            else:
                print('Accuterm backup is empty')

        elif file_choice == '3': #Dakis backup proccess
            valid_choice = True
            blist = get_list("dakis_backup")

            if len(blist) > 0:
                archive_dakis_checkout(blist)
                print("Choice 3: ", blist)
            else:
                print('Dakis backup is empty')
                
        elif file_choice == '0':
            #get_cursor_coords()
            valid_choice = True
            
        elif file_choice == "4":
            valid_choice = True
            print(getWindowList())

        elif file_choice == 'E':
            valid_choice = True
            break
	
        else: #User input incorrect
            file_choice = input("Select a operation type:\n\nPress Enter for Standard Operation.\n\nPress 2 for accuterm backup only.\nPress 0 to cancel. \n\nEnter Selection: ")

def get_list(fileName):
    new_list = set()
    f = open(str(fileName),"r")
    for line in f:
        new_list.add(line[:-1])
    return new_list

def getWindowList():
    windList = gw.getAllTitles()
    return windList

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

def get_cursor_coords(): #gets X,Y Coordinates of the cursors current location
    i = 0
    while i < 4:
        time.sleep(2)
        pos = pyautogui.position()
        print(pos)
        i = i+1

def create_screenshot(): #Captures a screenshot of the screen
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
    pyautogui.click(x=1375, y=48) #x=1371, y=51 og

def mark_order():
    pyautogui.click(x=796, y=43)

def mark_as_done():
    pyautogui.click(x=819, y=83)

def get_dakis_window():
    currentWindow = gw.getActiveWindow().title    
    found = False
    for i in range(10):
        if currentWindow[0:20] == 'Dakis Job Downloader':
            print("Deez")
            found = True
            break
        else:
            pyautogui.keyDown('alt')
            pyautogui.press('tab',presses=i)
            pyautogui.keyUp('alt')
        currentWindow = gw.getActiveWindow().title

    if not found:

        input = pyautogui.confirm(text="Cannot find Dakis Window. Open Dakis and Click Ok", title='Program Error', buttons=['Ok','Cancel'])

        if input == "ok":
            get_dakis_window()      
            
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
            user_id = input("Please enter a correct id. (ie : 1452b) ")
        else:
            correctID = True

    return user_id

def archive_dakis_checkout(list):
    for dakis_order in list:
        checkout_orders(dakis_order)
        #time.sleep(1)

def multi_order_checkout(user_id):
    dakis_order_list = set()
    accuTerm_order_list = set()
        
    order_number = input("\nScan OrderNumber: ")
    while order_number.lower() != "n":
        
        if(order_number == '' or len(order_number)<7):
            print("Please enter a correct value\n")
        
        elif(order_number[0] == "." and str(order_number[2]) == '1'):
            accuTerm_order_list.add(order_number)

        elif order_number[0] == "." and str(order_number[2]) != '1':
            winsound.PlaySound('alert.wav',winsound.SND_FILENAME)
            ans = pyautogui.confirm(text="This order belongs to a different store. Are you sure you want to check it out?", title='Wrong Store Error', buttons=['Yes','No'])
            
            if ans == 'Yes':
                accuTerm_order_list.add(order_number)

        elif len(order_number) == 8 and int(order_number) > 40000000:
            dakis_order_list.add(order_number)

        else:
            print("Incorrect order #. Please make sure you are using the correct order number.")

        order_number = input("Next Order Number (If finished press n ): ")
    
    write_backup_files(dakis_order_list,accuTerm_order_list)

    for dakis_order in dakis_order_list:
        checkout_orders(dakis_order)
        #time.sleep(1)
    if(len(accuTerm_order_list) > 0):
        bag_checkout(accuTerm_order_list, user_id)  

def bag_checkout(order_list, user_id):
    open_accuterm()

    if(user_id != None):
        pyautogui.write(user_id)
        pyautogui.press('enter')
            
        time.sleep(2)
        for order in order_list:
                pyautogui.write(order)
                #time.sleep(.5)
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
    get_dakis_window()

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
    #get_cursor_coords()
    select_function()
if __name__ == '__main__':
    main()
