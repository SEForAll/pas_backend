// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <string.h> 

#ifdef TEST_ELIMINATE
// 100% of the score
void eliminate(int n, int k)
{
  // allocate an arry of n elements
  int * arr = malloc(sizeof(* arr) * n);
  // check whether memory allocation succeeds.
  // if allocation fails, stop
  if (arr == NULL)
    {
      fprintf(stderr, "malloc fail\n");
      return;
    }
  // initialize all elements
  int i,j,m = 0;
  for(i=0;i<n;i++) arr[i]=i;
  i=0;
  // counting to k,
  // mark the eliminated element
  // print the index of the marked element
  // repeat until only one element is unmarked
  while (m<n-1){
    j=0;
    while(j<k){
      if(i==n) i=0;
      if(arr[i] != -1) j++;
      i++;
    }
    printf("%d\n",arr[--i]);
    m++;
    arr[i]=-1;
  }
  // print the last one
  for(i = 0;i < n;i++)
      if(arr[i]!= -1)
         printf("%d\n",arr[i]);
  // release the memory of the array
  free (arr);
}
#endif
