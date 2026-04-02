from PIL import ImageGrab
import datetime
import os

capture_path = "./results/screenshot.png"
full_capture_path = "./results/screenshot_full.png"
results_path = "./results"
def capture_full_screen():
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    screenshot = ImageGrab.grab()

    screenshot.save(full_capture_path, "PNG")
    print(f"Screenshot saved in {full_capture_path}")
    return screenshot
def capture_region(left,top,right,down):
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    bbox = (left,top,right,down)
    screenshot = ImageGrab.grab(bbox)
    screenshot.save(capture_path, "PNG")
    print(f"Região capturada")
    return screenshot
