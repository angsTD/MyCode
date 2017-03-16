
def insertionSortDec( unsortedList ):
    for index in range(1,len(unsortedList)):
        key = unsortedList[index]
        #print("Key: ", key," Index: ",index)
        innerIndex = index -1
        #print("Inner Index:",innerIndex)
        while (innerIndex>=0 and key > unsortedList[innerIndex] ):
            unsortedList[innerIndex+1] = unsortedList[innerIndex]
            innerIndex -= 1
        unsortedList[innerIndex+1]=key
 
testArrayList = [3,24,23,2,5,-2,-19,4,17,-6,34,22,23,-54,47,42,8724,24894,474,4284,5442,4824,-2424,-4284]
 
def printArray( unsortedList ):
    for index in range(0,len(unsortedList)):
        print "A[%d] = %d " %(index,unsortedList[index])


fp = open("InversionsTestCase.txt")
#lines = fp.readlines()
lines = map(int,fp.readlines())
insertionSortDec(lines)
printArray(lines)