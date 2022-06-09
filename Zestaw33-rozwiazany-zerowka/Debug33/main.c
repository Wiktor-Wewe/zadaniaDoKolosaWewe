#include <stdio.h>
#include <stdlib.h>

int main()
{
    int tab[3][4] = {{1,-2,30,-4},{4,2,2,7},{3,1,3,3}};
    int a=tab[1][-3]; //a=
    int b=tab[2][-2]; //a=  ,b=
    a=b++; //a=  ,b=
    b=a^2;  //a=  ,b=
    a=(b+=3)+7;  //a=  ,b=
    b=**((tab)+2); //a=  ,b=
    ++a; //a=  ,b=
    return 0;
}
