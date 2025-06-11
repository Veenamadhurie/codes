s = input().strip()

if len(s) > 1 and s.isdight():
    r = int(s[:-2]) if len(s) > 2 else int(s[0])
    h = int(s[-2:]) if len(s) > 2 else int(s[1])
else:
    
    r = int(s)
    h = int(input())
    
surface_area = 2 * 3.14 * r * (r + h)
volume = 3.14 * r * r * h

print(f"{round(surface_area, 1)}")
print(f"{round(volume, 1)}")