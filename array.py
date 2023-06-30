"""
Static array
1. All elements of the same type
2. Fixed number of elements
3. All elements are arranged sequentially in memory
4. O(1) - read/write operation.
5. O(n) - insert/delete element

Dynamic array
0.Dynamic arrays are implemented based on static arrays
1. All elements of the same type
2. Variable number of elements
3. All elements are arranged sequentially in memory
4. Have logic size (currentLength) and physic size (maxCapacity)
5. O(1) - read/write operation.
6. O(n) - insert/delete element

Single-linked list
1. The data is located in different memory areas
2. Have one link that points to the next element
3. O(n) or O(1) if we have a link on element that need insert/delete
4. O(n) - read/write operation
5. Have two links on head and tail of a list

Double-linked list
1. The data is located in different memory areas
2. Have two links, next points to the next element, prev points to the previous element
3. O(n) or O(1) if we have a link on element that need insert/delete
4. O(n) - read/write operation
5. Have two links on head and tail of a list

The difference between single-linked list and double-linked list:
1. In the double-linked list, we can iterate through the list in both directions
2. Double-linked list takes up more memory because it has an additional link (prev)
3. Deleting from the end for O(1) instead of O(n) as in a single-linked list

"""


def array_and_list():
    # Python lists are implemented on the basis of a dynamic array that stores links related to objects that
    # are "stored" in the list. Formally, it turns out that one type of data is stored - links.

    marks = [2, 3, 4, 5]
    lst = [0, 0.0, False]

    # Length array
    print(len(marks))

    # 0(1) insert in the end structure
    lst.append(0 + 0j)

    # O(n) insert in the structure
    lst.insert(0, "False")

    # O(1) Get value
    print(marks[0])

    # O(1) Set value
    marks[0] = 5

    # O(n + m) Connection arrays
    new = marks + lst
    print(new)

    # O(n) Create slice
    new = new[1:3]
    print(new)


def main():
    array_and_list()


if __name__ == '__main__':
    main()
