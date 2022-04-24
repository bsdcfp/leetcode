/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (76.71%)
 * Likes:    687
 * Dislikes: 0
 * Total Accepted:    187.6K
 * Total Submissions: 245.2K
 * Testcase Example:  '3'
 *
 * 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 3
 * 输出：[[1,2,3],[8,9,4],[7,6,5]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：[[1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 
 * 
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector< vector<int> > generateMatrix(int n) {
        /* 流程：
        * 1. 确认需要循环多少次
        * 2. 每次循环，负责填充一个完整时钟环。通过一个自增游标来赋值，控制到游标的走向。
        * 3. 每次循环，分为四个步骤，如何每两个步骤的衔接元素？
        * 4. n=奇数时，最后一个元素是不需要循环的。
        * 5. 单次循环结束，更新起始x、y坐标值
        */
       vector<vector<int> > res(n, vector<int>(n, 0));

       int loop = 1; 
       int x = 0, y = 0;
       int cur = 1;
       while (loop <= int((n-1)/2)+1)
       {
           int i = x, j = y;
           while (j < n-1-y)
           {
               res[i][j] = cur++;
               j++;
           }
           while (i < n-1-x)
           {
               res[i][j] = cur++;
               i++;
           }
           while (j > y)
           {
               res[i][j] = cur++;
               j--;
           }
           while (i > x)
           {
               res[i][j] = cur++;
               i--;
           }
           x = loop;
           y = loop;
           loop += 1;
       }

       if (n % 2 == 1)
       {
           res[int(n/2)][int(n/2)] = n * n;
       }
       
       return res;
    }
};

// int main() 
// {
//     Solution s;
//     vector<vector<int> > res = s.generateMatrix(7);
//     for (int i = 0; i < res.size(); i++)
//     {
//         for (int j = 0; j < res[0].size(); j++)
//         {
//             std::cout << res[i][j] << "\t";
//         }
//         std::cout << endl;
        
//     }
    
// }
// @lc code=end

