def sort(array, odd):
    inOrder = False
    totalSortTimes = 2
    randomNumber = [0]
    print(array)
    if odd:
        array.append(randomNumber)

    while not inOrder:
        k = 0
        tempArr = []
        while array[0][0].__len__() != 0 and array[1][0].__len__() != 0:
            if array[0][0] > array[1][0]:
                tempArr.append(array[1][0])
            else:
                tempArr.append(array[0][0])


        while k < 2:
            del array[0]
            k += 1

        if array.__len__() == 1:
            inOrder = True
    totalSortTimes *= 2


def split(array):
    odd = False
    tempList = array.split(" ")

    if tempList.__len__() % 2 == 1:
        odd = True

    splitList = []
    for i in tempList:
        singleton = [int(i)]
        splitList.append(singleton)

    sort(splitList, odd)


inputList = input()
split(inputList)
