#include <stdio.h>
#include <stdlib.h>

#define SIZE 6  // Fixed size of the array (vector)

struct CircularList {
    int v[SIZE];  // Array to hold elements
    int first;    // Index of the first element
    int last;     // Index of the last element
};

// Initialize the circular list
void initializeList(struct CircularList* list) {
    list->first = -1;  // List is empty initially
    list->last = -1;   // List is empty initially
}

// Check if the list is full
int isFull(struct CircularList* list) {
    return (list->first == (list->last + 1) % SIZE);
}

// Check if the list is empty
int isEmpty(struct CircularList* list) {
    return (list->first == -1);
}

// Insert at the end
void insertAtEnd(struct CircularList* list, int data) {
    if (isFull(list)) {
        printf("Error: List is full.\n");
        return;
    }

    if (isEmpty(list)) {
        list->first = 0;
        list->last = 0;
    } else {
        list->last = (list->last + 1) % SIZE;
    }
    list->v[list->last] = data;
}

// Insert at the beginning
void insertAtBeginning(struct CircularList* list, int data) {
    if (isFull(list)) {
        printf("Error: List is full.\n");
        return;
    }

    if (isEmpty(list)) {
        list->first = 0;
        list->last = 0;
    } else {
        list->first = (list->first - 1 + SIZE) % SIZE;
    }
    list->v[list->first] = data;
}

// Delete from the beginning
void deleteAtBeginning(struct CircularList* list) {
    if (isEmpty(list)) {
        printf("Error: List is empty.\n");
        return;
    }

    if (list->first == list->last) {  // Only one element
        list->first = -1;
        list->last = -1;
    } else {
        list->first = (list->first + 1) % SIZE;
    }
}

// Delete from the end
void deleteAtEnd(struct CircularList* list) {
    if (isEmpty(list)) {
        printf("Error: List is empty.\n");
        return;
    }

    if (list->first == list->last) {  // Only one element
        list->first = -1;
        list->last = -1;
    } else {
        list->last = (list->last - 1 + SIZE) % SIZE;
    }
}

// Display the list
void displayList(struct CircularList* list) {
    if (isEmpty(list)) {
        printf("[]\n");
        return;
    }

    printf("[");
    int i = list->first;
    while (i != list->last) {
        printf(" %d ", list->v[i]);
        i = (i + 1) % SIZE;
    }
    printf(" %d ", list->v[list->last]);
    printf("]\n");
}

// Main function to test
int main() {
    struct CircularList* list = (struct CircularList*) malloc(sizeof(struct CircularList));

    if (!list) {
        printf("Failed to allocate memory for the list.\n");
        return 1;
    }

    initializeList(list);

    insertAtEnd(list, 10);
    insertAtEnd(list, 20);
    insertAtEnd(list, 30);
    insertAtBeginning(list, 5);

    displayList(list);  // Output: [ 5 10 20 30 ]

    deleteAtBeginning(list);
    displayList(list);  // Output: [ 10 20 30 ]

    deleteAtEnd(list);
    displayList(list);  // Output: [ 10 20 ]

    free(list);
    return 0;
}
