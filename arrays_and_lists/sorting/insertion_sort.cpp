#include <iostream>
#include <vector>

using namespace std;

#define LIST_SIZE 500

vector<int> generate_random_list(int size) {
    vector<int> list; 
    for(int i = 0; i < size; i ++) {
      list.push_back(rand() % 100);
    }
    return list;
}

void print_list(string label, vector<int>& list) {
  cout << label;
  cout << "[";
  for(int i = 0; i < list.size(); i++) {
    if(i < list.size()-1) {
      cout << list[i] << ", ";
    } else {
      cout << list[i];
    }
  }
  cout << "]" << endl;
}

void insertion_sort(vector<int>& unordered_list) {
  int n = unordered_list.size();

  if (n <= 1) {
    return;
  }

  for(int i = 1; i<n; i++) {
    int current = unordered_list[i];
    int j = i - 1;
    while(j>=0 && current<unordered_list[j]) {
      unordered_list[j+1] = unordered_list[j];
      j--;
    }
    unordered_list[j+1] = current;
  }
}

int main() {
  vector<int> list = generate_random_list(LIST_SIZE);  // generate unordered list 
  print_list("Unordered_list: ", list);

 insertion_sort(list); // sort list 

  print_list("Ordered list: ", list);
  return 0;
}