'''library for generating random numbers'''
import random as rd

MAX_NUM = 25

'''
method responsible return a file
'''
def create_file():
    '''create a file and recording integer values in it (one per line)'''
    with open("nums.txt", 'w', encoding='utf-8') as file:

        for i in range(MAX_NUM):
            int_num = rd.randint(0, 100)
            file.write(f'{int_num}\n')
    return