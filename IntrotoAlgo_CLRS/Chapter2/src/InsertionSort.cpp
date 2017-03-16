//Function to take an array of length n , and sort it
#include "stdint.h"
#include <iostream>
#include "InsertionSort.h"
using namespace std;

void InsertionSort(int* A,int aLen)
{
	for(uint32_t index = 0; index<(aLen-1); index++ )
	{
		uint32_t compareIndex = index+1;
		for(uint32_t innerLoop = 0; innerLoop<=index; innerLoop++)
		{
			if(A[compareIndex]<A[innerLoop])
			{
				int32_t tempVal = A[compareIndex];
				for(uint32_t shiftInd = compareIndex;shiftInd>innerLoop;shiftInd--)
				{
					A[shiftInd]=A[shiftInd-1];
				}
				A[innerLoop] = tempVal;
			}
		}
	}
}

void PrintArray(int*A, int aLen)
{
	for(uint32_t index = 0; index<aLen; index++)
	{
		cout<<"A["<<index<<"]"<<" = "<<A[index]<<endl;
	}
}
