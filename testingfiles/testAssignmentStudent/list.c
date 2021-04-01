#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
 
#ifdef TEST_READLIST
bool readList(char * filename, List * arithlist)
{
  FILE * fptr = fopen(filename, "r");
  
  if (fptr == NULL)
  {
    //printf("ftpr is null\n");
    return false;
  }

  if (arithlist == NULL)
  {
    //printf("arithlist is null\n");
    return false;
  }

  int char0;
  int index = 0;
  char word[WORDLENGTH] = {0};

  while((char0 = fgetc(fptr)) != EOF)
  {
    if (index > WORDLENGTH - 2)
    {
      deleteList(arithlist);
      fclose(fptr);

      return false;
    }

    word[index] = char0;
    index++;

    if (char0 =='\n')
    {
      word[index] = '\0';
      index = 0;
      addNode(arithlist, word);
    }
  }

  fclose(fptr);
  //printf("the list printing worked\n");
  return true;

  }
  #endif
  
  #ifdef TEST_DELETELIST
  void deleteList(List * arithlist)
  {
    ListNode * temp;

    while(arithlist -> head != NULL)
    {
      temp = arithlist -> head -> next;
      free(arithlist->head);
      arithlist -> head = temp;
    }

    free(arithlist);

  return;
}
#endif
 
#ifdef TEST_ADDNODE
void addNode(List * arithlist, char * word)
{
 if (arithlist == NULL)
 {
   return;
 }

 ListNode * temp;
 temp = arithlist->tail;
 arithlist -> tail = malloc(sizeof(ListNode));

 if (arithlist -> tail == NULL)
 {
   return;
 }

 arithlist -> tail -> prev = temp;
 memcpy(arithlist -> tail -> word, word, strlen(word) + 1);

 if (arithlist -> head == NULL)
 {
   arithlist -> head = arithlist->tail;
 }

 if (arithlist -> tail -> prev != NULL)
 {
   arithlist -> tail -> prev -> next = arithlist -> tail;
 }

 arithlist -> tail -> next = NULL;

 return;
}
#endif
 
#ifdef TEST_DELETENODE
bool deleteNode(List * arithlist, ListNode * ln)
{
  if (arithlist == NULL)
  {
    return false;
  }

  if ((arithlist -> head == NULL) && (arithlist -> tail == NULL))
  {
    return false;
  }

  if (arithlist -> head == ln)
  {
    arithlist -> head = ln -> next;
    arithlist -> head -> prev = NULL;

    free(ln);
    return true;
  }
  else if (arithlist -> tail == ln) 
  {
    arithlist -> tail = ln -> prev;
    ln -> prev -> next = NULL;

    free(ln);
    return true;
  }
  else
  {
    ListNode * cursor = arithlist->head->next;

    while (cursor != ln)
    {
      cursor = cursor -> next;
    }

    cursor -> next -> prev = cursor -> prev;
    cursor -> prev -> next = cursor -> next;
  }
  free(ln);
  return true;
}
#endif

