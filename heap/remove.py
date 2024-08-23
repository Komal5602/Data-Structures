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

    def sink_down(self,index):
        max_index=index
        while True:
            left=self.left_child(index)
            right=self.right_child(index)
            if left<len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index=left
            if right<len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index=right

            if max_index != index:
                self.swap(index,max_index)
                index=max_index
            else:
                return
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.sink_down(0)
        return max_val


myheap=heap()
myheap.insert(10)
myheap.insert(20)
myheap.insert(30)
myheap.insert(26)
myheap.insert(29)

print(myheap.heap)
myheap.remove()
print(myheap.heap)