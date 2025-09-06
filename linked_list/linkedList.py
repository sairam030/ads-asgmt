## 1. Create Single Linked List class with following functionalities:

class Single_linked_list():
    class _node_ :
        def __init__ (self,ele):
            self.data = ele
            self.next = None

    def __init__ (self):
        self.head=None
        self.tail =None
        self.count = 0

    def is_empty(self):
        return self.count==0

    def get_count(self):
        return self.count

    def add_at_head(self,ele):
        new_node = self._node_(ele)
        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count =+ 1
     
    def add_at_tail(self,ele):
        new_node = self._node_(ele)
        if not self.is_empty():
            self.tail.next = new_node.next
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def is_member(self,key):
        cur = self.head
        while cur!= None:
            if cur.data == key:
                break;
            else:
                cur = cur.next
        return cur!= None
    
    def display(self):
        cur = self.head
        l=[]
        while cur!= None:
            l.append(cur.data)
            cur=cur.next
        return l
    
    def delete_at_tail(self):
        if not self.is_empty():
            data = self.tail.data
            if self.count>1:
                last = self.tail
                cur = self.head
                while cur.next == last:
                    cur = cur.next
                cur.next = None
                self.tail = cur

            else:
                self.head = self.tail=None
                count = count -1
                return data
        else:
            return None