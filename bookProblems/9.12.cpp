#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;

int main() {

   ifstream file;
   ofstream out;
   
   string fName, grade, line;
   
   cin >> fName;
   
   file.open(fName);
   if (!file.is_open()) return 1;
   
   out.open("report.txt");
   if (!out.is_open()) return 1;
      
      
   /* TODO: Read a file name from the user and read the tsv file here. */
   
   int g1, g2, g3, sts = 0;
   double mid1, mid2, mid3;
   mid1 = 0;
   mid2 = 0;
   mid3 = 0;
   
   string firstName, lastName;
   
   while (getline(file, line)){
    istringstream iss(line);
    
    iss >> firstName;
    iss >> lastName;
    iss >> g1;
    iss >> g2;
    iss >> g3;
    
    mid1 += g1;
    mid2 += g2;
    mid3 += g3;

    double total = (g1 + g2 + g3) / 3.0;  // Fix: declare total inside the loop
    
    if (total < 60) grade = "F";
    else if (total < 70) grade = "D";
    else if (total < 80) grade = "C";
    else if (total < 90) grade = "B";
    else grade = "A";
    
    cout << line << "\t" << grade << endl;
    
    out << line << "\t" << grade << endl;
    sts++;
   }

   /* TODO: Compute student grades and exam averages, then output results to a text file here. */
   
   mid1 = mid1 / sts;
   mid2 = mid2 / sts;
   mid3 = mid3 / sts;
   
   cout << mid1 << " " << mid2 <<  " " << mid3 << endl;
   
   out << endl;
   out << fixed << setprecision(2) <<  "Averages: midterm1 " << mid1 << ", midterm2 ";
   out << fixed << setprecision(2) << mid2 << ", final " << mid3 << endl;
   
   file.close();
   out.close();

   return 0;
}
