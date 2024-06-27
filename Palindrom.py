n=int(input("enter any number:"))
i=str(n)

if(i==i[::-1]):
    print("given number",n,"is palindrome")
else:
    print("given number",n,"is not palindrome")
