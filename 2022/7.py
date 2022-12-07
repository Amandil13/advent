#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re

def import_data():
    #Folder is just a dictionary that contains either more dictionaries or files
    root = folder('/','/')
    cwd = root
    with open('7.in') as f:
        for line in f:
            line = line.rstrip()
            if re.match (r'^\$',line): 
                m = re.search(r'^\$ (\w+) (\S+)',line)
                if m:
                    if m.group(1) == 'cd':
                        if m.group(2) == '..':
                            cwd = cwd.get_parent()
                        elif m.group(2) == '/':
                            cwd = root
                        else:
                            dirs = cwd.get_dirs()
                            cwd = dirs[m.group(2)]
            
            m = re.search(r'^(\d+) (\S+)',line)
            if m: 
                cwd.add_file(m.group(2),  m.group(1))
            else: 
                m = re.search(r'^dir (\S+)',line)
                if m:
                    cwd.add_folder(folder(m.group(1), cwd))
    return root
            

class folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.totalsize = 0
        self.size = 0
        self.dirs = {}
        #self.depth = parent.get_depth() + 1

    def get_dirs(self): 
        return self.dirs

    def get_files(self): 
        return self.files

    def get_parent(self): 
        return(self.parent)

    def get_size(self): 
        return(self.size)

    def get_totalsize(self): 
        return(self.totalsize)

    def get_name(self): 
        return self.name
    
    def get_depth(self):
        return self.depth

    def add_file(self,name,size):
        self.files[name] = int(size)
        self.size += int(size)

    def add_folder(self,folder): 
        self.dirs[folder.get_name()] = folder

    def du(self):
        for subdir in self.dirs.values(): 
            self.totalsize += subdir.du()
        self.totalsize += self.size
        print(f"Total size of {self.name} is {self.totalsize}")
        return self.totalsize

    def get_small_dirs(self): 
        dirs = []
        for subdir in self.dirs.values(): 
            dirs.extend(subdir.get_small_dirs())
        if int(self.totalsize) < 100000: 
            dirs.append(self.totalsize)
        return dirs

    def find_smallest(self,threshold): 
        smallest = 999999999
        if self.totalsize > threshold:
            smallest = self.totalsize
        for subdir in self.dirs.values(): 
            subdir_smallest = subdir.find_smallest(threshold)
            if subdir_smallest < smallest:
                smallest = subdir_smallest
        return smallest

    def __str__(self):
        return f"Name: {self.name}\nSize: {self.size}\nDirs: {self.dirs}\nfiles: {self.files}\n"


def part_one(data):
    smalldirs = sum(data.get_small_dirs())
    return smalldirs

def part_two(data):
    return data.find_smallest(1035571)

if __name__ == "__main__":

    data = import_data()
    data.du()
    part_one = part_one(data)
    part_two = part_two(data)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
