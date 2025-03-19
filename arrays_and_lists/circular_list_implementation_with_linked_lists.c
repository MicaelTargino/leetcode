#include <stdio.h>;
#include <stdlib.h>; 

struct Node {
    int data;
    struct Node* next;
};

struct CircularList {
    struct Node* first; 
    struct Node* last;
};

// initializeList 
void initializeList(struct CircularList* list) {
    list->first = NULL;
    list->last = NULL;
}

void insertAtBeginning(struct CircularList* list, int data) {
    // Create a new node
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = data;
    
    // If the list is empty
    if (list->first == NULL) {
        newNode->next = newNode;  // Point to itself, as it's the only node
        list->first = newNode;
        list->last = newNode;  // Both first and last are the same for a single node
    } else {
        // Insert at the beginning
        newNode->next = list->first;  // New node points to the current first
        list->first = newNode;  // Update first to the new node
        list->last->next = list->first;  // The last's next should point to the new first
    }
}

// Insert in index
void insertInIndex(struct CircularList* list, int data, int index) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode-> data = data;

    // iterate until index 
    struct Node* node;
    node = list->first;
    for(int i = 0; i < index - 1; i++) {
        node = node->next;
    }

    // modify newNode pointer
    newNode->next = node->next;
    
    // modify original list pointers
    node->next = newNode;

    if(node == list->last) {
        list->last = newNode;
    }
}

// delete node by index 
void deleteInIndex(struct CircularList* list, int index) {
    // If deleting the first node (index == 0)
    if (index == 0) {
        struct Node* oldNode = list->first;
        
        // If there's only one node in the list
        if (list->first == list->last) {
            list->first = NULL;
            list->last = NULL;
        } else {
            list->first = list->first->next;  // Update the first node
            list->last->next = list->first;   // The last node should still point to the first
        }

        free(oldNode);
        return;
    }

    // Traverse to the node just before the one to be deleted
    struct Node* temp = list->first;
    for (int i = 0; i < index - 1 && temp->next != list->first; i++) {
        temp = temp->next;
    }

    struct Node* oldNode = temp->next;
    temp->next = temp->next->next;

    // If we are deleting the last node, update the last pointer
    if (oldNode == list->last) {
        list->last = temp;
    }

    free(oldNode);
}

// deleteAtBeginning 
void deleteAtBeginning(struct CircularList* list) {
    struct Node* oldNode = list->first;
        
    // If there's only one node in the list
    if (list->first == list->last) {
        list->first = NULL;
        list->last = NULL;
    } else {
        list->first = list->first->next;  // Update the first node
        list->last->next = list->first;   // The last node should still point to the first
    }

    free(oldNode);
}

// deleteAtEnd
void deleteAtEnd(struct CircularList* list) {
    struct Node* oldNode = list->last;
        
    // If there's only one node in the list
    if (list->first == list->last) {
        list->first = NULL;
        list->last = NULL;
    } 

    // Traverse to the second-to-last node
    struct Node* temp = list->first;
    while (temp->next != list->last) {
        temp = temp->next;
    }

    temp->next = list->first;
    list->last = temp;
    free(oldNode);
}

// displayList 
void displayList(struct CircularList* list) {
    if (list->first == NULL) {  // Handle the case when the list is empty
        printf("[]\n");
        return;
    }

    printf("[");
    struct Node* temp = list->first;

    // Loop through the circular list and stop when we return to the first node
    do {
        printf(" %d ", temp->data);
        temp = temp->next;
    } while (temp != list->first);  // Stop when we circle back to the first node

    printf("]\n");
}



int main() {
    struct CircularList* l = (struct CircularList*) malloc(sizeof(struct CircularList));

    if(!l) {
        printf("Falha ao alocar lista circular\n");
        return 1;
    }

    initializeList(l);

    insertAtBeginning(l, 1);
    insertAtBeginning(l, 2);
    insertAtBeginning(l, 3);

    insertInIndex(l, 10, 2);

    displayList(l);

    deleteInIndex(l, 2);

    displayList(l);

    deleteAtBeginning(l);

    displayList(l);

    deleteAtEnd(l);

    displayList(l);

    return 0;
}