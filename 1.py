#**************Q1****************#
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_ += nums[i]
        return sum_

# Time : 356 ms
# Memory : 16.7 M

#**************Q2****************#
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(candyType)//2
        b=len(set(candyType))
        return min(a,b)
    
    #**************Q3****************#
    class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_length = 0
        
        for key in freq:
            if key + 1 in freq:
                max_length = max(max_length, freq[key] + freq[key+1])
                
        return max_length
    
    #**************Q4****************#
    class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
    
    #**************Q5****************#
    class Solution:
    def maximumProduct(self, vec: List[int]) -> int:
        if len(vec) == 3:
            return vec[0] * vec[1] * vec[2]
        max1 = max2 = max3 = -1000 
        min1 = min2 = 1000
        for i in vec:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return max(max1 * max2 * max3, min1 * min2 * max1)
    
     #**************Q6****************#
     class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    #**************Q7****************#
    class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[-1] < A[0]: 
            A = A[::-1]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
    
    #**************Q8****************#
    class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        else:
            return max(0,max(nums)-min(nums)-2*k)


    

    
    
        