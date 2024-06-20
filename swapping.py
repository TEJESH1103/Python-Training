#swapping 1st and last element in a list
input1 = input("Enter the elements of the list 1 separated by spaces: ")

list1 = input1.split()

list1[0],list1[-1]=list1[-1],list1[0]
print(list1)
