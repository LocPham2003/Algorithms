def sort(array, odd):
    inOrder = False
    randomNumber = [0]
    if odd:
        array.append(randomNumber)

    while not inOrder:
        isFirstArrayNotEmpty = True
        isSecondArrayNotEmpty = True
        tempArr = []
        while isFirstArrayNotEmpty and isSecondArrayNotEmpty:
            print("Sorting")
            isFirstArrayNotEmpty = len(array[0]) != 0
            isSecondArrayNotEmpty = len(array[1]) != 0
            if len(array[0]) == 0 and len(array[1]) == 1:
                tempArr.append(array[1][0])
                del array[1][0]
            elif len(array[0]) == 1 and len(array[1]) == 0:
                tempArr.append(array[0][0])
                del array[0][0]
            elif len(array[0]) == 0 and len(array[1]) > 1:
                if array[1][0] > array[1][1]:
                    tempArr.append(array[1][1])
                    del array[1][1]
                else:
                    tempArr.append(array[1][0])
                    del array[1][0]
            elif len(array[1]) == 0 and len(array[0]) > 1:
                if array[0][0] > array[0][1]:
                    tempArr.append(array[0][1])
                    del array[0][1]
                else:
                    tempArr.append(array[0][0])
                    del array[0][0]
            elif array[0][0] > array[1][0]:
                tempArr.append(array[1][0])
                del array[1][0]
            elif array[0][0] < array[1][0]:
                tempArr.append(array[0][0])
                del array[0][0]
            
        array.append(tempArr)
        if len(array) == 2:
            del array[0]
        elif len(array) > 2:
            del array[0]
            del array[0]

        if len(array) == 1:
            inOrder = True
    print(array)
    return array


def split(array):
    odd = False
    tempList = array.split(" ")

    if len(tempList) % 2 == 1:
        odd = True

    splitList = []
    for i in tempList:
        singleton = [int(i)]
        splitList.append(singleton)

    return sort(splitList, odd)[0]


inputList = input()
sortList = split(inputList)
print(sortList)

