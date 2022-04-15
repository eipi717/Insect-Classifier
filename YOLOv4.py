import subprocess
import os

def YOLOLocaliser(image_path):
    os.chdir("/Users/nicholas717/Downloads/FYP9Apr/code/YOLO/darknet")

    data = "/Users/nicholas717/Downloads/FYP9Apr/code/YOLO/cfg/class.data"
    cfg = "/Users/nicholas717/Downloads/FYP9Apr/code/YOLO/cfg/yolov4-tiny-custom.cfg"
    weights = "/Users/nicholas717/Downloads/FYP9Apr/code/YOLO/cfg/weights/2.weights"

    subprocess.run(["./darknet" ,"detector", "test", data,  cfg, weights, image_path, "-i", "0", "-thresh 0.25"])
