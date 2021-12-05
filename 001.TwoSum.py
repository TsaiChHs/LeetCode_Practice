def twoSum(nums, target):
    nums = list(enumerate(nums))
    nums.sort(key = lambda s : s[1])
    for i in range(len(nums)-1, 0, -1):
        # Check 相符
        for j in range(i):
            sums = nums[i][1] + nums[j][1]
            if sums == target:
                return [nums[j][0], nums[i][0]]

if __name__ == '__main__':
    print( twoSum(nums = [2,7,11,15], target = 9) )
    print( twoSum(nums = [3,2,4], target = 6) )
    print( twoSum(nums = [3,3], target = 6) )