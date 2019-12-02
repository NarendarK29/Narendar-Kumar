# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:31:24 2019

@author: Lenovo
"""
import struct
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data():
    with open("train-labels-idx1-ubyte.gz","rb") as labels:
        magic,n = struct.unpack(">II",labels.read(8))
        train_labels = np.fromfile(labels, dtype = np.uint8)
    with open("train-images-idx3-ubyte.gz","rb") as imgs:
        magic, num, nrows, ncols = struct.unpack(">IIII",imgs.read(16))
        train_images = np.fromfile(imgs,dtype=np.uint8).reshape(num,784)
    with open("t10k-labels-idx1-ubyte.gz","rb") as labels:
        magic,n = struct.unpack(">II",labels.read(8))
        test_labels = np.fromfile(labels, dtype = np.uint8)
    with open("t10k-images-idx3-ubyte.gz","rb") as imgs:
        magic, num, nrows, ncols = struct.unpack(">IIII",imgs.read(16))
        test_images = np.fromfile(imgs,dtype=np.uint8).reshape(num,784)
    return train_images,train_labels, test_images,test_labels
def visualize_data(img_array,label_array):
    fig, ax = plt.subplots(nrows = 8, sharex = True, sharey = True)
    ax = ax.flatten()
    for i in range(64):
        img = img_array(lable_array==9)[i].reshape(28,28)
        ax[i].imshow(img,cmap = "Greys", interpolation = "nearest")
    plt.show()
train_x,train_y,test_x,train_y = load_data()
visualize_data[train_x,train_y]
    
        