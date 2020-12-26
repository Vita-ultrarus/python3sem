class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.val):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def dfs(self, root):
        stack = []
        if root:
            stack = self.dfs(root.left)
            stack.append(root.val)
            stack = stack + self.dfs(root.right)

        return stack
