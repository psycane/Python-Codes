import time
from functools import reduce
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm
t1=time.time()
def lcm_of_n(li):
    return reduce(lcm,li)

li=[1,2,3,4,5,6,7,8,9,10]
print(lcm_of_n(li))
t2=time.time()
print(t2-t1)

t3=time.time()
li=[1,2,3,4,5,6,7,8,9,10]
gc=li[0]
prod=li[0]
for i in range(1,len(li)):
   gc=gcd(li[i],gc)
   prod*=li[i]
print(prod//gc)
t4=time.time()
print(t4-t3)


''' 
Code not giving correct answer:
      Providing=>
      Correct,
      Understandable,
      Brute-Force Code
      TC==>O(n)
  With same execution time.
  
  O/P==> of the above code
  2520
  0.016462326049804687
  3628800
  0.005449771881103516
'''
      
