#include<iostream>
#include<climits>
int main(){
    
    int n,k,i,j,a,ptr;
    long long A[100005];
    long long d,e,ft,sft,sd;
    sft = INT_MAX;
    sd = INT_MIN;
    std::cin>>n>>k;
    
    for( i=0 ; i<n ; i++ )
         std::cin>>A[i];
    
    for( i=0 ; i<k+2 ; i++ ){
         
         for( j=i+1 ; j<=k+2 ; j++ ){
              
              e = A[j]-A[i];
              d = e/(j-i);
              
              if( d*(j-i) == e ){
                  
                  ft = A[i] - d*i;
                  ptr = k;           
                  
                  for( a=0 ; a<n ; a++ ){
                  
                       if( ft != A[a] )
                           ptr--;
                           
                       if( ptr < 0 ) 
                           break;
                                   
                       ft += d;
                  }
              }           
              
              if( ptr >= 0 ){
                  ft = A[i] - d*i;
                  
                  if( ft < sft || ( ft == sft && sd > d ) ){
                      sft = ft;
                      sd = d;    
                  }    
              }
         }     
         
    }
    
    for ( i=0 ; i<n ;i++ ){
        std::cout<<sft<<" ";
        sft += sd;    
    }
    
    return 0;
        
}
