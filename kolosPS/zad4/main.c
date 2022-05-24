#include <stdio.h>
#include <stdlib.h>

struct osoba
{
    char *imie; //powinno byæ chyba char imie[20] ale nie dziala
    int wiek;
    float wzrost;
};

struct osoba f(unsigned n, struct osoba* tab)
{
    float najwiekszy_wzrost=0;
    int index_najwyzszego=0;
    for(int i=0; i<n; i++){
        if(tab[i].wzrost > najwiekszy_wzrost){
            najwiekszy_wzrost = tab[i].wzrost;
            index_najwyzszego = i;
        }
    }
    return tab[index_najwyzszego];
}

int main()
{
    unsigned n = 3;
    struct osoba tab[n];
    tab[0].imie = "Magda";
    tab[0].wiek = 20;
    tab[0].wzrost = 1.80;

    tab[1].imie = "Mateusz";
    tab[1].wiek = 20;
    tab[1].wzrost = 2.29;

    tab[2].imie = "Wiktor";
    tab[2].wiek = 21;
    tab[2].wzrost = 1.20;

    struct osoba najwyzsza = f(n, tab);
    printf("imie: %s\nwiek: %d\nwzrost: %f\n", najwyzsza.imie, najwyzsza.wiek, najwyzsza.wzrost);
    return 0;
}
