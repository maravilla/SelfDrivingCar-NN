import numpy as np
import matplotlib.pyplot as plt
import cv2
import csv, glob, os
import PIL

img_rows = 64
img_cols = 64

data_folder = '/Users/emaravilla/Documents/School/Testing/'

def image_preprocessing(img):
    resized = cv2.resize((cv2.cvtColor(img, cv2.COLOR_RGB2HSV))[:, :, 1], (img_cols, img_rows))
    return resized

#load data

print("loading data...")

log_path = data_folder + 'driving_log.csv'
folder_path = data_folder + 'IMG/'
save_path = data_folder + 'Reduced/'

log_path = data_folder + 'driving_log.csv'
logs = []

# load logs
with open(log_path, 'rt') as f:
    reader = csv.reader(f)
    for line in reader:
        logs.append(line)
    log_labels = logs.pop(0)

for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = image_preprocessing(img)
    new_path = save_path + 'center' + logs[i][0].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path, newImg, cmap='viridis')
    print("Saving processed image..",new_path)

for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = image_preprocessing(img)
    new_path = save_path + 'le' + logs[i][1].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path,newImg,cmap='viridis')
    print("Saving processed image..",new_path)

for i in range(len(logs)):
    img_path = logs[i][0]
    img_path = data_folder + 'IMG' + (img_path.split('IMG')[1]).strip()
    img = plt.imread(img_path)
    newImg = image_preprocessing(img)
    new_path = save_path + 'right' + logs[i][2].strip('Users/emaravilla/Documents/School/Testing/IMG/') + 'g'
    plt.imsave(new_path,newImg,cmap='viridis')
    print("Saving processed image..",new_path)