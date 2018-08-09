#!/usr/bin/env python3

import os


def hardlink_check(directory_path: str) -> bool:
    unique_inodes = set()
    try:
        for file in os.listdir(directory_path):
            inode = os.stat('{}/{}'.format(directory_path, file)).st_ino
            if inode not in unique_inodes:
                unique_inodes.add(inode)
            else:
                return True
    except Exception as e:
        print(e)
    return False
