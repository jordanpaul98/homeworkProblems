#include <iostream>
#include <vector>
using namespace std;

int main() {

   vector<string> words;
   
   string str;
   int n, i, j;
   char c;
   
   cin >> n;
   for (i=0; i<n; i++){
      cin >> str;
      words.push_back(str);
   }
   
   cin >> c;
   
   for (i=0; i<n; i++){
      for(j=0; j<words.at(i).length(); j++){
         if (words.at(i).at(j) == c){
            cout << words.at(i) << ",";
            break;
         }
      }
   }
   
   cout << endl;

   return 0;
}
