import random as rd
import shutil
import os

MAX_NUM = 25
FILES_TO_MOVE = ['in.txt', 'out.txt']

'''
method responsible create a file
'''
def create_file():
    '''create a file and recording integer values in it (one per line)'''
    with open("in.txt", 'w', encoding='utf-8') as file:
        for i in range(MAX_NUM):
            value = rd.randint(0, 100)
            file.write(f'{value}\n')

    return

'''
method responsible for move files to another directory
'''
def move_file():
    current_path = os.getcwd()

    for file in FILES_TO_MOVE:
        src = current_path + "/" + file
        dest = current_path + "/" + "txt/" + file
        shutil.move(src, dest)
        print("Moved Files: ", file)

    return
