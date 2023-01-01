n = int(input())

cycle = 1
# first check and define num , in this if quote use 'n'

if n <10:
  num = n*10+n
else:
  num2 = (n//10 +n%10)%10
  num = (n%10)*10 +num2

  
# and while check and define num , in this if quote use 'num'  
while num != n:
  
  if num < 10:
    num= num*10+num
    cycle+=1
    
  else:
    num2 = (num//10+num%10)%10
    num =  (num%10)*10 +num2 
    cycle+=1
    
print(cycle)
