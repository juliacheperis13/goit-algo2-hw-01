def find_min_max(arr):
    """
    Finds the minimum and maximum elements in an array using divide and conquer.

    :param arr: List of numbers
    :return: Tuple (min, max)
    """
    if not arr:
        raise ValueError("Array must not be empty")

    def helper(subarray):
        if len(subarray) == 1:
            return subarray[0], subarray[0]

        if len(subarray) == 2:
            return (min(subarray[0], subarray[1]), max(subarray[0], subarray[1]))

        mid = len(subarray) // 2
        left_min, left_max = helper(subarray[:mid])
        right_min, right_max = helper(subarray[mid:])

        return min(left_min, right_min), max(left_max, right_max)

    return helper(arr)


array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_min_max(array)
print(f"Minimum: {result[0]}, Maximum: {result[1]}")
