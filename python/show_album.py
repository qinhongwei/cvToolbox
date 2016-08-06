# -*- coding: utf-8 -*-
import argparse
import os
import time
import random
from PIL import Image
import subprocess
import psutil
import matplotlib.pyplot as plt
def showAlbum(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        #print path
        if os.path.isdir(path):
            showAlbum(path)
        else:
            #a = random.sample(range(100), 1)
            #if path[-4:] == '.jpg' and a == [1]:
            if path[-4:] == '.jpg':
                print path
                img = Image.open(path)
                ####plt.imshow(img)
                ####plt.show()
                img.show()
                ####os.system('xdg-open ' + path)
                time.sleep(1)
                # hide image
                for proc in psutil.process_iter():
                    if proc.name() == "display":
                        proc.kill()
def main(image_folder):
    showAlbum(image_folder)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='show jpg images in folder.')
    parser.add_argument(
        'image_folder', help='the image folder you\'d like to show.')

    args = parser.parse_args()
    main(args.image_folder)
