#include <stdio.h>
#include <stdlib.h>

#define SIZE 6  // Fixed size of the array (vector)

struct CircularQueue {
    int v[SIZE];  // Array to hold queue elements
    int first;    // Index of the front element
    int last;     // Index of the rear element
};

// Initialize the queue
void initializeQueue(struct CircularQueue* queue) {
    queue->first = -1;  // Queue is empty initially
    queue->last = -1;   // Queue is empty initially
}

// Check if the queue is empty
int isEmpty(struct CircularQueue* queue) {
    return (queue->first == -1);
}

// Check if the queue is full
int isFull(struct CircularQueue* queue) {
    return ((queue->last + 1) % SIZE == queue->first);
}

// Enqueue operation (insert at the rear)
void enqueue(struct CircularQueue* queue, int data) {
    if (isFull(queue)) {
        printf("Error: Queue is full.\n");
        return;
    }

    // If the queue is empty
    if (isEmpty(queue)) {
        queue->first = 0;
        queue->last = 0;
    } else {
        queue->last = (queue->last + 1) % SIZE;
    }
    queue->v[queue->last] = data;
    printf("Enqueued: %d\n", data);
}

// Dequeue operation (remove from the front)
int dequeue(struct CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Error: Queue is empty.\n");
        return -1;  // Indicating an error
    }

    int data = queue->v[queue->first];

    // If there is only one element in the queue
    if (queue->first == queue->last) {
        queue->first = -1;
        queue->last = -1;
    } else {
        queue->first = (queue->first + 1) % SIZE;
    }

    printf("Dequeued: %d\n", data);
    return data;
}

// Peek operation (view the front element)
int peek(struct CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Error: Queue is empty.\n");
        return -1;  // Indicating an error
    }
    return queue->v[queue->first];
}

// Display the queue
void displayQueue(struct CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty.\n");
        return;
    }

    printf("Queue: ");
    int i = queue->first;
    while (i != queue->last) {
        printf("%d ", queue->v[i]);
        i = (i + 1) % SIZE;
    }
    printf("%d\n", queue->v[queue->last]);
}

// Main function to test the circular queue
int main() {
    struct CircularQueue* queue = (struct CircularQueue*) malloc(sizeof(struct CircularQueue));

    if (!queue) {
        printf("Failed to allocate memory for the queue.\n");
        return 1;
    }

    initializeQueue(queue);

    enqueue(queue, 10);  // Enqueue 10
    enqueue(queue, 20);  // Enqueue 20
    enqueue(queue, 30);  // Enqueue 30
    enqueue(queue, 40);  // Enqueue 40
    enqueue(queue, 50);  // Enqueue 50
    enqueue(queue, 60);  // Enqueue 60 (this should fail since the queue is full)

    displayQueue(queue);  // Display the queue

    dequeue(queue);  // Dequeue (removes 10)
    dequeue(queue);  // Dequeue (removes 20)

    displayQueue(queue);  // Display the queue

    enqueue(queue, 70);  // Enqueue 70 (this should succeed now)

    displayQueue(queue);  // Display the queue

    printf("Peek: %d\n", peek(queue));  // Peek at the front element

    free(queue);
    return 0;
}
