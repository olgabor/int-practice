# Given n non-negative integers a1, a2, ..., an , where each 
# represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# https://leetcode.com/problems/container-with-most-water/ 
# Notice that you may not slant the container.

# area = length of shorter vertical line * distance beetwen lines 
height = [1,8,6,2,5,4,8,3,7]


def maxArea(height):
    l = 0 
    r = len(height) - 1 
    maxarea = 0 
    # print(r, len(height))
    # maxarea = 
    # print(maxarea)
    
    while l < r:
        area =  (min(height[l], height[r])) * (r - l)  
        maxarea = max( maxarea, area)  
        if height[l] < height[r]:
            l += 1 
        else: 
            r -= 1 

    return maxarea
        

print(maxArea(height))

# print((height[0], height[8] * 8))
