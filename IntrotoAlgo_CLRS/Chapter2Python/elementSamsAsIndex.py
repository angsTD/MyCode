

def findelement(stInd,endInd,Arr):
	midind = (stInd + endInd)/2
	if(Arr[midind] == midind):
		return Arr[midind]
	elif (midind == stInd):
		return (-1)
	elif (Arr[midind-1]<Arr[midind]):
		return findelement(midind,endInd,Arr)
	else:
		return findelement(stInd,midind,Arr)


#testArray = [1,2,3,4,5,6,7,8,9,10,11,10,4,3]
testArray2= [-32,-24,-11,-5,-2,1,2,3,4,5,6,7,8,9,14,16,18,19,31]

print "Max Element: %d" %findelement(0,(len(testArray2)-1),testArray2)
