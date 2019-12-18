#include <iostream>
using namespace std;

int Binary(int arr[], int n,int l, int k)
{
	int m;
	
	if (n >= l)
	m = (l+(n-1)) / 2;
	if (arr[m] == k)
		return (m);
	else if (arr[m] > k)
		return(Binary(arr, m - 1, l, k));
	else if(arr[m] < k)
		return(Binary(arr, n, m+1, k));
	return(-1);
	
}
int main() {
	int arr[]={10,20, 30,40,44,50};
	int k;
	int n;
	int p;
	
	k=40;
	n = sizeof(arr) / sizeof (arr[0]);
	p=Binary(arr, n-1, 0, k);
	if (p == -1)
	cout<<"Number not present"<<endl;
	else
	cout<<p<<endl;
	return 0;
}
