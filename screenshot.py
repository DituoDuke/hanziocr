from PIL import ImageGrab
import datetime
import os
import sys
import screeninfo
from screeninfo import get_monitors
monitor = get_monitors()[0]

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
capture_path = os.path.join(BASE_DIR, "results", "screenshot.png")
full_capture_path = os.path.join(BASE_DIR, "results", "screenshot_full.png")
results_path = os.path.join(BASE_DIR, "results")
def capture_full_screen():
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    bbox = (0,0,monitor.width,monitor.height)
    screenshot = ImageGrab.grab(bbox)

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
