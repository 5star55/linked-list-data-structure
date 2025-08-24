class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head=None
    
    def __repr__(self):
        current=self.head


        if current==self.head:
                 
            print(f"Head: {current.data}")
        elif current.next==None:
            print(f"Tail: {current.data}")
        else:
            print(f"Data: {current.data}")
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def append(self,data):
        new_node= Node(data)
        current= self.head
        if not self.head:
            self.head=new_node
            return
        while current.next:
            current=current.next
        current.next=new_node
    def display(self):
        current= self.head
        while current:
            print(current.data, end="->")
            current=current.next
        print("None")

    def size(self):
        current=self.head
        count=0

        while current:
            count+=1
            current=current.next
        return count
    def is_empty(self):
        return self.head==None
    
    def insert(self, data, index):
        if index==0:
            self.prepend(data)
        else:
            new_node=Node(data)
            position=index
            current=self.head

            while current and position>1:
                position-=1
                current=current.next

            new_node.next=current.next
            current.next=new_node

    def remove(self,key):
        prev=None
        current=self.head
        found=False

        while current and not found:
            if current.data==key and current is self.next:
                found=True
                self.head=current.next
            elif current.data==key:
                found=True
                prev.next=current.next
            else:
                prev=current
                current=current.next
            
            if current is None:
                print(f"{key} does not exist")
        return current
    
    def remove_at_index(self, index):
        current=self.head
        if index == 0:
            self.head=current.next
        
        prev=None
        count=0
        
        while current and count<index:
            count+=1
            prev=current
            current=current.next
        if current is None: 
            print(f"{index}Out of range, no node removed")

        print(f"Removing node at index {index}, with value {current.data}")
        prev.next=current.next
        

            





    def search(self, key):
        current= self.head

        while current:
            current=current.next
            if key==current.data:
                return current
        return None

    

l1=Linkedlist()
l1.prepend(4)
l1.prepend(5)
l1.prepend(7)
l1.insert(6,2)
l1.display()
print(l1.search(5))
l1.remove_at_index(2)


l1.display()





    
           
        
           

        

    