#include <stdio.h>
#include <stdlib.h>

int f(char napis[])
{
    int index = 0;
    while(napis[index]!='\0'){
        if(napis[index]>='0' && napis[index]<='9'){
            return index;
        }
        index++;
    }
    return 0;
}

int main()
{
    char napis[] = "To jest napis 123"; //14
    printf("%d\n", f(napis));
    return 0;
}
