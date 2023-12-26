# copy file modules.py from customLayout to ultralytics/ultralytics/nn
#
# cp -R customLayout/modules.py ultralytics/ultralytics/nn/

# yolo task=detect mode=export model=ultralytics/runs/detect/train/weights/best.pt format=onnx simplify=True opset=13 imgsz=416