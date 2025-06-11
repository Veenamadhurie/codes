data = int(input())

reversed_data = 0

while data > 0:
    digit = data % 10
    reversed_data = reversed_data * 10 + digit
    data = data // 10
    
print(reversed_data)