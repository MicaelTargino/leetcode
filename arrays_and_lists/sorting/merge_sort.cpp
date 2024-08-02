#include <iostream>
#include <vector>

using namespace std;

#define LIST_SIZE 200

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

void merge(vector<int>& l1, vector<int>& l2, vector<int>& list) {
    int left_size = l1.size();
    int right_size = l2.size();

    int l = 0, r = 0, i = 0;

    while (l < left_size && r < right_size) {
        if (l1[l] < l2[r]) {
            list[i] = l1[l];
            l++;
        } else {
            list[i] = l2[r];
            r++;
        }
        i++;
    }

    while (l < left_size) {
        list[i] = l1[l];
        i++;
        l++;
    }

    while (r < right_size) {
        list[i] = l2[r];
        i++;
        r++;
    }

};

void merge_sort(vector<int>& list) {
    if (list.size() <= 1) {
        return; // recursion base case
    }

    // divide list in two 
    int middle = (int) list.size() / 2;

    vector<int> l1(list.begin(), list.begin() + middle);
    vector<int> l2(list.begin() + middle, list.end());


    // recursive calls 
    merge_sort(l1);
    merge_sort(l2);

    merge(l1,l2, list);
}

int main() {
  vector<int> list = generate_random_list(LIST_SIZE);  // generate unordered list 
  print_list("Unordered_list: ", list);

  merge_sort(list); // sort list 

  print_list("Ordered list: ", list);

  return 0;
}