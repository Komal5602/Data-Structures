class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        myhash=0
        for letter in key:
            myhash=(myhash+ord(letter)*17)%len(self.data_map)
        return myhash
    
    def set_table(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_items(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
                
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def printTable(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
my_hash_table=HashTable()

my_hash_table.set_table('grapes',13)
my_hash_table.set_table('apples',7)
my_hash_table.set_table('bananas',3)
print(my_hash_table.get_items('apples'))
print(my_hash_table.keys())
# my_hash_table.printTable()