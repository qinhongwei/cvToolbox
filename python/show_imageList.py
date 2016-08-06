# -*- coding: utf-8 -*-
import argparse
import os
import time
import random
from PIL import Image
import matplotlib.pyplot as plt
def parse_args():
    """Parse input arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image_list',
        help='image list name')
    parser.add_argument(
        '--image-path', dest='image_path', default='./',
        help='image path')

    args = parser.parse_args()
    return args


def showList(rootDir, listname):
    with open(listname, 'r') as f:
        for line in f:
            line = line.strip('\n')
            path = os.path.join(rootDir, line)
            a = random.sample(range(1000), 1)
            if a == [1]:
            #if path[-4:] == '.jpg':
               print path
               img = Image.open(path)
               ####plt.imshow(img)
               ####plt.show()
               img.show()
               ####os.system('xdg-open ' + path)
               time.sleep(0.3)
def main():
    args = parse_args()
    showList(args.image_path, args.image_list)

if __name__ == '__main__':
    main()
