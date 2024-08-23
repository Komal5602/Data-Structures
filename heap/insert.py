class heap:
    def __init__(self):
        self.heap = []

    def left_child(self,index):
        return 2*index + 1
    
    def right_child(self,index):
        return 2*index + 2
    
    def parent(self,index):
        return (index - 1) // 2
    
    def swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current=len(self.heap)-1
    
        while current > 0 and self.heap[self.parent(current)] < self.heap[current]:
            self.swap(current,self.parent(current))
            current=self.parent(current)

myheap=heap()
myheap.insert(10)
myheap.insert(20)
myheap.insert(30)
myheap.insert(26)
myheap.insert(29)

print(myheap.heap)

myheap.insert(40)
print(myheap.heap)