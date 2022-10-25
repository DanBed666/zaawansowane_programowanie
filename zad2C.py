def zad2c(lst):

    return [i for i in lst if i % 2 == 0]


if __name__ == '__main__':

    print(zad2c([i for i in range(1, 11)]))
