class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end(), less<int>());
        sort(s.begin(), s.end(), less<int>());
        
        int happy_children = 0;
        
        int cookieIndex = 0;
        int childIndex = 0;

        while((cookieIndex < s.size()) && (childIndex < g.size())) {
            if(s[cookieIndex] >= g[childIndex]) {
                happy_children++;
                cookieIndex++;
                childIndex++;
            } else {
                cookieIndex++;
            }
        }
    
        return happy_children;
    }
};