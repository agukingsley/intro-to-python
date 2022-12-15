#write a pogram that generates 50 random numbers such that the firsyt number is b/w i and 2 the second is b/w i and 3
#from random import randrange
#for i in  range(1,51):
#    num=randrange(1,51)
#    print('1',num)

from random import randint

for i in range(51):
    num=randint(1,3)
    print(num)