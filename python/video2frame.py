#!/usr/bin/env python
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os

def parse_args():
    """Parse input arguments
    """
    parser = ArgumentParser()
    parser.add_argument('--video_dir',
            help=('video dir'),
            default='./')
    parser.add_argument('--save_dir',
            help=('dir to save frames'),
            default='frames')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    dir = args.video_dir
    save_dir = args.save_dir
    videolist = os.listdir(dir)
    i = 0
    for line in videolist:
        filepath = os.path.join(dir, line)
        filepath_new = filepath.replace(' ', '-') # some files contain space in filename
        line_new = line.replace(' ', '-')
        os.rename(filepath, filepath_new)
        filepath = filepath_new
        line = line_new
        print filepath
        if os.path.isfile(filepath):
            n = len(filepath)
            savepath = os.path.join(save_dir, line[0:n-6])
            print savepath
            if not os.path.exists(savepath):
                os.makedirs(savepath)
            cmd = 'ffmpeg -i ' + filepath + ' -r 5 ' + os.path.join(savepath, '%05d.jpg')
            print cmd
            os.system(cmd)
            i = i + 1
            print("%d: %s" % (i, line))
        if os.path.isdir(filepath):
            videolist_sub = os.listdir(filepath)
            for line_sub in videolist_sub:
                filepath_sub = os.path.join(filepath, line_sub)
                filepath_sub_new = filepath_sub.replace(' ', '-') # some files contain space in filename
                line_sub_new = line_sub.replace(' ', '-')
                os.rename(filepath_sub, filepath_sub_new)
                filepath_sub = filepath_sub_new
                line_sub = line_sub_new
                print filepath_sub
                if os.path.isfile(filepath_sub):
                    n = len(filepath_sub)
                    savepath = os.path.join(save_dir, line, line_sub)
                    print savepath
                    if not os.path.exists(savepath):
                        os.makedirs(savepath)
                    cmd = 'ffmpeg -i ' + filepath_sub + ' -r 5 ' + os.path.join(savepath, '%05d.jpg')
                    print cmd
                    os.system(cmd)
                    i = i + 1
                    print("%d: %s" % (i, line_sub))

if __name__ == '__main__':
    main()
