"""
# In binary tree we have root, nodes (left nodes of right nodes). If a node has no descendants, it is called a "leaf"
# Also we have levels. Level 0 - root. Level - this is the number of hops to the node

# All node has 3 field:
1. Data
2. Link left
3. Link right

# Add new elements in tree:
1. If the value being added is less than the value in the parent node, then the new node is added to the left branch,
otherwise to the right
2. If the added value is already present in the tree, it is ignored

Right of the root - values that are less than root
Left of the root - values that are greater than root

Search element in binary tree
O(log(n)) -  in balanced tree
O(n) - in unbalanced tree

Balanced tree - if its subtrees differ from one root by NO more than 1 level.

Tree balancing methods
1. AVL tree
2. Red-Black tree
3. Splay tree

If the data is received in a random order in the problem being solved, then on average, a binary tree close
to a balanced one will be formed

Ways to traverse the nodes of a binary tree:
1. In width (breadth-first). On every level evade left to right
2. In depth. First the leftmost nodes, then we go up to the level and check right.
LNR - data in ascending order
RNL - data in descending order
NLR - direct bypass

Delete element in binary tree:
1. If we delete a "leaf": link on leaf = null in node and delete leaf
2. If we delete a node, we take the smallest value in right subtree and write instead of the value of the node
being deleted.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    __LNR = 0
    __RNL = 1
    __NLR = 2

    @property
    def LNR(self):
        return self.__LNR

    @property
    def RNL(self):
        return self.__RNL

    @property
    def NLR(self):
        return self.__NLR

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, node):
        if self.__root is None:
            self.__root = node
            return node

        s, p, is_find = self.__find(self.__root, None, node.data)

        if not is_find and s:
            if node.data < s.data:
                s.left = node
            else:
                s.right = node

        return node

    def __show_LNR(self, node):
        if node is None:
            return
        self.__show_LNR(node.left)
        print(node.data)
        self.__show_LNR(node.right)

    def __show_RNL(self, node):
        if node is None:
            return
        self.__show_RNL(node.right)
        print(node.data)
        self.__show_RNL(node.left)

    def __show_NLR(self, node):
        if node is None:
            return

        print(node.data)
        self.__show_NLR(node.left)
        self.__show_NLR(node.right)

    @staticmethod
    def __del_leaf(s, p):
        if p.left == s:
            p.left = None
        else:
            p.right = None

    @staticmethod
    def __del_one_child(s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            else:
                p.left = s.left

        else:
            if s.left is None:
                p.right = s.right
            else:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):
        s, p, is_find = self.__find(self.__root, None, key)

        if not is_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.left is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    @staticmethod
    def show_wide_tree(node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]

            print()
            v = vn

    def show_depth_tree(self, node, mode=0):
        if mode == self.__LNR:
            self.__show_LNR(node)
        elif mode == self.__RNL:
            self.__show_RNL(node)
        elif mode == self.__NLR:
            self.__show_NLR(node)
        else:
            raise Exception("Unknown tree traversal method")


def binary_tree():
    v = [10, 5, 7, 16, 13, 2, 20]
    t = Tree()

    for x in v:
        t.append(Node(x))

    # t.show_wide_tree(t.root)
    t.show_depth_tree(t.root, t.LNR)


def main():
    binary_tree()


if __name__ == '__main__':
    main()
