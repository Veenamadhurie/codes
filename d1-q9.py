s = input().strip()

if len(s) > 1 and s.isdigit():
    r = int(s[0])
    h = int(s[1])
    
else:
    
    r = int(s)
    h = int(input())
    
volume = (1.0 / 3.0) * 3.14 * r * r * h

print(f"{volume:.2f}")