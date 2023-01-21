import file
import my_structure as ms

def main():
    file.create_file()
    f = open("nums.txt", "r")
    
    l = []
    sm = ms.StructureDict(l)
    
    for i in range(file.MAX_NUM):
        num = f.readline()
        sm.add(num)
        
    sm.test()
    sm.dictionary()
    sm.writing()
    
    return

if __name__ == "__main__":
    main()