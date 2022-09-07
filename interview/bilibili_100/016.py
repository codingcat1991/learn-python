import os
import shutil

files = os.listdir()
for file in files:
    if os.path.isdir(file):
        continue
    name, post = os.path.splitext(file)
    dir = post[1:]
    if not os.path.isdir(dir):
        os.mkdir(dir)
    shutil.move(f'{file}', f'{dir}/{file}')
