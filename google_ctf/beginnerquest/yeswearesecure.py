from hashlib import new


arr =  [52037,  
 52077, 
 52077, 
 52066, 
 52046, 
 52063,
 52081,   
 52081, 
 52085, 
 52077,
 52080,  
 52066
 ]

for v in arr:
    print(chr(v - 0xCafe), end="")