#include <stdio.h>
#include <stdlib.h>

struct element{
    double i;
    struct element* next;
};

void f(struct element* x){
    if (x == NULL){
        return;
    }

    struct element* przedostatni_index = NULL;
    while (x != NULL){
        if (x->next != NULL){
            if (x->next->i < 0){
                przedostatni_index = x;
            }
        }
        x = x->next;
    }

    if (przedostatni_index != NULL){
        struct element* nast = przedostatni_index->next->next;
        free(przedostatni_index->next);
        przedostatni_index->next = nast;
    }

}

int main()
{

    struct element a1 = {1.0, NULL};
    struct element a2 = {1.0, &a1};
    struct element a3 = {-1.0, &a2};
    struct element a4 = {-1.0, &a3};
    struct element a5 = {1.0, &a4};
    struct element a6 = {1.0, &a5};
    struct element tab[6];
    tab[0] = a1;
    tab[1] = a2;
    tab[2] = a3;
    tab[3] = a4;
    tab[4] = a5;
    tab[5] = a6;

    f(tab);
    struct element* x = &a6;
    while (x != NULL){
        printf("%f\n", x->i);
        x = x->next;
    }

    return 0;
}
