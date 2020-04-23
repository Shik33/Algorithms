def partition(arr, l , h):
    i = (l - 1)
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] =  arr[h], arr[i+1]
    return(i+1)

def  quick_sort(arr,l,h):
    if l < h :
        pi = partition(arr,l,h)
        quick_sort(arr,l,pi-1)
        quick_sort(arr,pi+1,h)

if __name__ == '__main__':
    arr = [10,20,11,30,7,1,81]
    n = len(arr)
    quick_sort(arr,0,n-1)
    for i in range(n):
        print("%d" %arr[i])