#!/usr/bin/env python3


def merge_two_files(fname1: str, fname2: str) -> str:
    """Takes two files with ordered numbers (positive or negative), one
    number per line, merges these files int new one, preserving the order
    and returns the name of a new file"""

    def proc_file(file):
        while True:
            line = file.readline()
            if not line:
                break
            yield line

    def init_val(proc):
        """ Returns line or None if file is empty """

        try:
            content = next(proc).rstrip('\n')
        except StopIteration:
            return None
        return int(content)

    def next_val(proc):
        content = next(proc).rstrip('\n')
        if content.lstrip('-').isdigit():
            return int(content)
        else:
            # In case of a new line at the end of the file
            raise StopIteration

    class KeyVal:
        """ Allows to create unique key objects, to avoid situations,
        when one of the equal integers keys override the other. """
        def __init__(self, val):
            self.val = val

    f1 = open(fname1)
    f2 = open(fname2)
    f3 = open('file3.txt', 'w')
    proc_1 = proc_file(f1)
    proc_2 = proc_file(f2)

    # Get initial values if file is not empty
    val_1 = init_val(proc_1)
    val_2 = init_val(proc_2)
    schedule = {}
    if val_1: 
        schedule[KeyVal(val_1)] = proc_1
    if val_2: 
        schedule[KeyVal(val_2)] = proc_2

    while True:
        if not schedule:
            break
        high_prior = sorted(schedule, key=lambda x: x.val)[0]
        current_proc = schedule.pop(high_prior)
        f3.write(str(high_prior.val) + '\n')
        try:
            new_val = next_val(current_proc)
            schedule[KeyVal(new_val)] = current_proc
        except StopIteration:
            pass

    f1.close(), f2.close(), f3.close()
    return 'file3.txt'


merge_two_files('file1.txt', 'file2.txt')

