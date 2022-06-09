#include <stdio.h>
#include <stdlib.h>

struct Osoba
{
    char *imie;
    int wiek;
    float wzrost;
};

char *funkcja(struct Osoba *tablica, int n)
{
    int najstarszy=0;
    for(int i=0; i<n; i++)
    {
        if(tablica[i].wiek>tablica[najstarszy].wiek)
        {
            najstarszy=i;
        }
    }
    return tablica[najstarszy].imie;
}

int main()
{
    unsigned int n=4;
    struct Osoba tab[n];
    tab[0].imie = "Michal";
    tab[0].wiek = 20;
    tab[0].wzrost = 1.76;

    tab[1].imie = "Janusz";
    tab[1].wiek = 11;
    tab[1].wzrost = 1.80;

    tab[2].imie = "Kornel";
    tab[2].wiek = 21;
    tab[2].wzrost = 2.00;

    tab[3].imie = "Wiktor";
    tab[3].wiek = 90S;
    tab[3].wzrost = 1.20;
    printf("%s",funkcja(tab,n));
    return 0;
}
