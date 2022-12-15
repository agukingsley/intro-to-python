#write a program that print out a list of interger with their square root
#for i in range(1,21,1):
#    print(i,i*i,sep='--')

#write a program that print your name 100 times 
#for i in range(1,101,1):
#    print('Your name')

#write a program to fill screen horizontally and vertically with your name. 
#for i in range(1,501,1):
#    print('Your name',end=' ')
#    print('Your name',i*2)

#write that program that looks like this AAAAAAABBBBBBBBBCDCDCDCDCDCDEFFFFFFG
#for i in range(10):
#    print('A',end='')
#for i in range(10):
#    print('B',end='')
#for i in range(5):
#    print('C',end='')
#    print('D',end='')
#for i in range(5):
#    print('E',end='')
#    print('F',end='')

#write a program that ask the user for their name and how many times to print it the program should print out the user  name the specified number of times 
#for q in range(1):
#    name=input('Enter name: ')
#    no=eval(input('Number of prints: '))
#    result=q*no
#    print(name,)
#    print(no)

#high=eval(input('enter width: '))
#width=eval(input('enter height:'))
#for i in range(high):
#    print('*'*width)
    
#write a program that asks the user how many fibonacci number and then prints that many.
#num=eval(input('enter fibbo number: '))
#first=1
#second=1
#print(first,end=',')
#print(second,end=',')
#for i in range(num-2):
#    third=first+second
#    print(third,end=',')
#    first=second
#    second=third

width=eval(input("Enter width: "))
height=eval(input("Enter height: "))
print('*'*width)
for i in range(height-2):
    print('*',' '*(width-2),'*',sep='')
    print('*',' '*(width-2),'*',sep='')
print('*'*width)