// ***
// *** You MUST modify this file, only the ssort function
// ***

#include <stdio.h>
#include <stdbool.h>

#ifdef TEST_COUNTCHAR
bool countChar(char * filename, int * counts, int size)
{
  // open a file whose name is filename for reading
  // if fopen fails, return false. Do NOT fclose
  // if fopen succeeds, read every character from the file
  //
  FILE * fptr = fopen(filename,"r");
  if(fptr==NULL){
    return false;
  }
  // if a character (call it onechar) is between
  // 0 and size - 1 (inclusive), increase
  // counts[onechar] by one
  // You should *NOT* assume that size is 256
  // reemember to call fclose
  // you may assume that counts already initialized to zero
  // size is the size of counts
  // you may assume that counts has enough memory space
  //
  // hint: use fgetc
  // Please read the document of fgetc carefully, in particular
  // when reaching the end of the file
  //
  int ch;
  while((ch = fgetc(fptr))!= EOF){
    if(ch<size && ch>=0)
      counts[ch]++;
  }
  fclose(fptr);
  return true;
}
#endif

#ifdef TEST_PRINTCOUNTS
void printCounts(int * counts, int size)
{
  // print the values in counts in the following format
  // each line has three items:
  // ind, onechar, counts[ind]
  // ind is between 0 and size - 1 (inclusive)
  // onechar is printed if ind is between 'a' and 'z' or
  // 'A' and 'Z'. Otherwise, print space
  // if counts[ind] is zero, do not print
  int i;
  for(i=0;i<size;i++){
    if(counts[i]){
      // 65-90,97-122
      ((i>64 && i <91) || (i>96 && i<123) ) ? printf("%d, %c, %d\n",i,i,counts[i]) : printf("%d,  , %d\n",i,counts[i]);
    }
  }
}
#endif
