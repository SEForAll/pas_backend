#include <stdio.h>  
#include <stdlib.h> 
#include <string.h> 
#include <stdbool.h>

int main(void)
{
    char * line = NULL;
    size_t len = 0;

    while (getline(&line, &len, stdin) != -1) {
        printf("%s", line);
    }
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}
