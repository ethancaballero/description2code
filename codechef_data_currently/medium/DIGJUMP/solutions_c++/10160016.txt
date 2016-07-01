#include<iostream>
#include<string>
#include<cstring>
#include<queue>
using namespace std;
queue<int> Q;
bool vis[100004];
int d[1000004];
vector<int> V[10];
int main()
{
   string s;
   cin>>s;
   memset(vis, false, sizeof vis);

   int sz = s.size();

   for(int i=1;i<sz;i++)
   {
     int val = s[i]-'0';
     V[val].push_back(i);
   }

   d[0] = 0;
   vis[0]  = true;
   Q.push(0);

   while(!Q.empty())
   {
      int idx = Q.front();
      if(idx == sz-1)
      break;
      Q.pop();

      int val = s[idx]-'0';
      int vsz = V[val].size();
      for(int j=0; j<vsz; j++)
       {
          int nidx = V[val][j];
          if(!vis[nidx])
          {
            vis[nidx]  = true;
            Q.push(nidx);
            d[nidx] = d[idx]+1;
          }
       }
       V[val].clear();

       if(idx-1 >=0 && !vis[idx-1])
       {
         vis[idx-1] = true;
         Q.push(idx-1);
         d[idx-1] = d[idx] + 1;
       }

       if(idx+1<sz && !vis[idx+1])
       {
         vis[idx+1] = true;
         Q.push(idx+1);
         d[idx+1] = d[idx] + 1;
       }
   }

   cout<<d[sz-1]<<endl;
   

	return 0;
}