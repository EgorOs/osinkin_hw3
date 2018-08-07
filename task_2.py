#!/usr/bin/env python3


def merge_two_files(fname1: str, fname2: str) -> str:

    def proc_file(file):
        while True:
            line = file.readline()
            if not line:
                break
            yield line

    f1 = open(fname1)
    f2 = open(fname2)
    proc_1 = proc_file(f1)
    proc_2 = proc_file(f2)
    val_1 = int(next(proc_1))
    val_2 = int(next(proc_2))
    while True:
        if val_1 <= val_2:
            print(val_1)
            val_1 = int(next(proc_1))
        else:
            print(val_2)
            val_2 = int(next(proc_2))


# f = open('file1.txt')
# for line in f: print(line, end='')

merge_two_files('file1.txt', 'file2.txt')

