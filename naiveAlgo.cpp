#include <iostream>
#include<string.h>
using namespace std;
 
void naive(char *p, char *t)
{
	int x;
	int y;
	int i;
	int j;
 
	x = strlen(p);
	y = strlen(t);
	for(i=0;i<y-x;i++)
	{
		for(j=0;j<x;j++)
		{
			if (t[i + j] != p[j])
			break; 
		}
		if (j == x)
		cout<<"Index is"<<i<<endl;
	}
}
int main() {
    char txt[] = "011002AACAADAABAAABAA"; 
    char pat[] = "AABA"; 
    naive(pat, txt); 
    return 0; 
} 