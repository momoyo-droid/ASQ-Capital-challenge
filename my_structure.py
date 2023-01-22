from collections import defaultdict

'''
class responsible for creating the dictionary structure and 
incrementing the value that each key is repeated in the file
'''
class StructureDict():
    def __init__(self) -> None:
        self.default_dict = defaultdict(int)

    def dictionary(self, integer_values) -> None:
        for key in integer_values:
            self.default_dict[key] += 1

    def writing(self) -> None:
        with open("out.txt", "w", encoding='utf-8') as f:
            for key, value in self.default_dict.items():
                if value > 1:
                    f.write(str(key) + " REPETIDO" + '\n')
                else:
                    f.write(str(key) + " INEDITO" + '\n')
