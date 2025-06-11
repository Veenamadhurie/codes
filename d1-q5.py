s = input().strip()

if len(s) == 2:
    b = int(s[0])
    h = int(s[1])
else:
    
    b = int(s)
    h = int(input())
    
area = 0.5 * b * h

print(round(area, 1))