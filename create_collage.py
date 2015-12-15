#!/usr/bin/python

# Martin Kersner, m.kersner@gmail.com
# 2015/12/14

from Collage import *
from Dataset import *

def main():
    img_path     = "lena.png"
    dataset_path = "/home/martin/datasets/flickr/thumbnails"
    dataset_csv  = "dataset.csv"
    block_size   = 64

    dataset = Dataset(dataset_path)
    #dataset.create()
    file_paths, rgb_means = dataset.load(dataset_csv)

    collage = Collage(img_path, file_paths, rgb_means, block_size)
    img_collage = collage.create()
    io.imsave("collage.png", img_collage)

if __name__ == "__main__":
    main()
