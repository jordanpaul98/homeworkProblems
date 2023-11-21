#include <iostream>
#include <vector>
using namespace std;

void SortVector(vector<int>& v){
   int n = v.size(), temp;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (v[j] < v[j + 1]) {
                temp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = temp;
            }
        }
    }
}

int main() {
   int n, val, i;
   cin >> n;
   
   vector<int> vals;

   for (i = 0; i < n; i++) {
     cin >> val;

     vals.push_back(val);
   }
   
   SortVector(vals);

   for (i = 0; i < n; i++) {
     cout << vals.at(i) << ",";
   }
   
   cout << endl;

   return 0;
}
