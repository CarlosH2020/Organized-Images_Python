"""
Organized Images 2.0 - Oganiza imagens dentro de pastas
By Carlos Henrque Barros Silva Campos

"""
import os
import glob
import shutil
import time
from pathlib import Path
arq_img = ["*.png", "*.jpg", "*.gif"]

print('Organized Images 2.0')
time.sleep(1)

try:
    desktop = Path.home() / "Desktop"
    os.mkdir(f'{desktop}\\Files')
    os.mkdir(f'{desktop}\\Files\\JPG')
    os.mkdir(f'{desktop}\\Files\\PNG')
    os.mkdir(f'{desktop}\\Files\\GIF')
except FileExistsError:
    pass

print()


def menu():
    print('=====================')
    print('        MENU         ')
    print('=====================')
    print('1 - PNG')
    print('2 - JPG')
    print('3 - GIF')
    print('4 - ALL')


def informacao(value):
    """ 4 - ALL para organizar toda as extensões IMG"""
    if value == 4:
        imagens_all()


def imagens_png():
    pass


def imagens_jpg():
    pass


def imagens_gif():
    pass


def imagens_all():
    os.chdir(desktop)
    for files in arq_img:
        for format_files in glob.glob(files):
            print(format_files)
            time.sleep(5)
            if files == arq_img[0]:
                shutil.move(format_files, 'C:\\Users\\Root\\Desktop\\Files\\PNG')

            elif files == arq_img[1]:
                shutil.move(format_files, 'C:\\Users\\Root\\Desktop\\Files\\JPG')

            elif files == arq_img[2]:
                shutil.move(format_files, 'C:\\Users\\Root\\Desktop\\Files\\GIF')


try:
    menu()
    opc = int(input('OPC:'))
    informação(opc)
except ValueError as err:
    print(err)





