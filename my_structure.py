'''
class responsible for creating the dictionary structure and 
incrementing the value that each key is repeated in the file
'''


class Structure():
    def __init__(self) -> None:
        self.dictionary = {}   # data structure

    def add(self, key):
        # return the value for the key
        if self.dictionary.get(key):
            self.dictionary[key] += 1   # is repeated
        else:
            self.dictionary[key] = 1   # not repeated

    def show(self):   # show the dictionary
        print(self.dictionary)
