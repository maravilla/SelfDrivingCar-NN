import numpy as np
import matplotlib.pyplot as plt
import PIL
import cv2
import csv, glob, os

def imageToHSV (image):
    resized = cv2.resize((cv2.cvtColor(image, cv2.COLOR_RGB2HSV))[:, :, 1], (img_cols, img_rows))
    return resized

img_rows = 64
img_cols = 64
data_folder = '/Users/emaravilla/Documents/School/Testing/'
log_path = data_folder + 'driving_log.csv'
folder_path = data_folder + 'IMG/'
save_path = data_folder + 'Reduced/'

logs = []

# load logs
with open(log_path, 'rt') as f:
    reader = csv.reader(f)
    for line in reader:
        logs.append(line)
    log_labels = logs.pop(0)

# Center
for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = imageToHSV(img)
    new_path = save_path + 'center' + logs[i][0].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path, newImg, cmap='viridis')
    print("Saving processed image..", new_path)
    
# Left
for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = imageToHSV(img)
    new_path = save_path + 'le' + logs[i][1].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path, newImg, cmap='viridis')
    print("Saving processed image..", new_path)

# Right
for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = imageToHSV(img)
    new_path = save_path + 'right' + logs[i][2].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path, newImg, cmap='viridis')
    print("Saving processed image..", new_path)
