#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

int main(){

int n,min,max,area,ind,ind1;

cin>>n;
int arr[n-1];
for(int i = 0;i<n;i++)
{
int x1,x2,x3,y1,y2,y3;
cin>>x1>>y1>>x2>>y2>>x3>>y3;
area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2));
arr[i] = area;
};


min = arr[0];
max = arr[0];
for(int i = 1;i<n;i++)
{

if(arr[i]<=min){
min= arr[i];
ind = i+1;
}


};

for(int i = 1;i<n;i++)
{
if(arr[i]>=max){
max= arr[i];
ind1 = i+1;
}
};

cout<<ind<<" "<<ind1;


return(0);
};