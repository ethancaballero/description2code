// LADDU : https://www.codechef.com/problems/LADDU

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
  int T;
  cin >> T;

  while(T){
    int activities; string tempString; bool originToken;
    cin >> activities >> tempString;

    originToken = tempString.compare("INDIAN") == 0 ? true : false;

    int sum=0;
    for (int i = 0; i < activities; i++) {
      cin >> tempString;
      if(tempString.compare("CONTEST_WON") == 0){
        int rank;
        cin >> rank;
        rank <= 20 ? sum+= 300 + (20-rank) : sum+= 300;
      }
      else if(tempString.compare("TOP_CONTRIBUTOR") == 0){
        sum+= 300;
      }
      else if(tempString.compare("BUG_FOUND") == 0){
        int severity;
        cin >> severity;
        sum += severity;
      }
      else if(tempString.compare("CONTEST_HOSTED") == 0){
        sum += 50;
      }
    }

    originToken ? cout << sum/200 << endl : cout << sum/400 << endl;


    T--;
  }
  return 0;
}
