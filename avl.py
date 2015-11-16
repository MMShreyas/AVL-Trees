import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(bst.BST):
    """
AVL binary search tree implementation.
Supports insert, find, and delete-min operations in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t):
        """Insert key t into this tree, modifying it in-place."""
        print "Inserting",t,"\n"
        node = bst.BST.insert(self, t)
        self.rebalance(node)
        print self
        print("\n\n")

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                print "Rebalancing Left Subtree of",node.key
                if height(node.left.left) >= height(node.left.right):
                    print "Height of left Subtree",height(node.left.left),">=","Height of Right Subtree",height(node.left.right)
                    print "Applying Right Rotate at",node.key
                    self.right_rotate(node)
                else:
                    print "Applying Left Rotate at",node.left.key
                    self.left_rotate(node.left)
                    print "Applying Right Rotate at",node.key
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                print "Rebalancing Right Subtree of",node.key
                if height(node.right.right) >= height(node.right.left):
                    print "Height of left Subtree",height(node.right.left),"<=","Height of Right Subtree",height(node.right.right)
                    print "Applying left Rotate at",node.key
                    self.left_rotate(node)
                else:
                    print "Applying Right Rotate at",node.right.key
                    self.right_rotate(node.right)
                    print "Applying Left Rotate at",node.key
                    self.left_rotate(node)
            node = node.parent

    def delete_min(self):
        node, parent = bst.BST.delete_min(self)
        self.rebalance(parent)
        #raise NotImplemented('AVL.delete_min')

    def delete(self, t):
        node, parent = bst.BST.delete(self,t)

        #self.rebalance(parent)
        #node = self.root
        #while node is not None:
            #if t == node.key:
                #print "Search Success"
                #if(node.left == None and node.right == None):
                #self.left = None
                #self.right = None
                #self.parent = None
                #node.parent.left = None
                #return
                #if(node.parent.left):
                    #node.parent.left = node.right
                #if(node.parent.right):
                    #node.parent.right = node.left

                #return node
            #elif t < node.key:
             #   node = node.left
            #else:
              #  node = node.right
        # node, parent = bst.BST.delete_min(self)
        #self.rebalance(parent)

#def test(args=None):
#    bst.test(args, BSTtype=AVL)

#if __name__ == '__main__': test()

t = AVL()
t.insert(1)
t.insert(6)
t.insert(9)
t.insert(30)
t.insert(156)
t.insert(20)
t.insert(5)
t.insert(19)
t.insert(18)
t.insert(154)
t.insert(158)
t.insert(157)
t.insert(125)
#t.delete(158)
t.insert(155)
t.insert(180)
t.delete(30)

print t
