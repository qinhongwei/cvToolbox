#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os

def parse_args():
    """Parse input arguments
    """
    parser = ArgumentParser()
    parser.add_argument('--video_list',
            help=('video list'),
            default='list.txt')
    parser.add_argument('--save_dir',
            help=('dir to save frames'),
            default='frames')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    listname = args.video_list
    save_dir = args.save_dir
    f = open(listname, 'r')
    videolist = f.readlines()
    i = 0
    print "hello"
    for line in videolist:
        line = line.strip('\n')
        print line
        filepath = line
        if os.path.isfile(filepath):
            n = len(filepath)
            savepath = os.path.join(save_dir, line[0:n-4])
            print savepath
            if not os.path.exists(savepath):
                os.makedirs(savepath)
            cmd = 'ffmpeg -i ' + filepath + ' -r 0.5 ' + os.path.join(savepath, '%05d.jpg')
            print cmd
            os.system(cmd)
            i = i + 1
            print("%d: %s" % (i, line))
    f.close()

if __name__ == '__main__':
    main()
