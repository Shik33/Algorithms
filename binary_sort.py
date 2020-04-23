def binary_sort(alist):
    for i in range(1,len(alist)):
        temp = alist[i]
        pos = binary_search(alist,temp,0,i) + 1
        for k in range(i, pos, -1):
            alist[k] = alist [k-1]
        alist[pos] = temp

def binary_search(alist, k, s, e):
    if e - s <= 1:
        if k < alist[s]:
            return s - 1
        else:
            return s
    m = (s + e)//2
    if alist[m] < k:
        return binary_search(alist, k, m, e)
    elif alist[m] > k:
        return binary_search(alist, k, s, m)
    else:
        return m
 
# arr = [1,5,34,86,3,42,2,8]
# n = len(arr)
# binary_sort(arr)
# print("Sorted array is:")
# for i in range(n):
#    print(arr[i]) 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
binary_sort(alist)
print('Sorted list: ', end='')
print(alist)