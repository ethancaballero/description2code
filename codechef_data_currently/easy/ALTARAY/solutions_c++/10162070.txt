#include<iostream>
#include<vector>

using namespace std;

void display(vector<int> outarr)
{
    for(int i = 0; i < outarr.size(); i++)
    {
        cout<<outarr[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        int n;
        cin>>n;

        vector<int> arr, outarr;

        for(int i = 0; i < n; i++)
        {
            int no;
            cin>>no;
            arr.push_back(no);
        }

        int start_pos, end_pos;

        start_pos = end_pos = 0;

        for(int i = 0; i < n; i++)
        {
            start_pos = end_pos = i;
            if(i == 0 || outarr[i - 1] == 1)
            {
                if( (arr[i] > 0 && arr[i + 1] < 0) || (arr[i] < 0 && arr[i + 1] > 0))
                {                
                    for(int j = start_pos + 1; j < n; j++ )
                    {
                        if( (arr[j] > 0 && arr[j + 1] < 0) || (arr[j] < 0 && arr[j + 1] > 0))       
                            continue;
                        else 
                            {
                                end_pos = j;
                                break;
                            }
                    }
                }
                outarr.push_back(end_pos - start_pos + 1);
            }
            else
            {
                outarr.push_back(outarr[i - 1] - 1);
            }                                      
        }
        display(outarr);
    }
    return 0;
}