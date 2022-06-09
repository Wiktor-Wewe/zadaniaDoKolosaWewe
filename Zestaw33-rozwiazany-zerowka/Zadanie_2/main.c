#include <stdio.h>
#include <stdlib.h>

int funkcja(unsigned int n)
{
    int suma = 0;
    for(int i=0; i<n; i++)
    {
        if(i%5==0 || i%7==0)
        {
            suma += i;
        }
    }
    return suma;
}

int main()
{
    printf("Hello world!\n");
    printf("%d",funkcja(8));
    return 0;
}
