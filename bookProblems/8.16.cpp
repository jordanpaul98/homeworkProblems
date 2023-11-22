#include <iostream>
#include "SongNode.h"

// TODO: Write PrintPlaylist() function

void PrintPlaylist(SongNode *head){
   SongNode* node = head->GetNext();
   while (node != nullptr) {
      node->PrintSongInfo();
      node = node->GetNext();
      if (node != nullptr) cout << endl;
   }
}

int main() {
	SongNode* headNode;
	SongNode* currNode;
	SongNode* lastNode;

	string songTitle;
	string songLength;
	string songArtist;

	// Front of nodes list                                                                         
	headNode = new SongNode();
	lastNode = headNode;

	// Read user input until -1  entered
	getline(cin, songTitle);
	while (songTitle != "-1") {
		getline(cin, songLength);
		getline(cin, songArtist);

		currNode = new SongNode(songTitle, songLength, songArtist);
		lastNode->InsertAfter(currNode);
		lastNode = currNode;

		getline(cin, songTitle);
	}

	// Print linked list
	cout << "LIST OF SONGS" << endl;
	cout << "-------------" << endl;
	PrintPlaylist(headNode);
	
	return 0;
}




//  SongNode.h

#include "iostream"
#include <string>

using namespace std;

class SongNode {
private:
	string songTitle;
	string songLength;
	string songArtist;
	SongNode* nextNodeRef; // Reference to the next node                                   

public:
	SongNode() {
		songTitle = "";
		songLength = "";
		songArtist = "";
		nextNodeRef = NULL;
	}

	// Constructor                                                                                     
	SongNode(string songTitleInit, string songLengthInit, string songArtistInit);

	// Constructor                                                                                     
	SongNode(string songTitleInit, string songLengthInit, string songArtistInit, SongNode* nextLoc);

	// insertAfter
	void InsertAfter(SongNode* nodeLoc);

	// Get location pointed by nextNodeRef                                                            
	SongNode* GetNext();
   
   // Prints song information   
	void PrintSongInfo();
};





//SongNode.cpp

#include "SongNode.h"

// Constructor                                                                                     
SongNode::SongNode(string songTitleInit, string songLengthInit, string songArtistInit) {
	this->songTitle = songTitleInit;
	this->songLength = songLengthInit;
	this->songArtist = songArtistInit;
	this->nextNodeRef = NULL;
}

// Constructor                                                                                     
SongNode::SongNode(string songTitleInit, string songLengthInit, string songArtistInit, SongNode* nextLoc) {
	this->songTitle = songTitleInit;
	this->songLength = songLengthInit;
	this->songArtist = songArtistInit;
	this->nextNodeRef = nextLoc;
}

// insertAfter
void SongNode::InsertAfter(SongNode* nodeLoc) {
	SongNode* tmpNext;
	tmpNext = this->nextNodeRef;
	this->nextNodeRef = nodeLoc;
	nodeLoc->nextNodeRef = tmpNext;
}

// Get location pointed by nextNodeRef                                                            
SongNode* SongNode::GetNext() {
	return this->nextNodeRef;
}

void SongNode::PrintSongInfo(){
      cout << "Title: " << this->songTitle << endl;
      cout << "Length: " << this->songLength << endl;
      cout << "Artist: " << this->songArtist << endl;
}
