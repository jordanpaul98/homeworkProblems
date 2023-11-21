#include <iostream>
#include <vector>
using namespace std;

int main() {

   vector<int> vals;
   int n, i, val, thres;
   
   cin >> n;
   for (i=0; i < n; i++){
      cin >> val;
      vals.push_back(val);
   }
   cin >> thres;
   
   for (i=0; i < n; i++){
      if (vals.at(i) < thres){
         cout << vals.at(i) << ",";
      }
   }
   
   cout << endl;

   return 0;
}
