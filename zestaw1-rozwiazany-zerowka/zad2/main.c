#include <stdio.h>
#include <stdlib.h>

int suma(unsigned int n)
{
    int wynik=0;
    for(int i=0; i<=n; i++){
        wynik += i*i*i;
    }
    return wynik;
}

int main()
{
    printf("Suma dla 4 = %d\n", suma(4));
    printf("Suma dla 12 = %d\n", suma(12));
    return 0;
}
