#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {

   vector<string> words;
   vector<int> freq;
   
   int i, j, n;
   string str;
   
   cin >> n;
   
   for (i=0; i<n; i++){
      cin >> str;
      words.push_back(str);
      freq.push_back(0);
   }
   
   for (i=0; i<n; i++){
      for (j=0; j<n; j++){
         if (words.at(i) == words.at(j)){
            freq.at(i) += 1;
         }
      }
   }
   
   for (i=0; i<n; i++){
      cout << words.at(i) << " - " << freq.at(i) << endl;
   }

   return 0;
}
