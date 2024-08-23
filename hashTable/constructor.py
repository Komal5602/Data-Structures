class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        myhash=0
        for letter in key:
            myhash=(myhash+ord(letter)*17)%len(self.data_map)
        return myhash
    def printTable(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
my_hash_table=HashTable()
my_hash_table.printTable()