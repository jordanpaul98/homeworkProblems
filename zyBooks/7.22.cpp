#include <iostream>
#include "Car.h"
using namespace std;

int main() {
   int userYear;
   int userPrice;
   int userCurrentYear;
   Car myCar;
      
   cin >> userYear;
   cin >> userPrice;
   cin >> userCurrentYear;
      
   myCar.SetModelYear(userYear);
   myCar.SetPurchasePrice(userPrice);
   myCar.CalcCurrentValue(userCurrentYear);
      
   myCar.PrintInfo();
   
   return 0;
}




//  car.cpp

#include <iostream>
#include <iomanip>
#include <cmath>
#include "Car.h"
using namespace std;

void Car::SetModelYear(int userYear){
   modelYear = userYear;
}

int Car::GetModelYear() const {
   return modelYear;
}

// TODO: Implement SetPurchasePrice() function

void Car::SetPurchasePrice(int price){
   purchasePrice = price;
}

int Car::GetPurchasePrice(){
   return purchasePrice;
}

// TODO: Implement GetPurchasePrice() function

void Car::CalcCurrentValue(int currentYear) {
   double depreciationRate = 0.15;
   int carAge = currentYear - modelYear;
      
   // Car depreciation formula
   currentValue = purchasePrice * pow((1 - depreciationRate), carAge);
}

// TODO: Implement PrintInfo() function to output modelYear, purchasePrice, and 
// currentValue

void Car::PrintInfo(){
     cout << "Car's information:" << endl;
     cout << "  Model year: " << GetModelYear() <<  endl;
     cout << "  Purchase price: $" << purchasePrice << endl;
     cout <<  fixed << setprecision(0) << "  Current value: $" << currentValue << endl;
}








//car.h


#ifndef CARH
#define CARH

class Car {
   private:
      int modelYear; 
      // TODO: Declare purchasePrice member (int)
      int purchasePrice;
      double currentValue;
   
   public:
      void SetModelYear(int userYear);

      int GetModelYear() const;
   
      // TODO: Declare SetPurchasePrice() function
      
      void SetPurchasePrice(int price);
   
      // TODO: Declare GetPurchasePrice() function
      int GetPurchasePrice();
   
      void CalcCurrentValue(int currentYear);
   
     // TODO: Declare PrintInfo() method to output modelYear, purchasePrice, and 
     // currentValue
     
     void PrintInfo();
   
};

#endif
