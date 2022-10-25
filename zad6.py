def zad6(lst1, lst2):

    lst1.extend(lst2)
    new_list = list(set((i**3 for i in lst1)))
    return sorted(new_list)


if __name__ == '__main__':

    print(zad6([1, 2, 3, 4, 5], [4, 5, 7, 8, 9]))
