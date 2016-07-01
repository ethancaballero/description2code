#include<bits/stdc++.h>

using namespace std;

int main(){
    	long long T;
    	cin>>T;
    	while(T--){
            int N,M;
            cin>>N>>M;
            int A[N];
            for(int i=0;i<N;i++){
                cin>>A[i];
            }
            int max=*max_element(A,A+N);
            long long count=0;
            for(int i=0;i<N;i++){
                count+=max-A[i];
            }
            if(count==M){
                cout<<"Yes";
            }
            else if(count<M){
                int count1=M-count;
                if(count1%N==0){
                    cout<<"Yes";
                }
                else{
                    cout<<"No";
                }
            }
            else{
                cout<<"No";
            }
            cout<<endl;
    }
//system("pause");
return 0;
}
