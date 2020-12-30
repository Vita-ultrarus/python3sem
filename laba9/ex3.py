import zipfile
import os
import string
from pathlib import Path


class TextLoader:

    adr = None

    def __init__(self, adr):
        self.adr = adr

    def __len__(self):
        files = os.listdir(self.adr)
        self.files = files
        return len(files)

    def __next__(self):
        zn = ['/', '.', ';', ':', '(', ')', ',', '?', '!']
        for i in self.files:
            with open(self.adr + '\\' + i, 'rt') as j:
                j = j.lower()
                for t in range(len(zn)):
                    j = j.replace(zn[t], ' ')
                    self.normal = j
        raise StopIteration()


    def __iter__(self):
        return self


way = 'C:\\Users\\Имя\\python3sem\\лаба9\\sample'
a = TextLoader(way)
print(len(a))
print(next(a))