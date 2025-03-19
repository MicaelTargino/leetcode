#include <iostream>
#include <vector> 
#include <algorithm> // Para std::max

using namespace std;

int kadane(const vector<int>& arr) {
    if(arr.size() == 0) {
        return 0;
    }

    int current_max = arr[0];
    int global_max = arr[0];

    for(size_t i = 1; i < arr.size(); i++) {
        current_max = max(arr[i], current_max + arr[i]);
        global_max = max(current_max, global_max);
    }

    return global_max;
}

int main() {
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    int max_sum = kadane(arr);

    cout << max_sum;

    return 0;
}