/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
 */

// @lc code=start
#include <iostream>
#include<vector>

using namespace std;
class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        if(nums.size() == 0) 
            return -1;
        int right = nums.size()-1;
        int left = 0;
        while (right >= left 
            && right < nums.size() 
            && left > -1)
        {
            /* 二分遍历 */
            int mid = (left+right)/2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid+1;
            } else if (nums[mid] > target) {
                right = mid-1;
            }
            std::cout << mid << endl;
        }
        return -1;
      
    }
};
// @lc code=end

// int main() 
// {
//     Solution s = Solution();
//     int data[] = {-1,0,3,5,9,12};
//     std::vector<int> input_data(data, data + sizeof(data) / sizeof(int));
//     std::cout << s.search(input_data, 2) << endl;
// }
