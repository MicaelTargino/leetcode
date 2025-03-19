#include <stdio.h>
#include <stdlib.h>

typedef struct listNode {
    int data;
    struct listNode* next;
} listNode;

void criaLista(listNode *l) {
    l->data = 0;
    l->next = NULL;
}

void adcionarInicio(listNode *l, int value) {
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    temp->next = l->next;
    l->next = temp;
}

void removerInicio(listNode* l) {
    if (l->next != NULL) {
        listNode* temp = l->next;
        l->next = temp->next;
        free(temp);
    }
}

void adicionarFim(listNode *l, int value) {
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    temp->next = NULL;
    
    listNode* atual = l;
    while (atual->next != NULL) {
        atual = atual->next;
    }
    atual->next = temp;
}

void removerFim(listNode* l) {
    if (l->next == NULL) return;
    
    listNode* atual = l;
    listNode* anterior = NULL;
    
    while (atual->next != NULL) {
        anterior = atual;
        atual = atual->next;
    }
    
    anterior->next = NULL;
    free(atual);
}

void adicionarMeio(listNode* l, int value, int pos) {
    listNode* temp = (listNode*)malloc(sizeof(listNode));
    temp->data = value;
    
    listNode* atual = l;
    for (int i = 0; i < pos && atual->next != NULL; i++) {
        atual = atual->next;
    }
    
    temp->next = atual->next;
    atual->next = temp;
}

void removerMeio(listNode* l, int pos) {
    if (l->next == NULL) return;
    
    listNode* atual = l;
    listNode* anterior = NULL;
    
    for (int i = 0; i < pos && atual->next != NULL; i++) {
        anterior = atual;
        atual = atual->next;
    }
    
    if (anterior != NULL && atual->next != NULL) {
        anterior->next = atual->next;
        free(atual);
    }
}

void mostrarLista(listNode l) {
    printf("[");
    for (listNode* i = l.next; i != NULL; i = i->next) {
        printf(" %d ", i->data);
    }
    printf("]\n");
}

int main() {
    listNode l;
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