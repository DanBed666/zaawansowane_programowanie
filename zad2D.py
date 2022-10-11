def zad2d(lst):

    return [i for i in lst[::2]]

if __name__ == '__main__':

    print(zad2d([i for i in range(1, 11)]))