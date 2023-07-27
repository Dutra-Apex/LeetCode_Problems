class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> temp{0, 0, 0};
        
        int i = 0;
        int l = 0;
        int r = nums.size();
        int total_sum = 0;

        while (i < nums.size())
        {
            l = i + 1;
            r = nums.size() - 1;
            while (l < r) {
                total_sum = nums[i] + nums[l] + nums[r];
                if (total_sum < 0) {
                    l += 1;
                } else if (total_sum > 0) {
                    r -= 1;
                } else {
                    temp[0] = nums[i];
                    temp[1] = nums[l];
                    temp[2] = nums[r];
                    ans.push_back(temp);
                    l += 1;
                    
                    while (nums[l-1] == nums[l] && l < r) {
                        l += 1;
                    }
                }
            }
            i += 1;
            while (i < nums.size() && nums[i-1] == nums[i]){
                i += 1;
            }
        }
        return ans;
    }
};
