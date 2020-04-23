def merge(arr):
	if len(arr) > 1:
		m = len(arr)//2

		L = arr[:m]
		R = arr[m:]

		n1 = len(L)
		n2 = len(R)

		merge(L)
		merge(R)

		i = 0
		j = 0
		k = 0
		while i < n1  and j < n2 :
			if L[i] <= R[j] :
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k+=1

		while i < n1 :
			arr[k] = L[i]
			i += 1
			k += 1
		while j < n2:
			arr[k] = R[j]
			j += 1
			k += 1

arr = [20,12,1,21,6,8]
n = len(arr)
# print ("Given Array : ")
# for i in range(n):
# 	print("%d" %arr[i]),

merge(arr)
print("\n Sorted array is")
for i in range(n):
	print("%d" %arr[i])# your code goes here