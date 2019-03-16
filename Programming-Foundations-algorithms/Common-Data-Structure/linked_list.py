# 
# Linked List example
#
 
# The Node class example

class Node(object):
    def __init__(self, val):
        self.val=val
        self.next= None

    def get_value(self):
        return self.val

    def get_next(self):
        return self.next
    
    def set_value(self, val):
        self.val=val
    
    def set_next(self, next):
        self.next=next

class LinkedList(object):
    def __init__(self, head=None):
        self.head= head
        self.count=0

    def get_count(self):
        return self.count

    # Insert in from the top of the list
    def insert(self, data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.count +=1
        self.head=new_node

    # Search for the item until value match by the search item
    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_value() == val:
                return item
            else:
                item=item.get_next()
        return None
    # Delete specific item from the list
    def deleteAt(self, idx):
        if idx > self.count-1:
            return 
        if idx==0:
            self.head=self.head.get_next()
        else:
            tempid=0
            node=self.head
            while idx-1>tempid:
                node=node.get_next()
                tempid +=1
            node.set_next(node.get_next().get_next())
            self.count -= 1
            return 
        

    def dump_list(self):
        tempnode= self.head
        while(tempnode != None):
            print("Node: ", tempnode.get_value())
            tempnode = tempnode.get_next()

itemlist = LinkedList()
itemlist.insert(10)
itemlist.insert(38)
itemlist.insert(13)
itemlist.insert(15)
itemlist.insert(12)
itemlist.insert(76)
itemlist.dump_list()

print("Item count", itemlist.get_count())
print("Find Element", itemlist.find(13))
print("Find Element", itemlist.find(40))

# itemlist.deleteAt(2)
itemlist.deleteAt(5)
# itemlist.deleteAt(1)
print("Item count", itemlist.get_count())
itemlist.dump_list()
