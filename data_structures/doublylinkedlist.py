class DNode:
    def __init__(self, value, prev = None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.num_nodes = 0

#     def is_empty(self):
#         return self.num_nodes == 0
    
#     def size(self):
#         return self.num_nodes
    
#     def index_of(self, value):
#         idx = 0

#         node = self.head
#         while node:
#             if node.get_value() == value:
#                 return idx
#             else:
#                 idx += 1
#             node = node.get_next()
        
#         return -1
    
#     def contains(self, value):
#         return self.index_of(value) != -1
    
#     def get_value_at_index(self, i):
#         counter = 0
#         value = 0

#         if (i < 0) or (i > self.size() - 1):
#             raise IndexError("Invalid index")
        
#         node = self.head
#         while node:
#             if counter == i:
#                 value = node.get_value()
#                 break
#             node = node.get_next()
#             counter += 1

#         return value
    
#     def get_first(self):
#         return self.get_item_at_index(0)
    
#     def get_last(self):
#         return self.get_item_at_index(self.size() - 1)
    
#     def add_at_index(self, i, value):
#         new_node = SNode(value)

#         if (i >= 0) and (i <= self.size()):
#             if i == 0:
#                 self.insert(None, new_node)
#             else:
#                 node = self.get_node_at_index(i - 1)
#                 self.insert(node, new_node)
#         else:
#             raise IndexError("Invalid index")

#     def add_front(self, value):
#         self.add_at_index(0, value)

#     def add_back(self, value):
#         self.add_at_index(self.size(), value)

#     def remove_at_index(self, i):
#         value = 0

#         if (i >= 0) and (i < self.size()) and self.head:
#             if i == 0:
#                 value = self.remove(None)
#             else:
#                 node = self.get_node_at_index(i - 1)
#                 node = self.remove(node)
#         else:
#             raise IndexError("Invalid index")
        
#         return value
    
#     def remove_front(self):
#         return self.remove_at_index(0)
    
#     def remove_back(self):
#         return self.remove_at_index(self.size() - 1)
    
#     def print(self):
#         if not self.head:
#             print("Nothing to print")
#         else:
#             node = self.head
#             print(f"List is: {node.get_value()}")
#             for i in range(1, self.size()):
#                 node = node.get_next()
#                 print(f", {node.get_value()}")
#             print(".")

#     def get_head(self):
#         return self.head
    
#     def get_node_at_index(self, i):
#         if (i < 0) or (i > self.size() - 1):
#             raise IndexError("Invalid index")
        
#         counter = 0
#         node = self.head

#         while node:
#             if counter == i:
#                 break
#             node = node.get_next()
#             counter += 1
        
#         return node
    
#     def insert(self, node, new_node):
#         if not node:
#             new_node.set_next(self.head)
#             self.head = new_node
#         else:
#             new_node.set_next(node.get_next())
#             node.set_next(new_node)

#         self.num_nodes += 1

#     def remove(self, node):
#         if not node:
#             value = self.head.get_value()
#             self.head = self.head.get_next()
#         else:
#             value = node.get_next().get_value()
#             node.set_next(node.get_next().get_next())
        
#         self.num_nodes -= 1

#         return value
        
        
