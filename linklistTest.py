class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def  getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,newdata):
        self.next=newdata
    def setnext(self,newnode):
        self.next=newnode
"""
temp=Node(93)
temp.setdata(10)
print(temp.getnext())
"""
#定义无序链表
class unorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getnext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() ==item:
                found = True
            else:
                current = current.getnext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous=current
                current = current.getnext()
        if previous == None:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())
myList = unorderedList()
myList.add(26)
myList.add(39)
myList.add(28)
myList.add(240)
myList.add(97)
myList.add(71)
print(myList.search(39))
myList.remove(97)
print(myList.search(97))
