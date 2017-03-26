#Code to find the max subarray within an array

def findMaxCrossingSubArray(lowIndex,HighIndex,midIndex,arrA):
	rSum = 0
	lSum = 0
	rInd = 0
	lInd = 0
	Sum = 0
	for indA in range (midIndex+1,HighIndex+1):
		Sum+= arrA[indA]
		if(Sum>rSum):
			rSum = Sum
			rInd = indA

	Sum = 0
	for indB in xrange (midIndex,lowIndex-1,-1):
		Sum+= arrA[indB]
		if(Sum > lSum):
			lSum = Sum
			lInd = indB
	return (lInd,rInd,lSum+rSum)

def findMaxSubArray(arrA, lowIndex, HighIndex):
	if(lowIndex == HighIndex):
		return (lowIndex,HighIndex,arrA[lowIndex])
	midIndex = (lowIndex + HighIndex)/2
	(leftLowInd, leftHighInd, leftSum) = findMaxSubArray(arrA,lowIndex,midIndex)
	(righLowInd, rightHighInd, rightSum) = findMaxSubArray(arrA,midIndex+1,HighIndex)
	(crossLowInd, crossHighInd, crossSum) = findMaxCrossingSubArray(lowIndex,HighIndex,midIndex,arrA)

	if( leftSum>= rightSum and leftSum >= crossSum):
		return (leftLowInd,leftHighInd,leftSum)
	if( rightSum >= leftSum and rightSum >= crossSum):
		return (righLowInd, rightHighInd, rightSum)
	else:
		return (crossLowInd, crossHighInd, crossSum)

testArr = [0,-1,3,4,-6,2,5,1,-8,10,4]
tup = findMaxSubArray(testArr,0,len(testArr)-1)
print tup