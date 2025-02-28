def merge_sort(arr): 
    # Base case if 0 or 1 element is already sorted 
    if len(arr) <= 1: 
        return arr 

    # Find the middle point to divide the array into two halves 
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:]) 
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    # Compare elements from both halves and merge then to the result
    while i< len(left) and j <len(right): 
        if left[i] < right[j]:
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j])
            j += 1 
        
    # Append only remaining elements 

    result.extend(left[i:])
    result.extend(right[j:])
    return result 

if __name__ == "__main__": 
    unsorted_list = [38, 29, 43, 9, 3, 32, 21]
    sorted_list = merge_sort(unsorted_list)
    print(f"Sorted list: {sorted_list}")