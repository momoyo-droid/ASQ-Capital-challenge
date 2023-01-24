import file
import my_structure as ms


def main():
    file.create_file()

    structure_dict = ms.Structure()

    with open("in.txt", "r") as in_txt:

        with open("out.txt", "w") as out_txt:
            for line in in_txt:
                key = int(line)
                structure_dict.add(key)   # key to dictionary
            # write out.txt file
            for key, value in structure_dict.dictionary.items():
                if value > 1:
                    out_txt.write(str(key) + " REPETIDO" + '\n')
                else:
                    out_txt.write(str(key) + " INEDITO" + '\n')

    structure_dict.show()

    file.move_file()

    return


if __name__ == "__main__":
    main()
