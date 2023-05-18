from picamera2 import Picamera2
from libcamera import controls
import time
import os

picam2 = Picamera2()
picam2.options["quality"] = 95 # JPEG quality level, where 0 is the worst quality and 95 is best.

picam2.set_controls({"AwbEnable": True})
picam2.set_controls({"AeEnable": True})
picam2.set_controls({"NoiseReductionMode": controls.draft.NoiseReductionModeEnum.HighQuality})

picam2.start()

# Create a directory named 'images' if it does not exist
if not os.path.exists('images'):
    os.makedirs('images')

# Capture the photo and save it with a name as timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
picam2.capture_file(f"images/{timestamp}.jpg")
