#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;

#define BUCKET_COUNT 6

class node {
    string key;
    int value;
    node* next;

public:
    node(const string& hk, int v) : key(hk), value(v), next(nullptr) {}

    string get_key() const { return key; }
    int get_value() const { return value; }
    node* get_next() const { return next; }

    void set_next(node* n) { next = n; }
    void set_value(int v) { value = v; }
};

class hashmap {
    node* buckets[BUCKET_COUNT];
    int hash_function(const string& input) {
        int acc = 0;
        for (char ch : input) {
            acc += static_cast<int>(ch);  // Sum ASCII values
        }
        return acc % BUCKET_COUNT;
    }
public:
    hashmap() {
        for(int i = 0; i < BUCKET_COUNT; i++) {
            buckets[i] = nullptr;
        }
    }

    void insert(const string& key, int value) {
        int hash_key = hash_function(key);

        // If the bucket is empty, create a new node and assign it to the bucket
        if (buckets[hash_key] == nullptr) {
            buckets[hash_key] = new node(key, value);
            return;
        }

        // Traverse the linked list to check for existing key
        node* curr = buckets[hash_key];
        while (curr->get_next() != nullptr) {
            if (curr->get_key() == key) {
                curr->set_value(value);  // Update the value if key exists
                return;
            }
            curr = curr->get_next();
        }

        // Check the last node for a match
        if (curr->get_key() == key) {
            curr->set_value(value);  // Update the value if key exists
            return;
        }

        // If key doesn't exist, append a new node at the end of the list
        curr->set_next(new node(key, value));
    }

    int search(const string& key) {
        int hash_key = hash_function(key);

        // If the bucket is empty, the key does not exist
        if (buckets[hash_key] == nullptr) {
            throw std::runtime_error("Key not found");
        }

        // Traverse the linked list to search for the key
        node* curr = buckets[hash_key];
        while (curr != nullptr) {
            if (curr->get_key() == key) {
                return curr->get_value();  // Return the value if key is found
            }
            curr = curr->get_next();
        }

        // If traversal completes without finding the key, throw an exception
        throw std::runtime_error("Key not found");
    }
};

int main() {
    // Create a hashmap instance
    hashmap hm;

    // Test cases
    try {
        // Insert key-value pairs
        cout << "Inserting key-value pairs..." << endl;
        hm.insert("apple", 100);
        hm.insert("banana", 200);
        hm.insert("cherry", 300);
        hm.insert("date", 400);
        hm.insert("fig", 500);

        // Search for keys
        cout << "Searching for keys..." << endl;
        cout << "Value for 'apple': " << hm.search("apple") << endl;    // Expected: 100
        cout << "Value for 'banana': " << hm.search("banana") << endl; // Expected: 200
        cout << "Value for 'cherry': " << hm.search("cherry") << endl; // Expected: 300
        cout << "Value for 'fig': " << hm.search("fig") << endl;       // Expected: 500

        // Update an existing key
        cout << "Updating value for 'banana' to 250..." << endl;
        hm.insert("banana", 250);
        cout << "Value for 'banana': " << hm.search("banana") << endl; // Expected: 250

        // Test non-existing key
        cout << "Searching for a non-existing key 'grape'..." << endl;
        cout << "Value for 'grape': " << hm.search("grape") << endl;   // Should throw an exception
    } catch (const std::exception& e) {
        // Handle exceptions
        cerr << "Exception: " << e.what() << endl;
    }

    return 0;
}
