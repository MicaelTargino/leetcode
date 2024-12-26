#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long max_sum = 0;
        long long window_sum = 0;
        int window_start = 0;

        // Slide the window
        for(int window_end = 0; window_end < nums.size(); window_end++) {
            // Add new element to window
            window_sum += nums[window_end];
            
            // When window size reaches k
            if (window_end - window_start + 1 == k) {
            
                max_sum = max(max_sum, window_sum);
                
                // Remove the starting element
                window_sum -= nums[window_start];
                window_start++;
            }
        }
        
        return max_sum;
    }
};