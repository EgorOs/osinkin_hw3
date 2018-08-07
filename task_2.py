#!/usr/bin/env python3


def merge_two_files(fname1: str, fname2: str) -> str:
    '''Takes two files with ordered numbers (positive or negative), one
    number per line, merges these files int new one, preserving the order
    and returns the name of a new file'''

    def proc_file(file):
        while True:
            line = file.readline()
            if not line:
                break
            yield line


    def next_val(proc):
        content = next(proc).rstrip('\n')
        if content.lstrip('-').isdigit():
            return int(content)
        else:
            # In case of a new line at the end of the file
            raise StopIteration


    class KeyVal:
        ''' Allows to create unique key objects, to avoid situations,
        when one of the equal integers keys overrite the other. '''
        def __init__(self, val):
            self.val = val


    f1 = open(fname1)
    f2 = open(fname2)
    f3 = open('file3.txt', 'w')
    proc_1 = proc_file(f1)
    proc_2 = proc_file(f2)
    val_1 = next_val(proc_1)
    val_2 = next_val(proc_2)
    #queue = {KeyVal(val_1): proc_1, KeyVal(val_2): proc_2}
    queue = {}
    queue[KeyVal(val_1)] = proc_1
    queue[KeyVal(val_2)] = proc_2
    while True:
        if not queue:
            break
        high_prior = sorted(queue, key=lambda x: x.val)[0]
        current_proc = queue.pop(high_prior)
        f3.write(str(high_prior.val) + '\n')
        try:
            new_val = next_val(current_proc)
            queue[KeyVal(new_val)] = current_proc
        except StopIteration:
            pass

    f1.close(), f2.close(), f3.close()
    return 'file3.txt'



# ISSUES
# do I have to consider float numbers?
# newline at the end of the file
# what about empty file?

# f = open('file1.txt')
# for line in f: print(line, end='')

merge_two_files('file1.txt', 'file2.txt')

