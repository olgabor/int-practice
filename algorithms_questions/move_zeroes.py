#given an array of integers, write a function to move all 0`s to the end while maintaining the relative order of the other elements 


# Move zeroes process: 
#  1. define a variable non_zero where count of the non zero elements will happen 

#  2. run a for loop 
#        within the for loop state the condition to check whether the number != 0 
#               if the number != 0: rewrite the value by index of non_zero element with current element nums[i]
#               increaze the non_zero count by 1 
# 3.  in order to insert all zero elements at the end of the list run the for loop in range of non_zero and len(nums) 
#     and assing nums[i] with 0 


class Solution:

    def moveZeroes(self, nums):
        non_zero = 0
        
        #find non-zero numbers and keep the track 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1 

        for i in range(non_zero, len(nums)):
            nums[i] = 0

        print(nums)


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
s.moveZeroes([0, 0, 9, 1, 0, 3, 12])
s.moveZeroes([1])