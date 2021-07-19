import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(250, 300):
        for j in range(410, 563):
            if data[i, j] > 100:
                hit("down")
                return

    for i in range(300, 350):
        for j in range(563, 650):
            if data[i, j] > 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Dino game will start in 3 seconds")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

