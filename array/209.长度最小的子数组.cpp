/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 *
 * https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (48.38%)
 * Likes:    1092
 * Dislikes: 0
 * Total Accepted:    307.1K
 * Total Submissions: 633.8K
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * 给定一个含有 n 个正整数的数组和一个正整数 target 。
 * 
 * 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
 * ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：target = 7, nums = [2,3,1,2,4,3]
 * 输出：2
 * 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：target = 4, nums = [1,4,4]
 * 输出：1
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * 1 
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
 * 
 * 
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        //用dp[i]，表示长度为i的数组，满足>=target的最小连续子数组长度
        //dp[i+1]和dp[i]有啥关系？dp[i+1]依赖于dp[i]的值
        if (nums.empty())
        {
            return 0;
        }
        //[2,3,1,2,4,3]
        //找到第一个窗口，right=3,left=0，sum=8，
        //缩小窗口，看有没有更合适的。直到窗口为0.
        //增加一个新的元素到窗口里，重复以上步骤
    
        int left = 0, len = 0, sum = 0; //滑动窗口，需要两个指针，len和sum分别记录长度和总和。

        for (int i=0; i < nums.size(); i++)
        {
            sum += nums[i];

            while (sum >= target)
            {
                len = len == 0 ? i-left+1 : min(len, i-left+1);
                sum -= nums[left++]; //非常关键，核心判断条件。记录窗口和的大小，left->i之间就是窗口包含的全部元素
            }
            
            std::cout << left << "," << i << "," << sum << endl;
            
        }
        
        return len;
    }
};

// int main()
// {
//     Solution s;
//     // int target = 7;
//     // vector<int> nums({2,3,1,2,4,3});
//     // int target = 9;
//     // vector<int> nums({1,1,1,1,1,1,1,1});
//     int target = 15;
//     vector<int> nums({5,1,3,5,10,7,4,9,2,8});

//     std::cout << s.minSubArrayLen(target, nums) << endl;
// }
// @lc code=end

