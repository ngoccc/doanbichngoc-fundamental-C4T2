l = [(1, 2, 40), (0, 15, 60), (10, 80, 0)]


def Replace_Value(myList, value):
    aList = []
    newList = []
    for i in myList:
        for j in range(len(i)):
            if j == 2:
                aList.append(value)
                newList.append(tuple(aList))
                aList = []
            else:
                aList.append(i[j])
    return newList



print(Replace_Value(l, 100))
