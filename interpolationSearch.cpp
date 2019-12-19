#include <iostream>
using namespace std;

int interpolationSearch(int arr[], int n, int k)
{
	int l;
	int h;
	int p;
	
	l=0;
	h = n - 1;
	while (l <= h && k>=arr[l] && k <=arr[h])
	{
		if (l == h)
		{
			if(arr[l] == k)
				return (l);
		}
	p = l +(((double)(h - l) / (arr[h] - arr[l]))* (k - arr[l]));
	
	if(arr[p] == k)
	return p;
	if (arr[p] < k)
	l = p + 1;
	else
	h = p - 1;
	}
	return (-1);

}

int main() {
	int arr[] = {10, 12, 13, 16, 18, 19, 20, 21,22, 23, 24, 33, 35, 42, 47}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    int x = 47;
    int index = interpolationSearch(arr, n, x); 
    if (index != -1) 
        cout << "Element found at index " << index; 
    else
        cout << "Element not found.";
	return 0;
}
