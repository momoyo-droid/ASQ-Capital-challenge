import file
import my_structure as ms


INEDITO = 0
REPETIDO = 1


def main():
    file.create_file()
    f = open("in.txt", "r")

    structure_dict = ms.Structure()

    integer_values = []
    '''
    read each line (integer values) of the file and add them to the list
    '''
    for i in range(file.MAX_NUM):
        value = f.readline()
        integer_values.append(int(value))

    structure_dict.verify_using_dict(integer_values)
    structure_dict.writing_using_dict()

    f.close()
    file.move_file()
    
    return


if __name__ == "__main__":
    main()
