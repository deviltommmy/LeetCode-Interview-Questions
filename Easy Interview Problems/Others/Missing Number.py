class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        for i in range(a+1):
            if i not in nums:
                return i

obj = Solution()
print(obj.missingNumber([3,0,1]))
