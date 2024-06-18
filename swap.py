#swapping 2 numbers using xor

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

a=a^b
b=a^b
a=a^b

print("a=",a)
print("b=",b)
