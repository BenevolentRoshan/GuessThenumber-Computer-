import random

def guess(x):
    low=1
    high=x
    feedback=""
    while feedback!='c' and low!=high:
        guess=random.randint(low,high)
        print(guess)
        feedback=input("type correct='c', Low='l', high='h': ").lower()
        if feedback=='l':
            low=guess+1
        elif feedback=='h':
            high=guess-1
        else:
            return guess
    return low

x=int(input("Enter the range from 1 to : "))
print(f"yay computer guees the number which is {guess(x)}")

