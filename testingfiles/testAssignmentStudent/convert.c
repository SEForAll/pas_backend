// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "list.h"
#include "convert.h"

#define try bool __HadError=false;
#define catch(x) ExitJmp:if(__HadError)
#define throw(x) __HadError=true;goto ExitJmp;

// DO NOT MODIFY FROM HERE --->>>
const int Operations[] = {'+', '-', '*', '(', ')'};

// return -1 if the word is not an operator
// return 0 if the word contains '+'
//        1                      '-'
//        2                      '*'
//        3                      '('
//        4                      ')'
int isOperator(char * word)
{
  int ind;
  int numop = sizeof(Operations) / sizeof(int);
  for (ind = 0; ind < numop; ind ++)
    {
    char *loc = strchr(word, Operations[ind]);
    if (loc != NULL && !isdigit(loc[1]))
	  {
	    return ind;
	  }
  }
  return -1;
}
// <<<--- UNTIL HERE

// ***
// *** You MUST modify the convert function
// ***
#ifdef TEST_CONVERT
ListNode * pop(List * list){
  ListNode * node = list -> head;
  list -> head = list -> head -> next;
  if (list -> head != NULL){
    list -> head -> prev = NULL;
  } else {
    list -> tail = NULL;
  }
  
  node -> next = NULL;
  node -> prev = NULL;
  
  return node;
}

void link(List * list, ListNode * node){
 node -> next = list -> head;
 if (node -> next == NULL){
   list -> tail = node;
 } else{
   list -> head -> prev = node;
 }
 list -> head = node;

 return;
}

bool convert(List * arithlist)
{
  if (arithlist == NULL)
    {
      return true;
    }
  if ((arithlist -> head) == NULL)
    {
      return true;
    }

  List * operators = malloc(sizeof(List));
  operators -> head = NULL;
  operators -> tail = NULL;

  List * out = malloc(sizeof(List));
  out -> head = NULL;
  out -> tail = NULL;

  while(arithlist -> head != NULL)
  {
    ListNode * current = pop(arithlist);
    
    int precidence = isOperator(current -> word);
    
    if(precidence == -1)
    {
      link(out, current);
    } else 
    {
      link(operators, current);
      
      if(operators -> head -> next != NULL)
      {
        int top = isOperator(operators -> head -> word);
        int under = isOperator(operators -> head -> next -> word);

        if(top == 1)
        {
          top = 0;
        }
        if(under == 1)
        {
          under = 0;
        }

        if(top > under && top != 4)
        {
          //do nothing
        }

        if(top == 4)
        {
          ListNode * node = pop(operators); // pop the ')'
          free(node);

          while(isOperator(operators -> head -> word) != 3 && operators -> head != NULL)
          {
            link(out, pop(operators));
          }

          node = pop(operators); // pop the '('
          free(node);
        }

        if(top <= under && under != 3)
        {
          ListNode * one = pop(operators);
          ListNode * two = pop(operators);

          link(operators, one);
          link(out, two);
        }
      }
    }
  }

  while(operators -> head != NULL)
  {
    link(out, pop(operators));
  }

  while(out -> head != NULL)
  {
    link(arithlist, pop(out));
  }

  deleteList(out);
  deleteList(operators);

  return true;
  
}
#endif

