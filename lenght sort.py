input1 = input("Enter the elements of the list 1 separated by spaces: ")

list1 = input1.split()

list1.sort(key=len)

print(list1)
