#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {

   vector<double> vals;
   int n, i;
   double val, mx = 0;
   
   cin >> n;
   for (i=0; i < n; i++){
      cin >> val;
      vals.push_back(val);
      if (val > mx) mx = val;
   }
   
   for (i=0; i < n; i++){
      vals.at(i) = vals.at(i) / mx;
      cout << fixed << setprecision(2) << vals.at(i) << " ";
   }
   
   cout << endl;

   return 0;
}
