#include <stdio.h>
#include <stdlib.h>

typedef struct listNode {
    int data;
    struct listNode* next;
    struct listNode* prev;
} listNode;

void criaLista(listNode **l) {
    *l = NULL;
}

void adicionarInicio(listNode **l, int value) {
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    temp->next = *l;
    temp->prev = NULL;
    
    if (*l != NULL) {
        (*l)->prev = temp;
    }
    *l = temp;
}

void removerInicio(listNode **l) {
    if (*l == NULL) return;
    
    listNode* temp = *l;
    *l = (*l)->next;
    if (*l != NULL) {
        (*l)->prev = NULL;
    }
    free(temp);
}

void adicionarFim(listNode **l, int value) {
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    temp->next = NULL;
    
    if (*l == NULL) {
        temp->prev = NULL;
        *l = temp;
        return;
    }
    
    listNode* atual = *l;
    while (atual->next != NULL) {
        atual = atual->next;
    }
    atual->next = temp;
    temp->prev = atual;
}

void removerFim(listNode **l) {
    if (*l == NULL) return;
    
    listNode* atual = *l;
    while (atual->next != NULL) {
        atual = atual->next;
    }
    
    if (atual->prev != NULL) {
        atual->prev->next = NULL;
    } else {
        *l = NULL;
    }
    free(atual);
}

void adicionarMeio(listNode **l, int value, int pos) {
    if (*l == NULL || pos == 0) {
        adicionarInicio(l, value);
        return;
    }
    
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    
    listNode* atual = *l;
    for (int i = 0; i < pos - 1 && atual->next != NULL; i++) {
        atual = atual->next;
    }
    
    temp->next = atual->next;
    temp->prev = atual;
    
    if (atual->next != NULL) {
        atual->next->prev = temp;
    }
    atual->next = temp;
}

void removerMeio(listNode **l, int pos) {
    if (*l == NULL) return;
    
    listNode* atual = *l;
    for (int i = 0; i < pos && atual->next != NULL; i++) {
        atual = atual->next;
    }
    
    if (atual->prev != NULL) {
        atual->prev->next = atual->next;
    } else {
        *l = atual->next;
    }
    
    if (atual->next != NULL) {
        atual->next->prev = atual->prev;
    }
    free(atual);
}

void mostrarLista(listNode *l) {
    printf("[");
    for (listNode* i = l; i != NULL; i = i->next) {
        printf(" %d ", i->data);
    }
    printf("]\n");
}

int main() {
    listNode* l;
    criaLista(&l);

    adicionarFim(&l, 1);
    adicionarFim(&l, 2);
    adicionarFim(&l, 3);
    mostrarLista(l);
    
    removerFim(&l);
    mostrarLista(l);
    
    adicionarMeio(&l, 4, 1);
    mostrarLista(l);
    
    removerMeio(&l, 1);
    mostrarLista(l);
    
    return 0;
}