#include <stdio.h>
#include <stdlib.h>

struct node
{
    float x;
    struct node * next;
};

struct node* dodaj(struct node* lista, float a)
{
    struct node* wsk = malloc(sizeof(struct node));
    wsk->x=a;
    wsk->next=lista;
    return wsk;
}

int funkcja(struct node *tab)
{
    if(tab==NULL)
    {
        return 0;
    }
    struct node *wsk = tab;
    while(wsk!=NULL)
    {
        if(wsk->x<0)
        {
            return 0;
        }
        wsk=wsk->next;
    }
    return 1;
}

int main()
{
    printf("Hello world!\n");
    struct node *lista = NULL;
    printf("%d\n\n", funkcja(lista));
    lista = dodaj(lista,4.5);
    printf("%d\n\n", funkcja(lista));
    lista = dodaj(lista,2.2);
    lista = dodaj(lista,-1.9);
    printf("%d\n\n", funkcja(lista));
    return 0;
}
