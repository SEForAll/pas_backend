#include "shuffle.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// do not modify this function
static void printDeck(CardDeck deck)
{ 
  int ind;
  for (ind = 0; ind < deck.size; ind ++)
    {
      printf("%c ", deck.cards[ind]);
    }
  printf("\n");
}

void divide(CardDeck origDeck, CardDeck * leftDeck, CardDeck * rightDeck)
{
  int le = origDeck.size;
  for(int i=1;i< le;i++){
    leftDeck[i-1].size = i;
    rightDeck[i-1].size = le-i; 
    memcpy(leftDeck[i-1].cards,origDeck.cards,i*sizeof(origDeck.cards[0]));
    memcpy(rightDeck[i-1].cards,origDeck.cards+i*sizeof(origDeck.cards[0]),(le-i)*sizeof(origDeck.cards[0]));
  }
}
void helper(CardDeck leftDeck, CardDeck rightDeck,int left,int right,CardDeck *result,int round){
  if(left == leftDeck.size){
    if(right <= rightDeck.size){
      for(int i=left+right;i<leftDeck.size+rightDeck.size;i++)
         result->cards[i] = rightDeck.cards[i-left];
    }
    round ==1 ? printDeck(*result):shuffle(*result,round-1);
    return;
  }
  if(right == rightDeck.size){
    if(left < leftDeck.size){
      for(int i=left+right;i<leftDeck.size+rightDeck.size;i++)
         result->cards[i] = leftDeck.cards[i-right];
    }
    round == 1 ? printDeck(*result):shuffle(*result,round-1);
    return;
  }
  result->cards[left+right] = leftDeck.cards[left];
  helper(leftDeck,rightDeck,left+1,right,result,round);
  result->cards[left+right] = rightDeck.cards[right];
  helper(leftDeck,rightDeck,left,right+1,result,round);
  return;
}
void interleave(CardDeck leftDeck, CardDeck rightDeck,int round)
{  
  CardDeck *result;
  result= malloc(sizeof(CardDeck));
  result->size = leftDeck.size+rightDeck.size;
  helper(leftDeck,rightDeck,0,0,result,round);
  free(result);
}
void shuffle(CardDeck origDeck, int round)
{
  CardDeck * leftDeck;
  CardDeck * rightDeck;
  leftDeck = malloc((MAX_SIZE-1)*sizeof(CardDeck));
  rightDeck = malloc((MAX_SIZE-1)*sizeof(CardDeck));
  divide(origDeck,leftDeck,rightDeck);
  for(int i=0;i<origDeck.size-1;i++){
     interleave(leftDeck[i],rightDeck[i],round);
  }
  free(leftDeck);
  free(rightDeck);
}