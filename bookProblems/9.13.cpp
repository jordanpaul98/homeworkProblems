#include <iostream>
#include <fstream>

using namespace std;

int main() {

   ifstream file;
   
   string fName;
   
   cin >> fName;
   
   file.open(fName);
   if (!file.is_open()) return 1;
   
   string line;
   while (getline(file, line)){
      int t1, t2, t3;
      
      t1 = line.find("\t");
      t2 = line.find("\t", t1 + 1);
      t3 = line.find("\t", t2 + 1);
      
      //cout << line.substr(t3 + 1, line.length() - t2) << endl;
      
      if (line.substr(t3 + 1, line.length() - t2) == "Available"){
         string food_1 = line.substr(0, t1);
         string food_2 = line.substr(t1 + 1, t2 - t1 - 1);
         string food_3 = line.substr(t2 + 1, t3 - t2 - 1);
         
         cout << food_2 << " (" << food_1 << ") -- " << food_3 << endl;
      }
   }
   
   file.close();

   return 0;
}
