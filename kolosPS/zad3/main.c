#include <stdio.h>
#include <stdlib.h>

int** tab2d(int x, int y)
{
    int** tab = malloc(y*sizeof(int));
    for(int i=0; i<y; i++){
        tab[i] = malloc(x*sizeof(int));
    }
    return tab;
}

float f(unsigned n, unsigned m, int** tab)
{
    float ilosc_elem=0, suma=0;
    for(int y=0; y<m; y++){
        for(int x=0; x<n; x++){
            if(tab[x][y]%2==1){
                suma+=tab[x][y];
                ilosc_elem++;
            }
        }
    }
    return suma/ilosc_elem;
}

int main()
{
    unsigned n = 2;
    unsigned m = 2;

    int** tab2 = tab2d(n, m);
    tab2[0][0] = 1;
    tab2[0][1] = 3;
    tab2[1][0] = 2;
    tab2[1][1] = 4;

    //powinno zworicic 2 bo (1+3)/2
    printf("%f\n", f(n, m, tab2));
    return 0;
}
