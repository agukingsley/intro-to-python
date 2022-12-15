#write a program that prints a giant letter A. Allow the user to specify how large the letter should be.
height=eval(input('enter how high the gaint A should be: '))
print(' '*height,'*',sep='')
for n in range(1,height):
    if n !=height//2:
        print(' '*(height-n),'*',(2*n-1)*' ','*',sep='')
    else:
        print(' '*(height-n),'*',(2*n-1)*'*',sep='')