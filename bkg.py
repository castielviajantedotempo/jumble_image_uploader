import select_file_from_folder as sel
import time
import datetime
from datetime import datetime as dt
from PIL import Image
from PIL import UnidentifiedImageError
import os
import subprocess

def is_image_pillow(filepath):
    try:
        Image.open(filepath)
        return True
    except UnidentifiedImageError:
        return False
    except Exception as e: # Catch other potential errors during opening
        print(f"An error occurred: {e}")
        return False

def sharp_time():
    while True:
        expected_hour = 10
        expected_minute = 00
        current_time = time.strftime("%Y%m%d-%H%M%S")
        date_format = '%Y%m%d-%H%M%S'
        d1 = dt.strptime(current_time, date_format)
        times = d1.time()
        picture = ""
        message = "" #put your personal message here!
        if times.hour == expected_hour:
            if times.minute == expected_minute:
                picture = sel.get_random_file("C:/Users/random_gui/Pictures")
                if is_image_pillow(picture):
                    print("It's an image!")
                else:
                    for i in range(10):
                        picture = sel.get_random_file("C:/Users/random_gui/Pictures")
                        if is_image_pillow(picture):
                            break
                exit_code =subprocess.run(["upload_image.sh", picture, message])
                print("Exit Code:", exit_code)
                
        time.sleep(60) #seconds

sharp_time()
