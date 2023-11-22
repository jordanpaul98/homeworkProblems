#include <iostream>
#include <cstring>
#include <fstream>

// Include any necessary libraries here.

using namespace std;

int main() {

   ifstream file;
   ofstream out;
   string line, fName;
   
   cin >> fName;
   
   file.open(fName);
   if (!file.is_open()){
      return 1;
   }
   
   while (getline(file, line)){
      int pos = line.find("_photo");
      if (pos != -1){
         line.replace(pos, 10, "_info.txt");
      }
      
      cout << line << endl;
      
   }
   
   file.close();

   return 0;
}
