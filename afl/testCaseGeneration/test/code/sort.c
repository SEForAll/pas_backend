// ***
// *** You MUST modify this file, only the ssort function
// ***

#include "sort.h"
#include <stdio.h>

// DO NOT MODIFY THIS FUNCTION
bool checkOrder(int * arr, int size)
	// This function returns true if the array elements are
	// in the ascending order.
	// false, otherwise
{
	int ind;
	for (ind = 0; ind < (size - 1); ind ++)
	{
		if (arr[ind] > arr[ind + 1])
		{
			return false;
		}
	}
	return true;
}


// YOU MUST MODIFY THIS FUNCTION
void ssort(int * arr, int size)
{
	// This function has two levels of for
	// The first level specifies which element in the array
	// The second level finds the smallest element among the unsorted
	// elements

	// This is the syntax to read or write an array element:
	// int x = arr[4];
	// read the value of arr[4] and store it in x
	// arr[4] = 5;
	// stores 5 in the element arr[4]
	// Please remember that indexes start from 0.

	// After finding the smallest element among the unsorted elements,
	// swap it with the element of the index from the first level

	int ind; // Index used for looping through array
	int count; // Counter to keep track of place in array
	int place; // Placeholder to store index of smallest val 
	int x; //Smallest val

        // loops through the each place in the array
	for (count = 0; count < (size - 1); count ++)
	{
		x = arr[count];
		place = count;
                
                // loops from last unsorted place
		for (ind = (count + 1); ind < (size); ind ++)
		{
             
                        // Tests to see if value in question is smaller than current val
			if (arr[ind] < x)
			{
				x = arr[ind];
				place = ind;
			}
                }
                 
                // Switches necissary array elements
		arr[place] = arr[count];
	        arr[count] = x;  
	}
}
