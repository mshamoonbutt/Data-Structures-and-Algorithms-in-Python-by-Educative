'''Built In Function'''
input_str = "LucidProgramming"
print(len(input_str))

'''Iterative Approach'''
def iterative_str_len(input_str):
    count = 0
    for i in input_str:
        count += 1
    return count

'''Recursive Approach'''
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))    