import threading, time
import pyautogui
last_box = None
def shoot(n=0.2):
    while True:
        pyautogui.press("space")
        time.sleep(n)
def dodge_right():
    for _ in range(1,110):
        pyautogui.press("right")
        time.sleep(0.01)
def dodge_left(): 
    for _ in range(1,110):
        pyautogui.press('left')
        time.sleep(0.01)
def dodge(n = 0.2):
    global last_box
    while True:
        pocisk_list = ["pocisk.png", "pocisk2.png"]
        for pocisk in pocisk_list:
            im = pyautogui.screenshot(region=(10,750,1200,85))
            # im.save(r"C:\Users\pboguski\3\area2.png")
            boxLocation = pyautogui.locateOnScreen('prostokat.png', region=(10,750,1200,825))
            print(boxLocation)
            if boxLocation == None:
                boxLocation = last_box
            if not boxLocation == None:
                projectileLocation = pyautogui.locateOnScreen(pocisk,region =(boxLocation.left-50, 700, 100,200),confidence=0.1,grayscale=True)
                im = pyautogui.screenshot(region =(boxLocation.left-100, 750, 200,100))
                # im.save(r"C:\Users\pboguski\3\area.png")
                print(projectileLocation)
                if not projectileLocation == None:
                    if(projectileLocation.lef < boxLocation.left):
                        dodge_left()
                    else:
                        dodge_right()
                    break
                last_box = boxLocation
thread = threading.Thread(target=shoot, daemon=True)
thread2 = threading.Thread(target=dodge, daemon=True)
time.sleep(1)
pyautogui.press("f5")
thread.start()
thread2.start()
time.sleep(30)