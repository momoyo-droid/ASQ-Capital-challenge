import file
import my_structure as ms


def main():
    file.create_file()

    structure_dict = ms.Structure()

    with open("in.txt", "r") as in_txt:

        with open("out.txt", "w") as out_txt:
            for line in in_txt:
                key = int(line)
                # key to dictionary and write out file
                structure_dict.add(key, out_txt)
            structure_dict.show()

    file.move_file()

    return


if __name__ == "__main__":
    main()
