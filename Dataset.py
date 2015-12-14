#!/usr/bin/python

# Martin Kersner, m.kersner@gmail.com
# 2015/12/14

import os
import pandas as pd
import numpy as np
from skimage import io

class Dataset:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.ext = [".png", ".jpg"]
        self.delimiter = ","

    def create(self):
        for filename in os.listdir(self.dataset_path):
            if self.is_image(filename):
                img_path = os.path.join(self.dataset_path, filename)
                img = io.imread(img_path)
                
                R, G, B = self.compute_mean(img)
                self.print_line(filename, R, G, B) 

    def is_image(self, filename):
        if filename.endswith(tuple(self.ext)):
            return True
        else:
            return False

    def print_line(self, filename, R, G, B):
        print filename + self.delimiter + str(R) + self.delimiter + str(G) + self.delimiter + str(B)

    def compute_mean(self, img):
        if (self.is_grayscale(img)):
            R_med = G_med = B_med = int(np.median(img))
        else:
            R_med = int(np.median(img[:,:,0]))
            G_med = int(np.median(img[:,:,1]))
            B_med = int(np.median(img[:,:,2]))
        
        return R_med, G_med, B_med

    def is_grayscale(self, img):
        if (len(img.shape) == 2):
            return True
        else:
            return False

    def load(self, csv_path):
        data = pd.read_csv(csv_path, names=["file_path", "r", "g", "b"], header=None)
        self.file_paths = data["file_path"]
        self.rgb_means  = data[["r", "g", "b"]]

        return self.file_paths, self.rgb_means
