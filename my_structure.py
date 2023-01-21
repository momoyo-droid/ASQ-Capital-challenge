from collections import defaultdict


class StructureDict():
    def __init__(self, ln) -> None:
        self.ln = []

    def add(self, n) -> None:
        self.ln.append(int(n))

    def dictionary(self) -> dict:
        dd = defaultdict(int)

        for k in self.ln:
            dd[k] += 1

        return dd

    def writing(self) -> None:
        d = self.dictionary()

        with open("out.txt", "w", encoding='utf-8') as f:
            for k, v in d.items():
                if v > 1:
                    f.write(str(k) + " REPETIDO" + '\n')
                else:
                    f.write(str(k) + " INEDITO" + '\n')

    def test(self) -> None:
        for i in range(len(self.ln)):
            print(self.ln[i])
