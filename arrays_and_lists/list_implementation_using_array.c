#include <stdio.h>

#define SIZE 10 // Define the maximum size of the list

// Define a structure to represent the list
struct list {
    int data[SIZE]; // Array to store list elements
    int control;    // Index to track the last element in the list
};

// Function to initialize the list
void createList(struct list* l) {
    l->control = -1; // Set control to -1 to indicate an empty list
}

// Function to clear the list
void clearList(struct list* l) {
    l->control = -1; // Reset control to -1 to clear the list
}

// Function to print the list
void printList(struct list l) { 
    if (l.control == -1) { // Check if the list is empty
        printf("[]\n");
        return;
    }

    printf("["); // Start printing the list
    for(int i = 0; i <= l.control; i++) {
        printf("%d", l.data[i]); // Print each element
        if (i <= (l.control - 1)) {
            printf(","); // Add a comma between elements
        }
    }
    printf("]\n"); // End printing the list
}

// Function to append an item to the list
void appendItemToList(struct list* l, int item) {
    if(l->control + 1 == SIZE) { // Check if the list is full
        printf("LIST IS FULL\n");
        return;
    }
    l->data[l->control + 1] = item; // Add the item to the end of the list
    l->control += 1; // Increment the control index
}

// Function to remove the last item from the list
void removeLastItem(struct list* l) {
    if (l->control == -1) { // Check if the list is empty
        printf("LIST IS EMPTY\n");
        return;
    }
    l->control -= 1; // Decrement the control index to remove the last item
}

// Main function to demonstrate the list operations
int main() {
    struct list l1; // Declare a list

    createList(&l1); // Initialize the list

    printList(l1); // Print the empty list

    appendItemToList(&l1, 1); // Append 1 to the list
    appendItemToList(&l1, 2); // Append 2 to the list
    appendItemToList(&l1, 3); // Append 3 to the list

    printList(l1); // Print the list [1, 2, 3]

    removeLastItem(&l1); // Remove the last item (3)

    printList(l1); // Print the list [1, 2]

    clearList(&l1); // Clear the list

    printList(l1); // Print the empty list

    return 0;
}