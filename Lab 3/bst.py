class BinarySearchTree:
    def __init__(self) -> None:
        self.size_bst = 0
        self.root = None

    class _BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.left = None
            self.right = None
            self.value = value
            self.parent = None

    # Insert into the Binary Search Tree
    def add(self, key, value):
        z = self._BSTNode(key, value)
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key > x.key:
                x = x.right
            else:
                x = x.left
        z.parent = y
        # if tree is empty assign z to root
        if y == None:
            self.root = z
        elif y.key < z.key:
            y.right = z
        else:
            y.left = z

        # Increase size
        self.size_bst += 1

    # Search an element in the BST, Arguments passed must be the root of the BST and the key
    def search(self, root, key):
        # If not found
        if root is None:
            return False

        # If found in root
        if root.key == key:
            return root.value

        if root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    # Return the size of the BST
    def size(self):
        return self.size_bst

    # Return the smallest element in BST
    def smallest(self):
        if self.root is None:
            return None
        x = self.root
        while x.left is not None:
            x = x.left
        return x.key, x.value

    # Return the largest element in BST
    def largest(self):
        if self.root is None:
            return None
        x = self.root
        while x.right is not None:
            x = x.right
        return x.key, x.value

    def remove(self):
        pass

    def in_order(self, root):
        if root is None:
            return ()
        return in_order(root.left)
        arr.append(root.key)
        return in_order(root.right)

    def post_order(self, root):
        if root is None:
            return ()
        return post_order(root.right)
        return post_order(root.left)
        arr.append(root.key)

    def pre_order(self, root):
        if root is None:
            return ()
        arr.append(root.key)
        return pre_order(root.left)
        return pre_order(root.right)
