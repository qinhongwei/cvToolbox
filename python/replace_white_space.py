#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os

def parse_args():
    """Parse input arguments
    """
    parser = ArgumentParser()
    parser.add_argument('--root_dir',
            help=('root dir'))
    args = parser.parse_args()
    return args
def replace_white_space(root_dir):
    """Replace the white space with '_' in dir and file names
    """
    filelist = os.listdir(root_dir)
    for line in filelist:
        print line
        filepath = os.path.join(root_dir, line)
        filepath_new = filepath.replace(' ', '_') # some files contain space in filename
        os.rename(filepath, filepath_new)
        filepath = filepath_new
        print filepath
        if os.path.isdir(filepath_new):
            replace_white_space(filepath_new)
def main():
    args = parse_args()
    root_dir = args.root_dir
    replace_white_space(root_dir)

if __name__ == '__main__':
    main()
