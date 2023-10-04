from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_idx = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_to_idx:
            return [num_to_idx[complement], idx]
        
        num_to_idx[num] = idx
    
    return