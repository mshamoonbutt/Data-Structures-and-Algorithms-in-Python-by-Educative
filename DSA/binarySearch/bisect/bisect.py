# Import allows us to make use of the bisect module.
import bisect

# This sorted list will be used throughout this lesson
# to showcase the functionality of the "bisect" method.
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))