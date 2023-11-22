#include <iostream>
using namespace std;

void SwapValues(int& userVal1, int& userVal2, int& userVal3, int& userVal4){
   int temp;
   temp = userVal1;
   userVal1 = userVal2;
   userVal2 = temp;
   
   temp = userVal3;
   userVal3 = userVal4;
   userVal4 = temp;
}

int main() {
   int v1, v2, v3, v4;
   cin >> v1;
   cin >> v2;
   cin >> v3;
   cin >> v4;
   
   SwapValues(v1, v2, v3, v4);
   
   cout << v1 << " " << v2 << " " << v3 << " " << v4 << endl;

   return 0;
}
