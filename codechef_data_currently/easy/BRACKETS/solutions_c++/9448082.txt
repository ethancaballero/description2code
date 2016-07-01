/**
 * author: jachermocilla@gmail.com
 * url:
*/

#include <iostream>
#include <sstream>

using namespace std;

#define ull unsigned long long

ull F(string s){
    ull balance=0;
    ull max_balance=0;
    ull i;
    char c;

    for (i=0;i<s.size();i++){
        c = s.at(i);
        //cout << c;
        if (c=='(')
            balance++;
        else
            balance--;
        max_balance = max_balance>balance?max_balance:balance;    
    }
    return max_balance;
}


int main(){
    ull n,i,j,k;
    string input;

    cin >> n;
    for (i=0;i<n;i++){
        cin >> input;
        //cout << input << endl;
        k = F(input);
        for (j=0;j<k;j++)
            cout << '(';
        for (j=0;j<k;j++)
            cout << ')';
        cout << endl;
    }
    return 0;
}
