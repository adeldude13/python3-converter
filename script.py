import glob
import codecs
import os
import re
import time
from pathlib import Path

formatt = input("Format? ")

def converter(dir_name=os.getcwd()):
    print("dir: " + dir_name)

    dirs = [d for d in os.listdir(dir_name) if os.path.isdir(os.path.join(dir_name, d))]
    for dir in dirs:
        if dir == "converted":
            continue
        converter(os.path.join(dir_name, dir))

    for file_name in Path(dir_name).glob(f"*.{formatt}"):
        convdir = os.path.join(dir_name, "converted/")
        if not os.path.exists(convdir):
            os.mkdir(convdir)
        print(file_name.name)
        with codecs.open(file_name, mode="r", encoding="cp1256") as sourceFile:
            with codecs.open(os.path.join(dir_name, "converted", file_name.name), mode="w", encoding="utf-8") as targetFile:
                while True:
                    contents = sourceFile.read()
                    if not contents:
                        break
                    targetFile.write(contents)


converter()
