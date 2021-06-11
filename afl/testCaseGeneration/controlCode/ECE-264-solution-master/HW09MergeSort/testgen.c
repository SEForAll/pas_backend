// ***
// *** test generator, for your reference
// ***
// *** You do not need to do anything with this file
// *** You MUST NOT submit this file. If you submit this file,
// *** you will receive 2 point penalty.
//
// *** DO NOT SUBMIT
//


#include <stdio.h>  
#include <stdlib.h> 
#include <string.h> 
#include <stdbool.h>
#include <time.h>
#include "hw09.h"
int cmp(const void *a, const void *b)
{
    return *(int*)a - *(int*)b; //????????????
    //return *(int *)b - *(int *)a; ????????????
}
int main(int argc, char * * argv)
{
  // argv[1]: number of vectors
  // argv[2]: name of output file (binary)
  if (argc != 4)
    {
      return EXIT_FAILURE;
    }
  int numElem = (int) strtol(argv[1], NULL, 10);
  if (numElem <= 0)
    {
      return EXIT_FAILURE;
    }
  int * vecArr;
  vecArr = malloc(sizeof (* vecArr) * numElem);
  if (vecArr == NULL)
    {
      return EXIT_FAILURE;
    }

  // assign the attributes
  srand (time(NULL));
  int ind;
  for (ind = 0; ind < numElem; ind ++)
    {
      // set the values between -49 and 50
      vecArr[ind] = (rand() % 1000) - 49;  
    }
  // print vector in text (to display)
  bool rtv1 = writeData(argv[2], vecArr, numElem);
  qsort(vecArr,numElem,sizeof(int),cmp);
  bool rtv2 = writeData(argv[3], vecArr, numElem);
  if (rtv1 == false || rtv2 == false) // read fail
    {
      free (vecArr);
      return EXIT_FAILURE;
    }
  free (vecArr);
  return EXIT_SUCCESS;
}

