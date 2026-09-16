class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = 0
        right[n - 1] = 0

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
        for j in range(n - 2, -1, -1):
            right[j] = right[1 + j] + nums[j + 1]
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1
