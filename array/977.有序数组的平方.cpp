/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 *
 * https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
 *
 * algorithms
 * Easy (69.01%)
 * Likes:    497
 * Dislikes: 0
 * Total Accepted:    308.2K
 * Total Submissions: 446.6K
 * Testcase Example:  '[-4,-1,0,3,10]'
 *
 * 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [-4,-1,0,3,10]
 * 输出：[0,1,9,16,100]
 * 解释：平方后，数组变为 [16,1,0,9,100]
 * 排序后，数组变为 [0,1,9,16,100]
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [-7,-3,2,3,11]
 * 输出：[4,9,9,49,121]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 10^4
 * -10^4 
 * nums 已按 非递减顺序 排序
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 请你设计时间复杂度为 O(n) 的算法解决本问题
 * 
 * 
 */

// @lc code=start
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        /* 1. 利用非递减的特性，先找到正负分界线。
         * 2. 用两个指针分别标记负数和非负数
         * 3. 从分界线处，负数指针向前，非负数指针向后
         * 4. 比较平方后结果，优先放入较小的值到结果中，同时指针前移或者后移
         * 5. 针对存在相同数值情况，每次只变化一个指针
         * 
         */
        vector<int> res;
        if (nums.empty()) return res;
        int head = 0, tail = nums.size()-1; //两个指针，从两头向中间比较。

        while (head < tail)
        {
            if (nums[head] < 0 and nums[tail] < 0)
            {
                res.push_back(pow(double(nums[head]), 2.0));
                head += 1;                
            } 
            else if (nums[head] >=0 and nums[tail] >=0)
            {
                res.push_back(pow(double(nums[tail]), 2.0));    
                tail -= 1;  
            } 
            else 
            {
                int pos_head = ~(nums[head]-1);
                if (pos_head >= nums[tail])
                {
                    res.push_back(pow(double(pos_head), 2.0));
                    head += 1;
                }
                else
                {
                    res.push_back(pow(double(nums[tail]), 2.0));    
                    tail -= 1;           
                }
            }
            
            //std::cout << "head:" << head << ", " << a << "; tail:" << tail << ", " << b << endl;
        }
        if (head == tail)
        {
            res.push_back(pow(double(nums[head]), 2.0));
        }
        //反转结果
        vector<int> reverse_res;
        for (int i = res.size()-1; i >= 0; i--)
        {
            reverse_res.push_back(res[i]);
        }
        
        return reverse_res;
        
    }
};

// int main() 
// {
//     Solution s = Solution();
//     //vector<int> inp = {-7,-3,2,3,11};
//     vector<int> inp = {-4,-1,0,0,3,10};

//    // vector<int> inp = {-1,-1,1,2,5};
//     vector<int> res = s.sortedSquares(inp);
//     for (size_t i = 0; i < inp.size(); i++)
//     {
//         std::cout << "i: " << i << ", " << inp[i] << ", " << res[i] << endl;
//     }
    

// }

// @lc code=end

