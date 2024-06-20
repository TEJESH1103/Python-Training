input1 = input("Enter the elements of the list 1 separated by spaces: ")

list1 = input1.split()
unique_list=list(set(list1))

print(unique_list)
