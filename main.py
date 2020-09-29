n=18
print('You can gessess 9 times\n')
a=9
b=0
while b<a :
    _=int(input('Enter your guesses coice:-\n'))
    if _==n:
        print("Congratlution u gusses the right number")
        break
    if _>n:
        print("You enter big number\n""Try small number")
    if _>1 and _<n:
        print("Try again ur close\n""Incress the number")
    if (b+1==a):
        print("Game over")
    elif _>100:
        print("Try 30-10")
    print('Your guess number:', b + 1, '\n', )
    b=b+1