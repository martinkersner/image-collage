#!/usr/bin/python

# Martin Kersner, m.kersner@gmail.com
# 2015/12/14

import numpy as np
import os
from skimage import io
from skimage.transform import downscale_local_mean
from sklearn.metrics import pairwise_distances_argmin_min

class Collage:
    def __init__(self, img_path, data_path, data, filenames):
        self.img = io.imread(img_path)
        self.down_factor = 10
        self.block_size  = 20
        self.data = data
        self.filenames = filenames
        self.data_path = data_path

    def downscale_image(self, img):
        R_down = self.downscale_channel(img[:,:,0])
        G_down = self.downscale_channel(img[:,:,1])
        B_down = self.downscale_channel(img[:,:,2])

        rows, cols = self.get_image_dim(R_down)
        RGB_down = np.zeros((rows, cols, 3), np.uint8)

        RGB_down[..., 0] = R_down
        RGB_down[..., 1] = G_down
        RGB_down[..., 2] = B_down

        return RGB_down

    def downscale_channel(self, channel):
         return downscale_local_mean(channel, (self.down_factor, self.down_factor)).astype(np.uint8)

    def create(self):
        downscaled_img = self.downscale_image(self.img)
        rows, cols = self.get_image_dim(downscaled_img)
    
        collage = np.zeros((self.block_size*rows, self.block_size*cols, 3), np.uint8)

        rr = cc = 0
        for r in range(0, rows):
            for c in range(0, cols):
                pixel = downscaled_img[r,c,:]
                img_block = self.closest_image(pixel)
                collage[rr:rr+self.block_size, cc:cc+self.block_size, :] = img_block

                cc += self.block_size

            cc = 0
            rr += self.block_size

        return collage

    def get_image_dim(self, img):
        img_shape = img.shape
        rows = img_shape[0]
        cols = img_shape[1]

        return rows, cols

    def closest_image(self, pixel):
        index, _ = pairwise_distances_argmin_min(pixel, self.data)

        img_path = os.path.join(self.data_path, self.filenames[index[0]])
        img = io.imread(img_path)

        return img
