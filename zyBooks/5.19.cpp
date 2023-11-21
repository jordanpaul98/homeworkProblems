#include <iostream>
#include <vector>   // Must include vector library to use vectors
using namespace std;

int main() {
   
   vector<int> vals;

   int num;
   cin >> num;
   
   while (num != -1){
      vals.push_back(num);
      cin >> num;
   }
   
   if (vals.size() > 9){
      cout << "Too many numbers" << endl;
   }else{
      cout << "Middle item: " << vals.at(vals.size() / 2) << endl;
   }

   return 0;
}
