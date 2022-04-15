import subprocess
import os
os.chdir("/Users/nicholas717/Downloads/code/YOLO/darknet")

file_path = "/Users/nicholas717/Downloads/YOLO/Butterfly/test/google18.jpg"

subprocess.run(["./darknet" ,"detector", "test", "/Users/nicholas717/Downloads/code/YOLO/cfg/class.data",  "/Users/nicholas717/Downloads/code/YOLO/cfg/yolov4-tiny-custom.cfg", "/Users/nicholas717/Downloads/code/YOLO/cfg/weights/1.weights", file_path, "-i", "0", "-thresh 0.25"])

from PIL import Image

img = Image.open("predictions.jpg")
img.show()