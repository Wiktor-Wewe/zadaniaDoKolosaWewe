#include <stdio.h>
#include <stdlib.h>

char* foo(char* napis1, char* napis2)
{
    int dlugosc1 = 0;
    for(int i=0; napis1[i]!='\0'; i++){
        dlugosc1++;
    }

    int dlugosc2 = 0;
    for(int i=0; napis2[i]!='\0'; i++){
        dlugosc2++;
    }
    char* napis = malloc((dlugosc1+dlugosc2+1)*(sizeof(char)));
    for(int i=0; i<dlugosc1; i++){
        napis[i] = napis1[i];
    }
    for(int i=0; i<dlugosc2; i++){
        napis[dlugosc1+i]=napis2[i];
    }
    napis[dlugosc1+dlugosc2] = '\0';
    return napis;
}

int main()
{

    printf("%s", foo("Wiktor ", "Wewersjtys"));
    return 0;
}
