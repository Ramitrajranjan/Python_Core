import random
# while loop
# x=int(input("Enter the number for which you want table= "))
# i=1
# while(i<11):
#     print(x,'*',i,'=',x*i)
#     i+=1


jackpot=random.randint(1,100)
x=int(input("Enter the guess="))
i=1
while(x!=jackpot):
    if x>jackpot:
        print("Guess lower")
    else:
        print("Guess higher")
    x=int(input("Enter the guess"))
    i=i+1
print("sahi jawab",i)