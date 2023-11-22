#include "MileageTrackerNode.h"
#include <string>
#include <iostream>
using namespace std;

int main () {
   // References for MileageTrackerNode objects
   MileageTrackerNode* headNode;
   MileageTrackerNode* currNode;
   MileageTrackerNode* lastNode;

   double miles;
   string date;
   int i;

   // Front of nodes list
   headNode = new MileageTrackerNode();
   lastNode = headNode;

   // TODO: Read in the number of nodes
      
   int num;
   cin >>  num;

   // TODO: For the read in number of nodes, read
   //       in data and insert into the linked list
   
   currNode = headNode;
   
   for (i=0; i<num; i++){
      cin >> miles;
      cin >> date;
      currNode = new MileageTrackerNode(miles, date, lastNode);
      lastNode->InsertAfter(currNode);
      lastNode = currNode;
   }

   // TODO: Call the PrintNodeData() method
   //       to print the entire linked list
   
   
   currNode = headNode->GetNext();
   while(currNode != nullptr){
      currNode->PrintNodeData();
      currNode = currNode->GetNext();
   }  

   // MileageTrackerNode Destructor deletes all
   //       following nodes
   delete headNode;
}






// MileageTrackerNode.h




#ifndef MILEAGETRACKERNODEH
#define MILEAGETRACKERNODEH

#include <string>
using namespace std;

class MileageTrackerNode {
   public:
      // Constructor
      MileageTrackerNode();

      // Destructor
      ~MileageTrackerNode();

      // Constructor
      MileageTrackerNode(double milesInit, string dateInit);

      // Constructor
      MileageTrackerNode(double milesInit, string dateInit, MileageTrackerNode* nextLoc);

      /* Insert node after this node.
      Before: this -- next
      After:  this -- node -- next
      */
      void InsertAfter(MileageTrackerNode* nodeLoc);

      // Get location pointed by nextNodeRef
      MileageTrackerNode* GetNext();

      void PrintNodeData();
   
   private:
      double miles;         // Node data
      string date;          // Node data
      MileageTrackerNode* nextNodeRef; // Reference to the next node
};

#endif





// MileageTrackerNode.cpp

#include "MileageTrackerNode.h"
#include <iostream>

// Constructor
MileageTrackerNode::MileageTrackerNode() {
   miles = 0.0;
   date = "";
   nextNodeRef = nullptr;
}

// Destructor
MileageTrackerNode::~MileageTrackerNode() {
   if(nextNodeRef != nullptr) {
      delete nextNodeRef;
   }
}

// Constructor
MileageTrackerNode::MileageTrackerNode(double milesInit, string dateInit) {
   miles = milesInit;
   date = dateInit;
   nextNodeRef = nullptr;
}

// Constructor
MileageTrackerNode::MileageTrackerNode(double milesInit, string dateInit, MileageTrackerNode* nextLoc) {
   miles = milesInit;
   date = dateInit;
   nextNodeRef = nextLoc;
}

/* Insert node after this node.
Before: this -- next
After:  this -- node -- next
*/
void MileageTrackerNode::InsertAfter(MileageTrackerNode* nodeLoc) {
   MileageTrackerNode* tmpNext;

   tmpNext = nextNodeRef;
   nextNodeRef = nodeLoc;
   nodeLoc->nextNodeRef = tmpNext;
}

// Get location pointed by nextNodeRef
MileageTrackerNode* MileageTrackerNode::GetNext() {
   return nextNodeRef;
}

void MileageTrackerNode::PrintNodeData(){
   cout << miles << ", " << date << endl;
}
