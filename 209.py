
def minSubArrayLen(target, nums):

    j = 0
    curr = nums[0]
    ans = 0

    for i in range(len(nums)):
        
        while curr < target and j < len(nums) - 1:
            j += 1
            curr += nums[j]
        
        if curr >= target:
            if not ans:
                ans = j - i + 1
            else:
                ans = min(ans, j - i + 1)
            print(i, j)
    
    return ans