"""
统计目录下的文件大小
"""
import os

cwd = os.getcwd()
files = os.listdir('.')
size = 0
for file in files:
    if os.path.isfile(file):
        size += os.path.getsize(f'{cwd}/{file}')
print(size / 1024)
