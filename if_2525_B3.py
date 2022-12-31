h, m = map(int, input().split())
n    = int(input())
if n+m>59:
    h+= (m+n)//60 # keypoint
    m = (m+n)%60 # keypoint
else:
    m += n
  
if h>23:
    h=h%24 # keypoint
print(h,m)
