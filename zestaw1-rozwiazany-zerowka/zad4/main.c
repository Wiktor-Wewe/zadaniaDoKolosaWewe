#include <stdio.h>
#include <stdlib.h>

struct element
{
    float x;
    struct element* next;
};

struct element* dodaj(struct element* lista, float a)
{
    struct element* wsk = malloc(sizeof(struct element));
    wsk->x=a;
    wsk->next=lista;
    return wsk;
}

void f(struct element* lista)
{
    if(lista!=NULL){
        struct element* wsk = lista;
        printf("Adres ostatniego elementu: %p\n", wsk);
        while(wsk->next!=NULL){
            wsk = wsk->next;
        }
        printf("Adres pierwszego elementu: %p\n", wsk);
    }
    else{
        printf("NULL\n");
    }
}

int main()
{
    struct element* lista=NULL;
    lista = dodaj(lista, 12.42);
    lista = dodaj(lista, -123.245);
    lista = dodaj(lista, -12.00);
    lista = dodaj(lista, 22.112);
    f(lista);
    return 0;
}
