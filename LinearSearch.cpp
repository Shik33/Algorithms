#include <iostream>
using namespace std;

int Linearposition(int arr[],int n, int k)
{
	int i;
	
	i=0;
	while (i <= n)
	{
		if (k == arr[i])
			return(i);
		i++;
	}
	return(-1);
}
int main() {
	int arr[] = {10, 02, 30, 40, 50};
	int p;
	int n;
	int k;
	
	k = 40;
	n = sizeof(arr)/sizeof(arr[0]);
	p = Linearposition(arr, n, k);
	if (p == -1)
	cout<<"Number does not exist"<<endl;
	else
	cout<<p<<endl;
	return 0;
}
