first=1
last=5
perfect_cube=False
for i in range(1,last+1):
    if i**3<=last and i**3>=first:
        perfect_cube=True
if perfect_cube==False:
    print('There is no perfect cube b/w 100 and 200')
else:
    print('There is at least one perfect cube exist b/w 100 & 2000')
    