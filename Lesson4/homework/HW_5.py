newList = []


def Selection_Sort(myList):
    if len(myList) == 0:
        return print(newList)
    else:
        # find min
        min = myList[0]
        for i in myList:
            if i < min: min = i
        for i in range(len(myList)):
            if myList[i] == min:
                newList.append(myList[i])
                # swap
                tg = myList[i]
                myList[i] = myList[0]
                myList[0] = tg
        Selection_Sort(myList[1:len(myList)])


Selection_Sort([3, 2, 4, 5, 1, 7])
