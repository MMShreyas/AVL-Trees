class BST(object):
    """
Simple binary search tree implementation.
This BST supports insert, find, and delete-min operations.
Each tree contains some (possibly 0) BSTnode objects, representing nodes,
and a pointer to the root.
"""

    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key t into this BST, modifying it in-place."""
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    # Go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete_min(self):
        """Delete the minimum key (and return the old node containing it)."""
        if self.root is None:
            return None, None
        else:
            # Walk to leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree.
            if node.parent is not None:
                node.parent.left = node.right
            else: # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

    def delete(self,t):
        if self.root is None:
            return None, None
        else:
            node = self.root
            while node is not None:
                if t == node.key:
                    print "Deleting node",t,"\n"
                    # if it is a leaf node
                    if node.left is None and node.right is None:
                        if node.parent.left == node:
                            node.parent.left = None
                        if node.parent.right == node:
                            node.parent.right = None

                    # Node has only one subtree (right), replace root with that one
                    elif node.right is not None and node.left is None:
                        print "Replacing Right subtree with root\n"
                        if node.parent.left == node:
                            node.parent.left = node.right
                        if node.parent.right == node:
                            node.parent.right = node.right
                        node.right = None


                    # Node has only one subtree (left), replace root with that one
                    elif node.left is not None and node.right is None:
                        print "Replacing Left subtree with root\n"
                        if node.parent.left == node:
                            node.parent.left = node.left
                        if node.parent.right == node:
                            node.parent.right = node.left
                        node.left = None
                    # if node has left and right sub trees
                    elif node.right is not None and node.left is not None:
                        print "Selected node has left and right subtree"
                        successor= node.right

                        if node is self.root:
                            print "Deleting Root Node",node.key,"\n"
                            rootnode = node
                            #rootsuccessor = self.root
                            #rootsuccessor = node.right
                            if successor.left is None:
                                node = successor
                                #successor.parent = node.parent
                                node.left = rootnode.left
                                node.left.parent = node
                                #node.parent.right = successor
                            elif successor.left is not None:
                                while successor and successor.left:
                                    successor=successor.left

                                successor.parent.left = None
                                #copy of node
                                nodec = node
                                successor.left = node.left
                                #successor.parent = node.parent
                                successor.right = node.right
                                node.key = successor.key
                                #if node.parent.left == node:
                                   #node.parent.left = successor
                                #if node.parent.right == node:
                                   #node.parent.right = successor


                        elif successor.left is None:
                            successor.parent = node.parent
                            successor.left = node.left
                            node.left.parent = successor
                            node.parent.right = successor

                        elif successor.left is not None:
                            while successor and successor.left:
                                successor=successor.left

                            successor.parent.left = None
                            #copy of node
                            nodec = node
                            successor.left = node.left
                            successor.parent = node.parent
                            successor.right = node.right

                            if node.parent.left == node:
                               node.parent.left = successor
                            if node.parent.right == node:
                               node.parent.right = successor
                        #x = node.left
                        if node is self.root:
                            parent = node
                            return node,parent
                        else:
                            parent = node.parent
                            node.disconnect()
                            return node,parent

                        #node.key = successor.key






                    # Node has both left & right subtree
                    #else:
                     #   successor = node.right
                        #while successor and successor.left:
                         #   successor = successor.left

                        #if successor:
                         #   node.key = successor.key

                            # Delete successor from the replaced node right subree
                          #  node.right.delete(successor.key)

                    parent = node.parent
                    #node.disconnect()
                    return node, parent
                elif t < node.key:
                    node = node.left
                else:
                    node = node.right





    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

class BSTnode(object):
    """
Representation of a node in a binary search tree.
Has a left child, right child, and key value.
"""
    def __init__(self, t):
        """Create a new leaf with key t."""
        self.key = t
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None

# def test(args=None, BSTtype=BST):
#     import random, sys
#     if not args:
#         args = sys.argv[1:]
#     if not args:
#         print 'usage: %s <number-of-random-items | item item item ...>' % \
#               sys.argv[0]
#         sys.exit()
#     elif len(args) == 1:
#         items = (random.randrange(100) for i in xrange(int(args[0])))
#     else:
#         items = [int(i) for i in args]
#
#     tree = BSTtype()
#     print tree
#     for item in items:
#         tree.insert(item)
#         print
#         print tree
#
# if __name__ == '__main__': test()
