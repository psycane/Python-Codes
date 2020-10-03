'''edited by Shouvik Dutta
'''
#from fractions import gcd  //We get a deprecation warning // So import gcd from math
from math import gcd
import time   #to check the run time difference of in build function modules using and brute_force & Euclid method using 
t1=time.time()
from functools import reduce
li=[12,16,48]
print (reduce(gcd,li))
t2=time.time()
print(t2-t1)


t3=time.time()
def my_gcd(a,b): 
   while(b): 
       a,b = b,a%b 
   return a
ans_gcd=li[0]
for i in range(1,len(li)):
    ans_gcd=my_gcd(ans_gcd,li[i])
print(ans_gcd)
t4=time.time()
print(t4-t3)


'''
O/P==>
4
0.011922359466552734
4
0.005944013595581055
'''
