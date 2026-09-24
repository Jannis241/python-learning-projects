import os
import pyautogui
from datetime import datetime

def get_unique_filename(base_path, base_name, extension):
    counter = 1
    file_path = f"{base_path}/{base_name}{extension}"
    while os.path.exists(file_path):
        file_path = f"{base_path}/{base_name}_{counter}{extension}"
        counter += 1
    return file_path

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

current_time = datetime.now().strftime("%H-%M-%S")
base_name = f"screenshot_{current_time}"
extension = ".png"
file_path = get_unique_filename("screenshots", base_name, extension)

screenshot = pyautogui.screenshot()
screenshot.save(file_path)

print(f"Screenshot gespeichert unter: {file_path}")
