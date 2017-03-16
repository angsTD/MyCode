//============================================================================
// Name        : Chapter2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "InsertionSort.h"
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	int testArray1[15]={-12, 1,7,3,90,5,27,-25,35,24,15,90,86,45,40};
	InsertionSort(testArray1,15);
	PrintArray(testArray1,15);

	return 0;


}
