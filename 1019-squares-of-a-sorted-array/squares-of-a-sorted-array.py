class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # 1. Square all elements in-place (all values are now in [0, 10^8])
        for i in range(n):
            nums[i] *= nums[i]
            
        SHIFT = 27
        MASK = (1 << SHIFT) - 1  # Extracts the lower 27 bits (original square)
        
        # 2. Two-pointer merge, encoding the sorted result in the upper 27 bits
        left, right = 0, n - 1
        for write in range(n - 1, -1, -1):
            left_val = nums[left] & MASK
            right_val = nums[right] & MASK
            
            if left_val > right_val:
                nums[write] |= (left_val << SHIFT)
                left += 1
            else:
                nums[write] |= (right_val << SHIFT)
                right -= 1
                
        # 3. Shift right to discard the old values and keep the sorted results
        for i in range(n):
            nums[i] >>= SHIFT
            
        return nums