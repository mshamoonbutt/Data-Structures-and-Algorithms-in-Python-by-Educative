'''Iterative Approach'''
vowels = 'aeiou'
def iterative_count_consonants(input_str):
    count = 0
    for i in input_str:
        if i.lower() not in vowels and i.isalpha():
            count += 1
    return count
   
'''Recursive Approach'''
def recursive_count_consonants(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))