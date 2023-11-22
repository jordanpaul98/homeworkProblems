#include "InventoryNode.h"

int main() {
	int count;
	int numItems;
	string item;

	InventoryNode *headNode = new InventoryNode();
	InventoryNode *currNode;

	// Obtain number of items
	cin >> count;

	// Get each item and number of each
	for (int i = 0; i < count; i++) {
		cin >> item;
		cin >> numItems;
		currNode = new InventoryNode(item, numItems);
		currNode->InsertAtFront(headNode, currNode);
	}

	// Print linked list
	currNode = headNode->GetNext();
	while (currNode != NULL) {
		currNode->PrintNodeData();
		currNode = currNode->GetNext();
	}

	return 0;
}










// InventoryNode.h

#include <iostream>
#include <string>
using namespace std;

class InventoryNode {
private:
	string item;
	int numberOfItems;
	InventoryNode *nextNodeRef;

public:
	//Constructor
	InventoryNode() {
		this->item = "";
		this->numberOfItems = 0;
		this->nextNodeRef = NULL;
	}

	//Constructor
	InventoryNode(string itemInit, int numberOfItemsInit) {
		this->item = itemInit;
		this->numberOfItems = numberOfItemsInit;
		this->nextNodeRef = NULL;
	}

	//Constructor
	InventoryNode(string itemInit, int numberOfItemsInit, InventoryNode nextLoc) {
		this->item = itemInit;
		this->numberOfItems = numberOfItemsInit;
		this->nextNodeRef = &nextLoc;
	}


	// TODO: Define InsertAtFront() member function that inserts a node at the 
	//       front of the linked list (after the dummy head node
	
   void InsertAtFront(InventoryNode *head, InventoryNode *loc){
	   loc->nextNodeRef = head->nextNodeRef;
	   head->nextNodeRef = loc;
	}


	//Get the next node
	InventoryNode *GetNext() {
		return this->nextNodeRef;
	}

	//Print node data
	void PrintNodeData() {
		cout << this->numberOfItems << " " << this->item << endl;
	}
};
