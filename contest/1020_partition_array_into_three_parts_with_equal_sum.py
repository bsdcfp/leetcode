class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        sum_idx = {} # 所有和值的索引
        idx_sum = [] # 每个索引及其之前所有数据的和
        if not A or len(A) < 3:
            return False
        for i in range(len(A)):
            if i == 0:
                idx_sum.append(A[i])
                sum_idx[A[i]] = [i]
                continue
            idx_sum.append(idx_sum[i-1] + A[i])
            if sum_idx.get(idx_sum[i]) is not None:
                sum_idx[idx_sum[i]].append(i)
            else:
                sum_idx[idx_sum[i]] = [i]
        total_sum = int(idx_sum[len(A)-1])
        print(idx_sum)
        if total_sum % 3 == 0:
            equal_sum = total_sum/3
            first = sorted(sum_idx.get(equal_sum))[0]
            second = sorted(sum_idx.get(equal_sum*2))[-1]
            print(equal_sum, first, second)
            if first is not None and second is not None and first < second:
                return True
        return False

A = [29,31,27,-10,-67,22,15,-1,-16,-29,59,-18,48]
s = Solution()
print(s.canThreePartsEqualSum(A))
