"""
Set - an unordered collection of data consisting of unique values
1.Implemented on binary red-black trees
2.O(n) - checking the "=", "<", ">" of sets (the two-pointer method)
"""


def main():
    s = {1, 2, 3, 2, 3}
    print(s)  # {1, 2, 3}

    # Create a copy of set
    s2 = s.copy()
    print("First set: ", s, "Second set:", s2, sep=" ")

    # Remove left element
    el = s.pop()  # el = 1
    print(el, s, sep=" & ")  # 1 & {2, 3}

    # Add new elements in a set
    s.update((4, 5))
    print(s)  # {2, 3, 4, 5}




if __name__ == "__main__":
    main()
