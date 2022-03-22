import os
from roboflow import Roboflow

rf = Roboflow(model_format="yolov5", notebook="ultralytics")

os.environ["DATASET_DIRECTORY"] = "/Users/albertoharres/datasets"

from roboflow import Roboflow
rf = Roboflow(api_key="75OFN1RCpHsNjcafx1QL")
project = rf.workspace("alberto-harres").project("arche-writing-2")
dataset = project.version(4).download("yolov5")