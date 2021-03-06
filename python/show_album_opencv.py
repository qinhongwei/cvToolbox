# -*- coding: utf-8 -*-
from __future__ import division
import argparse
import os
import random

import cv2
def showAlbum(rootDir, frequency):
    im_index = 0
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        #print path
        if os.path.isdir(path):
            showAlbum(path, frequency)
        else:
            #a = random.sample(range(100), 1)
            #if path[-4:] == '.jpg' and a == [1]:
            if path[-4:] == '.jpg' or path[-4:] == '.png':
                im_index = im_index + 1
                if random.randint(1, frequency) != 1:
                    continue
                print('%d %s' % (im_index, path)),
                img = cv2.imread(path)
                print('h x w: %d x %d' % (img.shape[0], img.shape[1])),
                screen_res = 1080., 1920.
                scale_width = screen_res[1] / img.shape[1]
                scale_height = screen_res[0] / img.shape[0]
                scale = min(scale_width, scale_height)
                if scale < 1:
                    window_width = int(img.shape[1] * scale)
                    window_height = int(img.shape[0] * scale)
                    img = cv2.resize(img, (window_width, window_height))
                    print(', resized to %d x %d' % (window_height, window_width))
                else:
                    window_width = img.shape[1]
                    window_height = img.shape[0]
                    print('\n'),

                cv2.namedWindow(path, cv2.WINDOW_NORMAL)
                cv2.resizeWindow(path, window_width, window_height)
                cv2.imshow(path, img)
                keypress = cv2.waitKey(0)
                cv2.destroyAllWindows()
                if keypress == 27:
                    break
def main(image_folder, frequency):
    showAlbum(image_folder, frequency)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='show jpg images in folder.')
    parser.add_argument(
        'image_folder', help='the image folder you\'d like to show.')
    parser.add_argument(
        'show_frequency', help='randomly show one of show_frequency.',
        type=int,
        default=1)


    args = parser.parse_args()
    main(args.image_folder, args.show_frequency)
