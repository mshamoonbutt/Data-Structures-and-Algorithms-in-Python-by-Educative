def log2(n):
    if n <= 1:
        return 0
    else:
        return 1 + log2(n // 2)

n = 32
print("log2({}) = {}".format(n, log2(n)))  
