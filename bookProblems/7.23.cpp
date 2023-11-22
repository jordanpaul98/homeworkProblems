#include <iostream>
#include <string>
#include "Team.h"
using namespace std;

int main() {
   string name;
   int wins;
   int losses;
   Team team;

   cin >> name;
   cin >> wins;
   cin >> losses;

   team.SetName(name);
   team.SetWins(wins);
   team.SetLosses(losses);

   team.PrintStanding();
   
   return 0;
}









#include <iostream>
#include <iomanip> 
#include "Team.h"
using namespace std;

void Team::SetName(string name){ this->name = name; }

void Team::SetWins(int wins){ this->wins = wins; }

void Team::SetLosses(int losses){ this->losses = losses; }
   
// TODO: Declare accessor functions - 
//       GetName(), GetWins(), GetLosses()

string Team::GetName() { return name; }

int Team::GetWins() { return wins; }

int Team::GetLosses() { return losses; }
   
// TODO: Implement GetWinPercentage()

double Team::GetWinPercentage() { return (double)wins / (double)(wins + losses); }

// TODO: Implement PrintStanding()

void Team::PrintStanding(){
   cout << "Win percentage: " << fixed << setprecision(2) << GetWinPercentage() << endl;
   if (GetWinPercentage() >= 0.5){
      cout << "Congratulations, Team " << name << " has a winning average!" << endl;
   }else{
      cout << "Team " << GetName() << " has a losing average." << endl;
   }
}













#ifndef TEAMH
#define TEAMH

#include <string>

using namespace std;

class Team {
   // TODO: Declare private data members - name, wins, losses
   
   private:
   string name;
   int wins;
   int losses;
   
   public:
   
   // TODO: Declare mutator functions - 
   //       SetName(), SetWins(), SetLosses()
   
   void SetName(string name);
   void SetWins(int wins);
   void SetLosses(int losses);
   
   // TODO: Declare accessor functions - 
   //       GetName(), GetWins(), GetLosses()
   
   string GetName();
   int GetWins();
   int GetLosses();
   
   // TODO: Declare GetWinPercentage()
   
   double GetWinPercentage();
   
   // TODO: Declare PrintStanding()
   
   void PrintStanding();
};

#endif
