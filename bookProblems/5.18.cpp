#include <iostream>
#include <vector>   // Must include vector library to use vectors
using namespace std;

int main() {
   vector<int> userInts; // A vector to hold the user's input integers
   
   int num, val;
   cin >> num;
   
   for (int i = 0; i < num; i++){
      cin >> val;
      userInts.push_back(val);
   }

   for (int i = userInts.size() - 1; i >= 0; i--){
      cout << userInts.at(i) << ",";
   }
   
   cout << endl;

   return 0;
}
