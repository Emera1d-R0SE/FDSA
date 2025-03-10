def find_second_largest_and_smallest(arr):
    if len(arr) < 2:
        return None, None  # Not enough elements to find second largest and second smallest

    unique_arr = list(set(arr))  # Remove duplicates
    unique_arr.sort()  # Sort the array

    if len(unique_arr) < 2:
        return None, None  # Not enough unique elements

    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]

    return second_largest, second_smallest

# Example usage:
array = [3, 5, 1, 8, -3, 7, 2]
second_largest, second_smallest = find_second_largest_and_smallest(array)
print("Second Largest element:", second_largest)
print("Second Smallest element:", second_smallest)
