h, m = map(int, input().split())
n    = int(input())
if n+m>59:
    h+= (m+n)//60 # keypoint1
    m = (m+n)%60 # keypoint2
else:
    m += n
  
if h>23:
    h=h%24 # keypoint3
print(h,m)
