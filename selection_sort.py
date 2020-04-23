# Python program for implementation of Selection
# User Inputs the values
size=int(input("Enter Size:"))
l=[0]*size
for i in range(size):
    l[i]=int(input("Enter Digit"))
print ('The defined array is',l)

# Traverse through all array elements
for i in range(size):

    # Find the minimum element in remaining
    # unsorted array
    k = i
    for j in range(i+1, size):
        if l[k] > l[j]:
            k = j

    # Swap the found minimum element with
    # the first element
    l[i],l[k]=l[k], l[i]

# Driver code to test above
print ("Sorted array")
for i in range(size):
    print("%d" %l[i]),