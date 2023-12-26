import glob
import cv2
import os
import random

label_path = 'datasets/data/*.txt'
label_files = glob.glob(label_path)

#convert png image to jpg
png_image_path = 'datasets/data/*.png'
png_image_paths = glob.glob(png_image_path)
for path in png_image_paths:
  print(path)
  image = cv2.imread(path)
  os.remove(path)
  cv2.imwrite(path.replace("png","jpg"),image)

#check image fauld
for label_file in label_files:
  im = cv2.imread(label_file.replace("txt", "jpg"))
  if im is None:
    label_files.remove(label_file)
    print(f"Remove file {label_file}")
    # raise FileNotFoundError(f"Image Not Found {label_file}")

random.seed(43)
random.shuffle(label_files)

# Calculate number of files for training, validation
data_size = len(label_files)
train_size = int(data_size * 0.8)

train_txt_paths = label_files[:train_size]
valid_txt_paths = label_files[train_size:]

# print(valid_txt_paths)

t = open("datasets/train.txt", "w")
for train_txt_path in train_txt_paths:
  t.write(train_txt_path.replace("/content/", "").replace("txt", "jpg") + "\r\n")
t.close()

v = open("datasets/val.txt", "w")
for valid_txt_path in valid_txt_paths:
  v.write(valid_txt_path.replace("/content/", "").replace("txt", "jpg") + "\r\n")
v.close()

classes = open("datasets/classes.txt", "r")
classes = classes.readlines()

class_index = open("datasets/classes_index.txt", "w")
indx = 0
for classname in classes:
  class_index.write(f"{indx}: {classname}")
  indx += 1
class_index.close()