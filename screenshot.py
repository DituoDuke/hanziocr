from PIL import ImageGrab
import datetime
import os

capture_path = "./screenshots"
def capture_full_screen():
    if not os.path.exists(capture_path):
        os.makedirs(capture_path)
    screenshot = ImageGrab.grab()

    screenshot.save(f"{capture_path}/screenshot.png", "PNG")
    print(f"Screenshot saved in {capture_path}")
    return screenshot
def capture_region(left, top,right,down):
    if not os.path.exists(capture_path):
        os.makedirs(capture_path)
    bbox = (top,left,right,down)
    screenshot = ImageGrab.grab(bbox)
    screenshot.save(f"{capture_path}/screenshot.png", "PNG")
    print(f"Região capturada")
    return screenshot
