def my_range(n, e, s, m=1, view='No'):   # m means it'll multiply each value by given value: my_range(0, 11, 1, 2) --> 0*2..1*2..2*2...
    list1 = []                          # m = 1 and view = 'No' because if not given when calling
    list2 = []                          # the program won't crash as these are their default values
    start = n
    while start < e:
        list1.append(start)
        result = start * m  # new positional arg "m"
        start += s
        list2.append(result)
    if view == 'Yes':
        for i in list1:
            print(i)
        for k in list2:
            print("\t", "\t", "Multiples are as follows: {}.".format(k))
    else:
        pass
    return list1, list2
the_view = input("Do you want to view the list in a ordered way?: ")
print(my_range(0, 11, 2, 2, the_view.capitalize()))

