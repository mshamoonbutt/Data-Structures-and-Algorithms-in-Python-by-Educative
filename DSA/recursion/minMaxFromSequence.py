'''Recursive Approach'''
def find_max(sequence):
    if len(sequence) == 1:
        return sequence[0]
    else:
        return max(sequence[0], find_max(sequence[1:]))
    
def find_min(sequence):
    if len(sequence) == 1:
        return sequence[0]
    else:
        return min(sequence[0], find_min(sequence[1:]))   
    
sequence = [3, 7, 2, 9, 5, 8, 6, 4, 1]
print("Minimum value:", find_min(sequence))
print("Maximum value:", find_max(sequence))
     