print()
for i in range(1,11):
    print(i,' ',end='')
print()
for i in range(1,11,2):
    print(i,' ',end='')
print()
for i in range(11,0,-1):
    print(i,' ',end='')
print()
for i in range(11,0,-2):
    print(i,' ',end='')
print()
for i in"kolkata":
    print(i)
    
for i in range(1,11):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")
    
for i in range(1,11):
    if(i==5):
        break
    print(i)

for i in range(1,11):
    if(i==5):
        continue
    print(i)
for i in range(1,11):
    if(i==5):
        pass
    print(i,"444")