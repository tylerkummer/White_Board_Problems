class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use dictionary to map what we are looking for
        values = dict()
        # Use for loop an enumerate to go over all the numbers in the array
        for i, elem in enumerate(nums):
            # Create compliment of value for every element
            comp = target - elem
            # Check if complement is in the dictionary
            if comp in values:
                # Return the sum up of the target value
                return [values[comp], i]
            # Compliment not in the array continue onto next element
            values[elem] = i
