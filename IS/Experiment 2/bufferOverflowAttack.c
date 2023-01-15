#include <stdio.h>
// #include <conio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *ptr;
    char *dptr;
    // clrscrO;
    ptr = (char *)malloc(10 * sizeof(char));
    dptr = (char *)malloc(10 * sizeof(char));
    printf("\nAddress of ptr : %d\n", ptr);
    printf("Address of dptr: %d\n", dptr);
    printf("\nEnter The String:\n");

    gets(ptr);
    system(dptr);
}