"""
Trie - prefix tree
In every node ONE symbol
1. is_key - whether the vertex is intermediate or the value of a particular key. If we see false,
then this is an intermediate value (there is no such key), if we meet the first true, then all the characters before it
will be the keys of the tree, that is, true - this vertex is the end of this or that key.
2. symbol - stores 1 key symbol
3. Data - data that is available for this key

O(|key|) - get the value by key

Deleting keys:
First we delete leaf vertices.
We change all the characters of the key to is_key false if the key is intermediate, for another key and data = None.
If all the symbols don't lead anywhere else, we remove them from the tree if the vertex is a leaf

If the tree is large and loaded, then you can simply change the flag to false - there will be no big memory loss
If the tree is small, then you can delete leaf vertices
If you delete leaf nodes sequentially, then the prefix tree is compressed
"""


class Node:

    def __init__(self, char=None, key=False, data=None):
        self.char = char
        self.is_key = key
        self.data = data
        self.children = []

    @staticmethod
    def __format(node):
        chd = list()
        for child in node.children:
            chd.append(child.char)
        return chd

    def __str__(self):
        return f"Char: {self.char} Is_key: {self.is_key} Data: {self.data} Children: {self.__format(self)}"


class Trie:
    __dict = {}

    def __init__(self):
        self.__root = Node("*", False, None)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("The key must be a string")

        chars = self.__get_chars(key)
        count = 0
        parent = self.__root
        for char in chars:
            if count < len(chars) - 1:
                count += 1
                parent = self.__append(Node(char, False), parent)
            else:
                parent = self.__append(Node(char, True, value), parent)

        self.__add_dict(key, value)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError("The key must be a string")

        chars = self.__get_chars(key)
        node = self.__root
        count = 0
        for char in chars:
            is_find, node = self.__find(node, char)
            if not is_find:
                raise IndexError("Element with this key doesn't exist")
            count += 1
            if count == len(chars):
                if node.is_key:
                    return node.data
                else:
                    raise IndexError("Element with this key doesn't exist")

    def __delitem__(self, key):
        if not isinstance(key, str):
            raise TypeError("The key must be a string")

        chars = self.__get_chars(key)
        for char in chars:
            pass

    def __str__(self):
        return str(self.__root)

    def __del_leaf(self, node):
        pass

    @staticmethod
    def __get_chars(key):
        return list(key)

    @staticmethod
    def __find(node, value):
        if not node.children:
            return False, None

        for child in node.children:
            if value == child.char:
                return True, child
        return False, None

    def __append(self, node, parent):
        is_exist, n = self.__find(parent, node.char)
        if not is_exist:
            parent.children.append(node)
            return node
        else:
            if node.is_key and node.data:
                n.is_key = node.is_key
                n.data = node.data
            return n

    def __add_dict(self, key, value):
        self.__dict[key] = value

    def show(self):
        for key, value in self.__dict.items():
            print(f"[{key}]:{value}", end="\n")

    def clear(self):
        self.__root = Node("*", False, None)

    def empty(self):
        if self.__root.children:
            return False
        return True

    def copy(self):
        temp = Node()
        temp.data = self.__root.data
        temp.char = self.__root.char
        temp.is_key = self.__root.is_key
        temp.children = self.__root.children
        return temp


def main():
    t = Trie()
    t["key"] = 1
    t["kea"] = 2
    t["kob"] = 3
    t["kok"] = 4
    t["k"] = 8
    t["ko"] = 9
    t["yes"] = 5
    t["y"] = 10
    t["yi"] = 6

    t.show()
    print(t)


if __name__ == "__main__":
    main()
