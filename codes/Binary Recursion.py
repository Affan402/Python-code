MyList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def BinarySearch(MyArray, SearchValue, Top, Bottom):
    while Top <= Bottom:
        Middle = (Top + Bottom)//2
        if SearchValue == MyArray[Middle]:
            return Middle
        elif SearchValue > MyArray[Middle]:
            Top = Middle +1
        else:
            Bottom = Middle -1
    return -1                

#print(BinarySearch(MyList, 30, 0, 9))


def BinaryRec(MyArray, SearchValue, Top, Bottom):
    Middle = (Top+Bottom)//2
    if SearchValue == MyArray[Middle]:
        return Middle
    elif Top > Bottom:
        return -1
    elif SearchValue > MyArray[Middle]:
        return BinaryRec(MyArray, SearchValue, Middle +1, Bottom)
    else:
        return BinaryRec(MyArray, SearchValue, Top, Middle -1)
    
print(BinaryRec(MyList, 200, 0, 9))    