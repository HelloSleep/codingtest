x,y,z = map(int, input().split())

if x==y==z :
    print(10000+ x*1000)
elif x==y or y == z: #key point1
    print(1000 + y *100)
elif x==z: #key point2
    print(1000 +x *100)
else: #key point3
    print(max(x,y,z)*100)
