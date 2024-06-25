# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]   
    return None     