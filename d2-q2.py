N = int(input())

product = 1

while N > 0:
    digit = N % 10
    product *= digit
    N = N // 10
        
print(product)        