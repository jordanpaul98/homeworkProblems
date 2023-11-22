#include <iostream>

#include "VendingMachine.h"
using namespace std;

int main() {
	/* Type your code here */
	
	int buy, refill;
	VendingMachine machine;
	
	cin >> buy;
	cin >> refill;
	
	machine.Purchase(buy);
	machine.Restock(refill);
	
	machine.Report();
}










// VendingMachine.h\

#ifndef VENDINGMACHINE_H_
#define VENDINGMACHINE_H_

#include <iostream>
using namespace std;

class VendingMachine {

    public:
		VendingMachine();
		void Purchase(int amount);
		int GetInventory();
		void Restock(int amount);
		void Report();

    private:
        int bottles;
};

#endif /* VENDINGMACHINE_H_ */








// VendingMachine.cpp

#include <iostream>
#include <string>

#include "VendingMachine.h"
using namespace std;


VendingMachine::VendingMachine() {
	bottles = 20;
}

void VendingMachine::Purchase(int amount) {
	bottles = bottles - amount;
}

int VendingMachine::GetInventory() {
	return bottles;
}


void VendingMachine::Restock(int amount) {
	bottles = bottles + amount;
}

void VendingMachine::Report() {
	cout << "Inventory: " << bottles << " bottles" << endl;
}
