#include <iostream>
#include <string>

using namespace std;

int GetMonthAsInt(string month) {
	int monthInt = 0;
	
	if (month == "January")
		monthInt = 1;
	else if (month == "February")
		monthInt = 2;
	else if (month == "March")
		monthInt = 3;
	else if (month == "April")
		monthInt = 4;
	else if (month == "May")
		monthInt = 5;
	else if (month == "June")
		monthInt = 6;
	else if (month == "July")
		monthInt = 7;
	else if (month == "August")
		monthInt = 8;
	else if (month == "September")
		monthInt = 9;
	else if (month == "October")
		monthInt = 10;
	else if (month == "November")
		monthInt = 11;
	else if (month == "December")
		monthInt = 12;
	return monthInt;
}

int main () {
	
	string str;
	
	getline(cin, str);
	
	while (str != "-1"){
      int com = str.find(",");
      int spc = str.find(" ");
      
      if (com != -1 && spc != -1){
         string month = str.substr(0, spc);
         string day = str.substr(spc + 1, com - spc - 1);
         string year = str.substr(com + 2, str.length() - com);
         
         cout << GetMonthAsInt(month) << "-" << day << "-" << year << endl;
      }
      getline(cin, str);
	}

}
