class PriorityQueue():
    def __init__(self) -> None:
        self.queue = []
        
    def insert_item(self,item):
        self.queue.append(item)
        position = len(self.queue)-1
        while position > 0 and self.queue[self.get_father(position)][0] > item[0]:
            self.queue[self.get_father(position)], self.queue[position] = self.queue[position], self.queue[self.get_father(position)]
            position = self.get_father(position)
        
    
    def get_father(self,position):
        return (position-1)//2
    
    def min_heapfy(self,queue,father):
        smaller = father
        left = 2* father+1
        
        if(left< len(queue) and queue[left][0]< queue[smaller][0]):
            smaller = left
            
        right = 2*father+2
        
        if(right < len(queue) and queue[right][0]<queue[smaller][0]):
            smaller = right
        
        if(smaller != father):
            queue[father],queue[smaller] =queue[smaller],queue[father]
            self.min_heapfy(queue,smaller)             
    
    def pop_item(self):
        element = self.queue[0]
        self.queue[0] = self.queue[len(self.queue)-1]
        self.queue.pop(-1) 
        self.min_heapfy(self.queue,0)
        return element
    
    def is_empty(self):
        return self.queue is []