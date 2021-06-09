// ***
// *** DO NOT modify this file
// ***

#include <stdio.h>  
#include <stdlib.h> 
#include <string.h> 
#include <stdbool.h>
#include "sort.h"

void printArray(int * arr, int size)
{
  int ind;
  for (ind = 0; ind < size; ind ++)
    {
      fprintf(stdout, "%d\n", arr[ind]);
    }
}

int main(int argc, char * * argv)
{
  // read input file
  // open file to read
  if (stdin == NULL)
    {
      fprintf(stderr, "fopen fail\n");
      // do not fclose (fptr) because fptr failed
      return EXIT_FAILURE;
    }
  // count the number of integers
  int value;
  int count = 0;
  while (fscanf(stdin, "%d", & value) == 1)
    {
      count ++;
    }
  fprintf(stdout, "The file has %d integers\n", count);
  // allocate memory to store the numbers
  int * arr = malloc(sizeof(int) * count);
  if (arr == NULL) // malloc fail
    {
      fprintf(stderr, "malloc fail\n");
      return EXIT_FAILURE;
    }
  // return to the beginning of the file
  fseek (stdin, 0, SEEK_SET);
  int ind = 0;
  while (ind < count)
    {
      if (fscanf(stdin, "%d", & arr[ind]) != 1)
	{
	  fprintf(stderr, "fscanf fail\n");
	  free (arr);
	  return EXIT_FAILURE;
	}
      ind ++;
    }
  ssort(arr, count);
  // call checkOrder to see whether this function correctly sorts the
  // elements
  if (checkOrder(arr, count) == false)
    {
      fprintf(stderr, "checkOrder returns false\n");
    }
  printArray(arr, count);
  free (arr);
  return EXIT_SUCCESS;
}
