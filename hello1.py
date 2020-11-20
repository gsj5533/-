import datetime
import numpy as np
from chinese_calendar import is_workday
import time
from Crypto.Random.random import randint
from dask import sizeof
from _ast import In
from _io import open
from airtest.core.api import text
print('hello python')
robTime = time.strftime('%H%M', time.localtime())
print(robTime)

i = 0
red = np.arange(1,35)
blue = np.arange(1,12)
while i < 5 :
    i +=  1
    np.random.shuffle(red)
    np.random.shuffle(blue)
    r = red[0:5]
    b = blue[0:2]
    print('前驱：' , r)
    print('后驱：' , b)
# np.savetxt("1.txt",red[0:5],fmt='%d',delimiter="/n")
# np.savetxt("1.txt",blue[0:2],fmt='%d',delimiter="/n")
    with open('D:\\test.txt','a',encoding='utf-8') as f:
        text1 = ','.join(str(i) for i in r)
        text2 = ','.join(str(i) for i in b)
        f.write(r + '\n')
        f.write(b + '\n')
        
#a = np.random.randint(36,size = (5,5))
#b = np.random.randint(13,size = (5,2))
#print(a,b)