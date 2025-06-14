# Welcome to solution of LeetCode problems

# 1. Two Sum (Easy)

'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums) + 1):
            for j in range(0, len(nums) + 1):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


a = Solution()
print(a.twoSum([3,3], 6))
'''

##################################################################################################

# 9. Palindrome Number (Easy)

# Solution #1

'''

class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome(-121))

'''


# Solution 2 - we can make our program faster

'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False
        
'''



##############################################################################################3

# 13. Roman to Integer (Easy)

'''
class Solution(object):
    def romanToInt(self, s):
        greek_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        today_nums = [greek_nums[i] for i in s]

        negative_numbers = [today_nums[i] for i in range(len(today_nums) - 1) if today_nums[i] < today_nums[i + 1]]

        return sum(today_nums) - 2 * sum(negative_numbers)

'''

################################################################################################

# 14.








