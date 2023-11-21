#include <iostream>
#include <cstdlib>
using namespace std;

string CoinFlip(){
   if (rand() % 2 == 0) {
      return "Tails";
   }else{
      return "Heads";
   }
}

int main() {
   // Add more variables as needed
   
   int i, flips, seedVal;
   
   cin >> flips;
   cin >> seedVal;
   
   srand(seedVal);  // Unique seed

   for (i = 0; i < flips; i++){
      cout << CoinFlip() << endl;
   }

   return 0;
}
