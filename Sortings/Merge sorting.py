def sort(array):
    inOrder = False
    while not inOrder:
        isArr1Empty = True
        isArr2Empty = True
        tempArr = []
        while isArr1Empty and isArr2Empty:
            isArr1Empty = len(array[0]) != 0
            isArr2Empty = len(array[1]) != 0
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
            elif array[0][0] == array[1][0]:
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
    return array


def split(array):
    tempList = array.split(" ")
    splitList = []
    for i in tempList:
        singleton = [int(i)]
        splitList.append(singleton)

    return sort(splitList)[0]

inputList = input()
print(split(inputList))
