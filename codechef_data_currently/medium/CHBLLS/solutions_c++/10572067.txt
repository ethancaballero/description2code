#include<bits/stdc++.h>
using namespace std;

int main(){
int input1=0;
cout<<1<<endl;
fflush(stdout);
cout<<"3"<<" "<<"1"<<" "<<"2"<<" "<<"2"<<endl;
fflush(stdout);
cout<<"3"<<" "<<"3"<<" "<<"4"<<" "<<"4"<<endl;
fflush(stdout);
fflush(stdin);
cin>>input1;
if(input1==0){
	cout<<"2"<<endl<<"5";
	fflush(stdout);
	exit(0);
	}
else if(input1==1){

	cout<<"2"<<endl<<"3";
	fflush(stdout);
	exit(0);
 }
else if(input1==2){

	cout<<"2"<<endl<<"4";
	fflush(stdout);
	exit(0);
 }
else if(input1==-1){

	cout<<"2"<<endl<<"1";
	fflush(stdout);
	exit(0);
 }
else if(input1==-2){
	cout<<"2"<<endl<<"2";
	fflush(stdout);
	exit(0);
 }
fflush(stdout);
return 0;
}
