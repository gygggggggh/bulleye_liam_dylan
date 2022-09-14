# mini projet
from random import choices

point = 0,10,20,30,40
for i in range(100):
    test = (choices(point , weights= (50,0,5,10,35)))#Fast Overarm 
    print(f'vous avez gagner {test} point')



