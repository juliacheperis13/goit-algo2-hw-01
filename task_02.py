import random


def quick_select(arr, k):
    """
    Finds the k-th smallest element in an unsorted array using Quick Select.

    :param arr: List of numbers
    :param k: The k-th position (1-based index) of the smallest element to find
    :return: The k-th smallest element
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    def partition(low, high):
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low

        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    def select(low, high, index_to_find):
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if pivot_index == index_to_find:
            return arr[pivot_index]
        elif pivot_index > index_to_find:
            return select(low, pivot_index - 1, index_to_find)
        else:
            return select(pivot_index + 1, high, index_to_find)

    return select(0, len(arr) - 1, k - 1)


array = [3, 2, 1, 5, 4]
k = 2
result = quick_select(array, k)
print(f"The {k}-th smallest element is {result}")
