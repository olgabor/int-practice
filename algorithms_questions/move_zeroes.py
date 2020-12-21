#given an array of integers, write a function to move all 0`s to the end while maintaining the relative order of the other elements 

class Solution:

    def moveZeroes(self, nums):
        non_zero = 0
        
        #find non-zero numbers, keep the track 
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