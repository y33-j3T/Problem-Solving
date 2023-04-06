class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.size = 1

class AVL:
    def __init__(self):
        self.root = None
    
    def _search(self, node, value):
        if not node: return None
        elif value == node.value: return node
        elif value > node.value: return self._search(node.right, value)
        else: return self._search(node.left, value)

    def search(self, value):
        res = self._search(self.root, value)
        # return T() if not res else res.value
        return -1 if not res else res.value
    
    def _find_min(self, node):
        if not node.left:
            return node.value
        return self._find_min(node.left)
    
    def find_min(self):
        return self._find_min(self.root)
    
    def _find_max(self, node):
        if not node.right:
            return node.value
        return self._find_max(node.right)
    
    def find_max(self):
        return self._find_max(self.root)
    
    def _successor(self, value):
        vPos = self._search(self.root, value)
        # return T() if not vPos else self.successor(vPos)
        return -1 if not vPos else self.successor(vPos)
    
    def successor(self, node):
        if not node.right:
            return self._find_min(node.right)
        
        parent_node = node.parent
        while (parent_node) and (node == parent_node.right):
            node = parent_node
            parent_node = node.parent

        return None if not parent_node else parent_node.value
    
    def _predecessor(self, value):
        vPos = self._search(self.root, value)
        # return T() if not vPos else self.predecessor(vPos)
        return -1 if not vPos else self.predecessor(vPos)
    
    def predecessor(self, node):
        if not node.left:
            return self._find_max(node.left)
        
        parent_node = node.parent
        while (parent_node) and (node == parent_node.left):
            node = parent_node
            parent_node = node.parent

        # return T() if not parent_node else parent_node.value
        return -1 if not parent_node else parent_node.value
    
    def _inorder(self, node):
        if not node: return None
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _insert(self, node, value):
        if not node:
            return Node(value)
        
        tmp = node.parent
        if value > node.value:
            node.right = self._insert(node.right, value)
            node.right.parent = node
        else:
            node.left = self._insert(node.left, value)
            node.left.parent = node

        self._update_height(node)
        self._update_size(node)
        return self._balance(node)
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
        
    def _remove(self, node, value):
        if not node:
            return None
        
        if value > node.value:
            node.right = self._remove(node.right, value)
        elif value < node.value:
            node.left = self._remove(node.left, value)
        else:
            if (not node.left) and (not node.right):
                return None
            elif (not node.left) and (node.right):
                node.right.parent = node.parent
                return node.right
            elif (node.left) and (not node.right):
                node.left.parent = node.parent
                return node.left
            else:
                successor_value = self._successor(node)
                node.value = successor_value
                node.right = self._remove(node.right, successor_value)

            self._update_height(node)
            self._update_size(node)
            return self._balance(node)
        
    def remove(self, value):
        self.root = self._remove(self.root, value)
    
    def _balance(self, node):
        if self.height(node.left) > self.height(node.right) + 1:
            if self.height(node.left.right) > self.height(node.left.left):
                node.left = self._left_rotate(node.left)
            node = self._right_rotate(node)
        elif self.height(node.right) > self.height(node.left) + 1:
            if self.height(node.right.left) > self.height(node.right.right):
                node.right = self._right_rotate(node.right)
            node = self._left_rotate(node)

        return node
    
    def _right_rotate(self, node):
        if not node:
            return None
        
        child = node.left
        tmp = node.left.right
        node.left.right = node
        node.left = tmp

        self._update_height(node)
        self._update_height(child)
        self._update_size(node)
        self._update_size(child)
        return child
    
    def _left_rotate(self, node):
        if not node:
            return None
        
        child = node.right
        tmp = node.right.left
        node.right.left = node
        node.right = tmp

        self._update_height(node)
        self._update_height(child)
        self._update_size(node)
        self._update_size(child)
        return child 
    
    def _rank(self, node, value):
        if not node:
            return 0
        elif value < node.value:
            return self._rank(node.left, value)
        elif value > node.value:
            return self.size(node.left) + 1 + self._rank(node.right, value)
        else:
            return self.size(node.left)
        
    def rank(self, value):
        return self._rank(self.root, value)
    
    def _update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def height(node):
        if not node:
            return -1
        return node.height

    def _update_size(self, node):
        node.size = self.size(node.left) + self.size(node.right) + 1

    def size(node):
        if not node:
            return 0
        return node.size
            