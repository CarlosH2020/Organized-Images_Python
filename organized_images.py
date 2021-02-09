"""
Organized Images - Oganiza imagens dentro de pastas


class Imgs:

    def __init__(self, jpg, gif, png):
        self.__jpg = jpg
        self.__gif = gif
        self.__png = png

    def localiza_jpg(self):
        return os.chdir(f'C:\\Users\\Root\\Desktop')

    def localiza_gif(self):
        pass

    def localiza_png(self):
        pass


files = Imgs(glob.glob("*.jpg"), glob.glob("*.gif"), glob.glob("*.png"))
"""
import os
import glob
import shutil
import time


print('Organized Images')
time.sleep(5)
try:
    os.mkdir('C:\\Users\\Root\\Desktop\\Files')
    os.mkdir('C:\\Users\\Root\\Desktop\\Files\\JPG')
    os.mkdir('C:\\Users\\Root\\Desktop\\Files\\PNG')
    os.mkdir('C:\\Users\\Root\\Desktop\\Files\\GIF')
except FileExistsError:
    pass


os.chdir('C:\\Users\\Root\\Desktop')
for file in glob.glob("*.png"):
    if file:
        print(file)
        shutil.move(file, 'C:\\Users\\Root\\Desktop\\Files\\PNG')
for file in glob.glob("*.jpg"):
    if file:
        print(file)
        shutil.move(file, 'C:\\Users\\Root\\Desktop\\Files\\JPG')
for file in glob.glob("*.gif"):
    if file:
        print(file)
        shutil.move(file, 'C:\\Users\\Root\\Desktop\\Files\\GIF')

