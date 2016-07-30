# -*- coding: utf-8 -*-
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
def parse_args():
    """Parse input arguments
    """
    parser = ArgumentParser()
    parser.add_argument('--dir',
            help=('dir'))
    parser.add_argument('--keyword',
            help=('keyword'),
            default='')
    parser.add_argument('--filetype',
            help=('filetype'),
            default='')
    args = parser.parse_args()
    return args


def list_myfiles(rootDir, keyword, filetype):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            list_myfiles(path, keyword, filetype)
        else:
            if (filetype == '' or path[0-len(filetype):] == filetype) and path.find(keyword) != -1:
                print path
                #os.remove(path)
if __name__ == '__main__':
    args = parse_args()
    dir = args.dir
    keyword = args.keyword
    filetype  = args.filetype
    list_myfiles(dir, keyword, filetype)
