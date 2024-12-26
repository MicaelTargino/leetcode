#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long max_sum = 0;
        long long window_sum = 0;
        unordered_map<int, int> window_count;
        int window_start = 0;

        // Slide the window
        for(int window_end = 0; window_end < nums.size(); window_end++) {
            // Add new element to window
            window_sum += nums[window_end];
            window_count[nums[window_end]]++;
            
            // When window size reaches k
            if (window_end - window_start + 1 == k) {
                // Check if all elements are distinct
                if (window_count.size() == k) {
                    max_sum = max(max_sum, window_sum);
                }
                
                // Remove the starting element
                window_sum -= nums[window_start];
                window_count[nums[window_start]]--;
                if (window_count[nums[window_start]] == 0) {
                    window_count.erase(nums[window_start]);
                }
                window_start++;
            }
        }
        
        return max_sum;
    }
};