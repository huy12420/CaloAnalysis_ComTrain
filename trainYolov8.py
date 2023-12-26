#copy file modules.py from sourceLayout to ultralytics/ultralytics/nn
#cp -R sourceLayout/modules.py ultralytics/ultralytics/nn/

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="calo.yaml", epochs=300, imgsz=416)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("datasets/data/0000000.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format
