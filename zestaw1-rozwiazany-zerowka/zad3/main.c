#include <stdio.h>
#include <stdlib.h>

void wyswietl_tablice(int** tab, unsigned int m, unsigned int n)
{
    for(int y=0; y<m; y++){
        for(int x=0; x<n; x++){
            printf("%d\t", tab[y][x]);
        }
        printf("\n");
    }
}

int **rezerwacja(int n, int m)
{
    int **tab=(int**)malloc(sizeof(int*)*n);
    for(int i=0;i<n;i++)
    {
        *(tab+i)=(int*)malloc(sizeof(int)*m);
    }
    return tab;
}

int f(int** tab, int n, int m)
{
    int max=0; int min=tab[0][0];
    for(int y=0; y<n; y++){
        for(int x=0; x<m; x++){
            if(tab[y][x]>max){
                max = tab[y][x];
            }
            if(tab[y][x]<min){
                min=tab[y][x];
            }
        }
    }
    return max-min;
}

int main()
{
    int** tab = rezerwacja(2, 3);
    tab[0][0] = 2; tab[0][1] = 12; tab[0][2] = 122;
    tab[1][0] = 3; tab[1][1] = 42; tab[1][2] = 452;
    wyswietl_tablice(tab, 2, 3);
    printf("roznica: %d\n", f(tab, 2, 3));
    return 0;
}
