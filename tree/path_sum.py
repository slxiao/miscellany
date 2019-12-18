#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.leftChild = None
        self.rightChild = None
  
class Tree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    @staticmethod
    def create(array, node, index, length): 
        if index < length: 
            node = Node(array[index])   
            node.leftChild = Tree.create(array, node.leftChild, 2 * index + 1, length)  
            node.rightChild = Tree.create(array, node.rightChild, 2 * index + 2, length) 
        return node 

    @staticmethod
    def search(stack, node, total):
        if node == None: 
            return
        stack.append(node.data) 
        if node.leftChild == None and node.rightChild == None: 
            if sum(stack) == total:
                print(", ".join([str(i) for i in stack])) 
        Tree.search(stack, node.leftChild, total) 
        Tree.search(stack, node.rightChild, total) 
        stack.pop() 

def main(array, total):
    tree = Tree()
    tree.root = Tree.create(array, None, 0, len(array))
    tree.search([], tree.root, total)

if __name__ == '__main__': 
    main([10, 5, 12, 4, 7], 22)
    