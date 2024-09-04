def two_sum(nums, target):
    num_to_index = {}  # Create a dictionary to store numbers and their indices
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # Return an empty list if no pair is found

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
