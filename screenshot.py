from PIL import ImageGrab
import datetime
import os

capture_path = "./results/screenshot.png"
def capture_full_screen():
    if not os.path.exists(capture_path):
        os.makedirs(capture_path)
    screenshot = ImageGrab.grab()

    screenshot.save(capture_path, "PNG")
    print(f"Screenshot saved in {capture_path}")
    return screenshot
def capture_region(left, top,right,down):
    if not os.path.exists(capture_path):
        os.makedirs(capture_path)
    bbox = (top,left,right,down)
    screenshot = ImageGrab.grab(bbox)
    screenshot.save(capture_path, "PNG")
    print(f"Região capturada")
    return screenshot
