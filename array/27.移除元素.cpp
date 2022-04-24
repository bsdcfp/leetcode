/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 *
 * https://leetcode-cn.com/problems/remove-element/description/
 *
 * algorithms
 * Easy (59.51%)
 * Likes:    1273
 * Dislikes: 0
 * Total Accepted:    660.8K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,2,2,3]\n3'
 *
 * 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
 * 
 * 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
 * 
 * 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
 * 
 * 
 * 
 * 说明:
 * 
 * 为什么返回数值是整数，但输出的答案是数组呢?
 * 
 * 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
 * 
 * 你可以想象内部操作如下:
 * 
 * 
 * // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
 * int len = removeElement(nums, val);
 * 
 * // 在函数里修改输入数组对于调用者是可见的。
 * // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
 * for (int i = 0; i < len; i++) {
 * print(nums[i]);
 * }
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [3,2,2,3], val = 3
 * 输出：2, nums = [2,2]
 * 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而
 * nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0,1,2,2,3,0,4,2], val = 2
 * 输出：5, nums = [0,1,4,0,3]
 * 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0,
 * 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * 0 
 * 0 
 * 
 * 
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty()) return 0;
        int pt_search = 0, pt_res = nums.size();
        /* 
        * 1. res表示最终结果，初始值res为nums.size()，search一直找。默认返回res
        * 2. search指针从0开始找，每找到一个数字需要判断一下，是否等于target
        * 3. 如果等于，判断res是否是数组长度，是就用res记录search位置，不是，那么res不变，search+1
        * 4. 如果不等于，判断res是否是数组长度，是，res不变，search+1；不是，res和search交换，然后都+1
        * 5. 重复3-4，最后返回res
        */
        while (pt_search < nums.size())
        {
            if (nums[pt_search] == val)
            {
                if (pt_res == nums.size())
                {
                    pt_res = pt_search;
                    pt_search += 1;
                }
                else
                {
                    pt_search += 1;
                }
            }
            else
            {
                if (pt_res == nums.size())
                {
                    pt_search += 1;
                }
                else
                {
                    nums[pt_res] = nums[pt_search];
                    pt_res += 1;
                    pt_search +=1;
                }
            }
        }
        return pt_res;
    }
};
// @lc code=end

int main() 
{
    Solution s = Solution();
    vector<int> inp = {0,1,2,2,3,0,4,2};
    std::cout << s.removeElement(inp, 2) << endl;

}

