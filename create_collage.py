#!/usr/bin/python

# Martin Kersner, m.kersner@gmail.com
# 2015/12/14

from Collage import *
from Dataset import *

def main():
    img_path     = "lena.png"
    dataset_path = "/home/martin/datasets/flickr-dataset/20x20"
    dataset_csv  = "dataset.csv"

    dataset = Dataset(dataset_path)
    #dataset.create()
    file_paths, rgb_means = dataset.load(dataset_csv)

    collage = Collage(img_path, dataset_path, file_paths, rgb_means)
    img_collage = collage.create()
    io.imsave("collage.png", img_collage)

if __name__ == "__main__":
    main()
