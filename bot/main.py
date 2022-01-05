import threading
import time
import pyautogui
last_box = None


def shoot(n=0.2):
    while True:
        pyautogui.click()
        pyautogui.press('space')
        time.sleep(0.4)
        pyautogui.click()


def dodge_right():
    for _ in range(1, 110):
        pyautogui.press("right")
        time.sleep(0.01)


def dodge_left():
    for _ in range(1, 110):
        pyautogui.press('left')
        time.sleep(0.01)


def dodge(n=0.2):
    global last_box
    while True:
        pocisk_list = ["pocisk.png", "pocisk2.png"]
        for pocisk in pocisk_list:
            im = pyautogui.screenshot(region=(10, 750, 1200, 85))
            # im.save(r"C:\Users\pboguski\3\area2.png")
            boxLocation = pyautogui.locateOnScreen(
                'prostokat.png', region=(10, 750, 1200, 825))


thread = threading.Thread(target=shoot, daemon=True)
thread2 = threading.Thread(target=dodge, daemon=True)
time.sleep(1)
pyautogui.press("f5")
thread.start()
time.sleep(1500)
