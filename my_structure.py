REPETIDO = 1
INEDITO = 0

'''
class responsible for creating the dictionary structure and
incrementing the value that each key is repeated in the file
'''


class Structure():
    def __init__(self) -> None:
        self.dictionary = {}   # data structure

    def add(self, key, out_txt):
        # check if key exist in dictionary
        if key in self.dictionary:
            self.dictionary[key] = REPETIDO   # is repeated
            out_txt.write(str(key) + " REPETIDO" + '\n')
        else:
            self.dictionary[key] = INEDITO   # not repeated
            out_txt.write(str(key) + " INEDITO" + '\n')

    def show(self):   # show the dictionary
        print(self.dictionary)
